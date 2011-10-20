
# External
import unittest

# Local
import util
util.modImportPath()
from symbolic import *

class ParserTests(unittest.TestCase):

	def setUp(self):
		self._parser = Parser()

	def assertParse(self, expectedTree, string):
		parsedTree = self._parser.parse(string)

		util.assertTreesMatch(expectedTree, parsedTree)

	def test_simpleEqaulity(self):
		expectedTree = Equality(Addition(Symbol('A'), Value(1)), Value(0))

		self.assertParse(expectedTree, "A + 1 = 0")

	def test_simpleMultiplication(self):
		expectedTree = Addition(Value(3),
		                        Multiplication(Value(4), Value(5))
		                       )

		self.assertParse(expectedTree, "3 + 4 * 5")

	def test_operatorPrecedence1(self):
		expectedTree = Addition(Multiplication(Value(4), Value(5)),
		                        Value(3)
		                       )

		self.assertParse(expectedTree, "4 * 5 + 3")

	def test_operatorPrecedence2(self):
		expectedTree = Addition(Division(Value(4), Value(5)),
		                        Value(3)
		                       )

		self.assertParse(expectedTree, "4 / 5 + 3")

	def test_operatorPrecedence3(self):
		expectedTree = Subtraction(Multiplication(Value(4), Value(5)),
		                           Value(3)
		                          )

		self.assertParse(expectedTree, "4 * 5 - 3")

if __name__ == '__main__':
	unittest.main()
