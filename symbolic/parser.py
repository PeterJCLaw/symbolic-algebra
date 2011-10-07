
import re
from string import whitespace

class ParseException(Exception):
	pass

class Parser(object):
	_operators = '=*/+-'
	_punctuation = _operators[0] + '()' + _operators[1:]

	def parse(self, string):
		string = string.strip()
		print self._punctuation

		for token in self.tokenise(string):
			print "'"+token+"'"

		return None

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
