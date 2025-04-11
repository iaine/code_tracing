"""
Functions to work with types
"""
import json

class read_types():

    def __init__(self):
      self.typ = {}

    def read(self, datastructure):
      """
      Read the type and add to structure
      """
      _types = type(datastructure)
      self.typ[datastructure] = str(_types)
