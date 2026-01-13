import asyncio
from agents.basicagent.sample import sample
from agents.backends.utils import EnvironmentConfig, ExecutionConstraints, ModelConfig


LAB_ENVIRONMENTS = [
    "cloningscenarios",
    "dbqa",
    "figqa",
    "litqa2",
    "protocolqa",
    "seqqa",
    "suppqa",
    "tableqa",
]


async def main() -> None:
    for environment_name in LAB_ENVIRONMENTS:
        await sample(
            environment_config=EnvironmentConfig(
                environment=environment_name,
                split="test",
                host="http://labbench.default.34.121.159.27.nip.io",
                max_tasks=1,
            ),
            model_config=ModelConfig(
                model="deepseek/deepseek-chat",
                backend_name="openrouter",
                max_output_tokens=16_000,
                max_context_window=128_000,
            ),
            local_log_dir="logs",
        )


if __name__ == "__main__":
    asyncio.run(main())
