
import os.path
import sys

def modImportPath():
	myDir = os.path.dirname(os.path.abspath(__file__))
	sys.path.insert(0, os.path.join(os.path.abspath(myDir), '..'))

modImportPath()

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

def prepMessage(expectedTree, actualTree, message, params):

	if message != None:
		if params != None:
			message = message % params
	else:
		message = ''

	return message + "\nExpected: %s\n  Actual: %s" % (expectedTree, actualTree)


def assertTreesMatch(expectedTree, actualTree, message=None, *params):
	if isinstance(expectedTree, Operator) and isinstance(actualTree, Operator):
		assertTreesMatch(expectedTree.left, actualTree.left)
		assertTreesMatch(expectedTree.right, actualTree.right)
	message = prepMessage(expectedTree, actualTree, message, params)
	assert expectedTree == actualTree, message

def assertTreesDifferent(expectedTree, actualTree, message=None, *params):
	if isinstance(expectedTree, Operator) and isinstance(actualTree, Operator):
		assertTreesMatch(expectedTree.left, actualTree.left)
		assertTreesMatch(expectedTree.right, actualTree.right)
	message = prepMessage(expectedTree, actualTree, message, params)
	assert expectedTree != actualTree, message
