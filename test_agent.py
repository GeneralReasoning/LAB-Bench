import json
import asyncio
import os
import sys

from openai import AsyncOpenAI
from openreward import OpenReward

async def main():
    or_client = OpenReward()
    oai_client = AsyncOpenAI()

    MODEL_NAME = "gpt-5.2"

    # Choose which environment to test (default: protocolqa)
    ENV_NAME = "labbench"
    SPLIT = "test"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY environment variable not set")
        return

    print(f"Testing environment: {ENV_NAME}")
    print(f"Using model: {MODEL_NAME}")
    print()

    environment = or_client.environments.get(name=ENV_NAME, base_url="http://localhost:8080", variant="figqa")
    tasks = await environment.list_tasks(split=SPLIT)
    tools = await environment.list_tools(format="openai")

    print(f"Found {len(tasks)} tasks")
    print(tools)
    print()

    # Test first task
    for task in tasks[:1]:
        print(f"Testing task: {task.task_spec.get('id', 'unknown')}")
        print("-" * 80)

        rollout = or_client.rollout.create(
            run_name=ENV_NAME + "_test",
            rollout_name="test_run",
            environment=ENV_NAME,
            split=SPLIT,
            task_spec=task.task_spec
        )

        async with environment.session(task=task, secrets={"openai_api_key": OPENAI_API_KEY}) as session:
            prompt = await session.get_prompt()

            # Display the question
            print("Question:")
            print(prompt[0].text[:500] + "..." if len(prompt[0].text) > 500 else prompt[0].text)
            print()

            input_list = [{"role": "user", "content": prompt[0].text}]
            finished = False

            rollout.log_openai_response(message=input_list[0], is_finished=finished)

            turn_count = 0
            max_turns = 10  # Prevent infinite loops

            while not finished and turn_count < max_turns:
                turn_count += 1
                print(f"Turn {turn_count}:")

                response = await oai_client.responses.create(
                    model=MODEL_NAME,
                    tools=tools,
                    input=input_list
                )

                rollout.log_openai_response(response.output[-1])
                input_list += response.output

                for item in response.output:
                    if item.type == "function_call":
                        print(f"  Tool called: {item.name}")

                        # Parse arguments
                        try:
                            args = json.loads(str(item.arguments))
                            print(f"  Arguments: {args}")
                        except json.JSONDecodeError:
                            print(f"  Arguments (raw): {item.arguments}")
                            args = {}

                        # Call the tool
                        tool_result = await session.call_tool(item.name, args)

                        reward = tool_result.reward
                        finished = tool_result.finished

                        # Get output text
                        if tool_result.blocks:
                            if hasattr(tool_result.blocks[0], 'text'):
                                output_text = tool_result.blocks[0].text
                            elif hasattr(tool_result.blocks[0], 'data'):
                                # ImageBlock
                                output_text = f"[Image returned: {len(tool_result.blocks[0].data)} bytes]"
                            else:
                                output_text = str(tool_result.blocks[0])
                        else:
                            output_text = "No output"

                        input_list.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": output_text
                        })

                        rollout.log_openai_response(input_list[-1], reward=reward, is_finished=finished)

                        print(f"  Output: {output_text[:100] + '...' if len(output_text) > 100 else output_text}")
                        if reward is not None:
                            print(f"  Reward: {reward:.3f}")
                        print(f"  Finished: {finished}")
                        print()

                        if finished:
                            print("=" * 80)
                            print(f"TASK COMPLETED!")
                            print(f"Final Reward: {reward:.3f}")
                            print(f"Result: {'✓ CORRECT' if reward > 0.5 else '✗ INCORRECT'}")
                            print("=" * 80)
                            break

                    elif item.type == "text":
                        # Model generated text response
                        text_content = item.text if hasattr(item, 'text') else str(item)
                        print(f"  Model response: {text_content[:200] + '...' if len(text_content) > 200 else text_content}")

            if not finished:
                print()
                print("Warning: Max turns reached without completion")

if __name__ == "__main__":
    print("LAB-Bench Agent Test")
    print("=" * 80)
    print()
    print("Usage: python test_agent.py [environment]")
    print("Available environments:")
    print("  - protocolqa (default)")
    print("  - seqqa")
    print("  - tableqa")
    print("  - suppqa")
    print("  - cloningscenarios")
    print("  - figqa")
    print("  - dbqa")
    print("  - litqa2")
    print()

    asyncio.run(main())
