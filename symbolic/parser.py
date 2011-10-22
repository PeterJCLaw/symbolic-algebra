
import re
from string import whitespace

# Local imports
from .operators import *
from operator import Operator
from symbol import Symbol
from thing import Thing
from value import Value

class ParseException(Exception):
	pass

class Parser(object):
	_operators = '^*/+-='
	_leftBracket = '('
	_rightBracket = ')'
	_punctuation = _leftBracket + _rightBracket + _operators

	def parse(self, string):
		string = string.strip()
		self._groupStack = []
		self._leftStack = []
	#	print 'Parsing:', string

		for token in self.tokenise(string):
		#	print "'"+token+"'"
			if token in self._operators:
				operatorType = self._createOperator(token)
				self._addOperator(operatorType)
			elif token.isdigit():
				self._appendOrMerge(Value(int(token)))
			elif token[0].isalpha() and token.isalnum():
				self._appendOrMerge(Symbol(token))
			elif token is self._leftBracket:
				self._groupStack.append(self._leftStack)
				self._leftStack = []
			elif token is self._rightBracket:
				oldLeft = self._leftStack
			#	print 'oldLeft', oldLeft
				self._leftStack = self._groupStack.pop()
			#	print 'popped ', self._leftStack
				self._appendOrMerge(oldLeft)
			else:
				raise ParseException("Got unexpected token '%s'." % token)
		#	print self._leftStack

		if len(self._leftStack) == 0:
			return None

		tree = self._removeGrouping(self._leftStack)
	#	print tree
		return tree

	def _addOperator(self, opType):
		# get one from the stack, or error
		last = self._leftStack.pop()
	#	print 'opType=%s' % opType
	#	print 'last=%s' % last

		if isinstance(last, Operator) and self._higherPrecedence(opType, type(last)):
	#		print 'doing something clever'
			self._leftStack.append(last)
			# TODO: avoid this hack
			newOp = last._right = opType(last.right, None)
		else:
			newOp = opType(last, None)

		self._appendOrMerge(newOp)

	def _appendOrMerge(self, item):
		if len(self._leftStack) == 0:
			self._leftStack.append(item)
			return

		last = self._leftStack[-1]
	#	print 'item=%s' % item
	#	print 'last=%s' % last
		if isinstance(last, Operator) and last.right is None:
			# TODO: avoid this hack
			last._right = item

	def _higherPrecedence(self, first, second):
		"""
		Determines if the first Operator type has higher precedence than the second.
		"""
	#	print first, second
		firstPos  = self._operators.index(first._type)
		secondPos = self._operators.index(second._type)
		return firstPos < secondPos

	def _removeGrouping(self, tree):
		if isinstance(tree, list):
			tree = tree[0]
		if isinstance(tree, Operator):
			tree._left  = self._removeGrouping(tree._left)
			tree._right = self._removeGrouping(tree._right)
		return tree

	def tokenise(self, string):
		token = ''
		for s in string:
			# token boundary
			if s in whitespace:
				if token != '':
					yield token
					token = ''
			elif s in self._punctuation:
				if token != '':
					yield token
					token = ''
				yield s
			elif s.isalnum():
				token += s
			else:
				raise ParseException("Got invalid token '%s'." % s)

		if token != '':
			yield token

	def _createOperator(self, token):
		if token == '=':
			return Equality
		elif token == '^':
			return Exponent
		elif token == '*':
			return Multiplication
		elif token == '/':
			return Division
		elif token == '+':
			return Addition
		elif token == '-':
			return Subtraction
