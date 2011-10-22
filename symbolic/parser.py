
import re
from string import whitespace

# Local imports
from addition import Addition
from division import Division
from equality import Equality
from exponent import Exponent
from multiplication import Multiplication
from operator import Operator
from subtraction import Subtraction
from symbol import Symbol
from thing import Thing
from value import Value

class ParseException(Exception):
	pass

class Parser(object):
	_operators = '^*/+-='
	_punctuation = '()' + _operators

	def parse(self, string):
		string = string.strip()
		self._leftStack = []
	#	print

		for token in self.tokenise(string):
		#	print "'"+token+"'"
			if token in self._operators:
				operatorType = self._createOperator(token)
				self._addOperator(operatorType)
			elif token.isdigit():
				self._appendOrMerge(Value(int(token)))
			elif token[0].isalpha() and token.isalnum():
				self._appendOrMerge(Symbol(token))
			else:
				raise ParseException("Got unexpected token '%s'." % token)

	#	print self._leftStack

		if len(self._leftStack) == 0:
			return None

		return self._leftStack[0]

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
			self._leftStack[-1]._right = item

	def _higherPrecedence(self, first, second):
		"""
		Determines if the first Operator type has higher precedence than the second.
		"""
	#	print first, second
		firstPos  = self._operators.index(first._type)
		secondPos = self._operators.index(second._type)
		return firstPos < secondPos

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
