import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from preprocessors import parserData

def process(draws, conn):
    parserData.parser(draws, conn)