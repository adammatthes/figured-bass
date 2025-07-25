import unittest
from harmony_graph import *

class TestHarmonyGraph(unittest.TestCase):
    def test_access_keys(self):
        numeral_list = Harmony_Graph().graph[I]
        self.assertEqual(V in numeral_list, True)
