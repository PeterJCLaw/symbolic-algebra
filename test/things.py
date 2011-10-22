
# External
import unittest

# Local
import util
util.modImportPath()
from symbolic import *

class ThingsTests(unittest.TestCase):
	# Variables to be overridden
	_type = None	# The Thing type to test
	_a = None		# The smaller value
	_b = None		# The larger value

	def test_equals(self):
		a = self._type(self._a)
		b = self._type(self._a)

		util.assertTreesMatch(a, b, "Two instances with the same value (%s) should be equal" % self._a)

	def test_notEquals(self):
		a = self._type(self._a)
		b = self._type(self._b)

		util.assertTreesDifferent(a, b, "Two instances with the different values (%s, %s) should not be equal" % (self._a, self._b))

	def test_notEqualsOtherType(self):
		a = self._type(self._a)

		assert a != self, "An instance should not claim to be equal to an arbitrary object"
		self.assertNotEqual(a, self, "An instance should not claim to be equal to an arbitrary object")

	def test_notNone(self):
		a = self._type(self._a)

		util.assertTreesDifferent(a, None, "An instance should not claim to be None")

	def test_greater(self):
		a = self._type(self._a)
		b = self._type(self._b)

		self.assertGreater(b, a)

	def test_less(self):
		a = self._type(self._a)
		b = self._type(self._b)

		self.assertLess(a, b)


class SymbolTests(ThingsTests):
	_type = Symbol
	_a = 'A'
	_b = 'B'

class ValueTests(ThingsTests):
	_type = Symbol
	_a = 2
	_b = 5
