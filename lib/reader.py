#!/usr/bin/python3.11.8
from collections.abc import Generator

class Reader(object):

    """
    A simple implementation for static file reading.
    The benefit is just it reads all files, but in memory
    friendly way.
    """
    
    def __init__(self, path: str) -> None:
        self.file = open(path, "r")
        pass

    def read(self) -> Generator[str]:
        lines = (line.strip() for line in self.file.readlines())
        self.file.close()
        return lines

class PositionalReader(object):
    """
    For now this class ommited, because of lack of time and simplicity of this project.
    """
    pass

