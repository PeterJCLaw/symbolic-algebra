
import re
from string import whitespace

# Local imports
from addition import Addition
from equality import Equality
from multiplication import Multiplication
from operator import Operator
from symbol import Symbol
from thing import Thing
from value import Value

class ParseException(Exception):
	pass

class Parser(object):
	_operators = '=*/+-'
	_punctuation = _operators[0] + '()' + _operators[1:]

	def parse(self, string):
		string = string.strip()
		self._leftStack = []
		print self._punctuation

		for token in self.tokenise(string):
			print "'"+token+"'"
			if token in self._operators:
				# get one from the stack, or error
				last = self._leftStack.pop()
				operator = self._createPunctuation(token)
				self.appendOrMerge(operator(last, None))
				pass
			elif token.isdigit():
				self.appendOrMerge(Value(int(token)))
			elif token[0].isalpha() and token.isalnum():
				self.appendOrMerge(Symbol(token))
			else:
				raise ParseException("Got unexpected token '%s'." % token)

		print self._leftStack

		if len(self._leftStack) == 0:
			return None

		return self._leftStack[0]

	def appendOrMerge(self, item):
		if len(self._leftStack) == 0:
			self._leftStack.append(item)
			return

		last = self._leftStack[-1]
		print 'last=%s' % last
		if isinstance(last, Operator) and last.right is None:
			# TODO: avoid this hack
			self._leftStack[-1]._right = item

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

		yield token

	def _createPunctuation(self, token):
		if token == '=':
			return Equality
		elif token == '*':
			return Multiplication
		elif token == '+':
			return Addition
