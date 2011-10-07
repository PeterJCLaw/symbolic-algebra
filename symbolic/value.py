
from thing import Thing

class Value(Thing):
	_value = None
	def __init__(self, value):
		self._value = value

	def __cmp__(self, other):
		return self._value.__cmp__(other._value)

	def __hash__(self):
		return self._value

	def __repr__(self):
		return "Value(%s)" % self._value

	def __nonzero__(self):
		return self._value != 0

	@property
	def value(self):
		return self._value
