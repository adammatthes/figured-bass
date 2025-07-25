import unittest
from harmony_graph import *

class TestHarmonyGraph(unittest.TestCase):
    def test_access_keys(self):
        hg = Harmony_Graph()
        numeral_set = hg.graph[I]
        self.assertEqual(V in numeral_set, True)
        numeral_set = hg.graph[ii]
        self.assertEqual(V in numeral_set, True)
        self.assertEqual(vi in hg.graph[iii], True)
        self.assertEqual(V in hg.graph[IV], True)
        self.assertEqual(I in hg.graph[V], True)
        self.assertEqual(V in hg.graph[vi], True)
        self.assertEqual(I6 in hg.graph[viio], True)

