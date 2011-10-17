
import os.path
import sys
sys.path.insert(0, os.path.abspath('.'))

from symbolic import *

def buildSimpleTree():
	"""
	Returns the very simple tree that represents: "A + 1 = 0"
	"""
	return Equality(Addition(Symbol('A'), Value(1)), Value(0))

def assertSimpleTrees(expectedTree, actualTree):
	assert expectedTree.left.left == actualTree.left.left
	assert expectedTree.left.right == actualTree.left.right
	assert expectedTree.left == actualTree.left
	assert expectedTree.right == actualTree.right
	assert expectedTree == actualTree

def assertParse(expectedTree, string):
	p = Parser()
	parsedTree = p.parse(string)

	assertSimpleTrees(expectedTree, parsedTree)

def modelTest():
	expectedTree = buildSimpleTree()
	actualTree = buildSimpleTree()

	assertSimpleTrees(expectedTree, actualTree)

def parserTest():
	expectedTree = buildSimpleTree()

	assertParse(expectedTree, "A + 1 = 0")

def parserTest2():
	expectedTree = Addition(Value(3),
	                        Multiplication(Value(4), Value(5))
	                       )

	assertParse(expectedTree, "3 + 4 * 5")

def parserTest3():
	expectedTree = Addition(Multiplication(Value(4), Value(5)),
	                        Value(3)
	                       )

	assertParse(expectedTree, "4 * 5 + 3")

if __name__ == '__main__':
	print 'modelTest\t',
	try:
		modelTest()
		print 'PASS',
	finally:
		print
	print 'parserTest\t',
	try:
		parserTest()
		print 'PASS',
	finally:
		print
	print 'parserTest2\t',
	try:
		parserTest2()
		print 'PASS',
	finally:
		print
	print 'parserTest3\t',
	try:
		parserTest3()
		print 'PASS',
	finally:
		print
