
# External
import unittest

# Local
import util
util.modImportPath()
from symbolic import *

class TreeTests(unittest.TestCase):

	def buildSimpleTree(self):
		"""
		Returns the very simple tree that represents: "A + 1 = 0"
		"""
		return Equality(Addition(Symbol('A'), Value(1)), Value(0))

	def test_model_equals(self):
		expectedTree = self.buildSimpleTree()
		actualTree = self.buildSimpleTree()

		util.assertSimpleTrees(expectedTree, actualTree)
		util.assertTreesMatch(expectedTree, actualTree)

	def test_model_different(self):
		expectedTree = self.buildSimpleTree()
		actualTree = Value(4)

		util.assertTreesDifferent(expectedTree, actualTree)


if __name__ == '__main__':
	unittest.main(buffer=True)
