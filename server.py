from openreward.environments import Server

from cloningscenarios import CloningScenarios
from dbqa import DBQA
from figqa import FigQA
from litqa2 import LitQA2
from protocolqa import ProtocolQA
from seqqa import SeqQA
from suppqa import SuppQA
from tableqa import TableQA

if __name__ == "__main__":
    server = Server([CloningScenarios, DBQA, FigQA, LitQA2, ProtocolQA, SeqQA, SuppQA, TableQA])
    server.run()
