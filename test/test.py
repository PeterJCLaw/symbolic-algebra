
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

def modelTest():
	expectedTree = buildSimpleTree()
	actualTree = buildSimpleTree()

	assertSimpleTrees(expectedTree, actualTree)

def parserTest():
	expectedTree = buildSimpleTree()

	p = Parser()
	parsedTree = p.parse("A + 1 = 0")

	assertSimpleTrees(expectedTree, parsedTree)

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
