#!/usr/bin/python3.11.8
from collections.abc import Generator

class Reader(object):

    def __init__(self, path: str) -> None:
        self.file = open(path, "r")
        pass

    def read(self) -> Generator[str]:
        lines = (line.strip() for line in self.file.readlines())
        self.file.close()
        return lines

class PositionalReader(object):
    pass

