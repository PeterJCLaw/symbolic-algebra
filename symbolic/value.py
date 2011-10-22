
from thing import Thing

class Value(Thing):
	_value = None
	def __init__(self, value):
		self._value = value

	def __lt__(self, other):
		return isinstance(other, type(self)) and self._value < other._value

	def __le__(self, other):
		return isinstance(other, type(self)) and self._value <= other._value

	def __eq__(self, other):
		return isinstance(other, type(self)) and self._value == other._value

	def __ne__(self, other):
		return not isinstance(other, type(self)) or self._value != other._value

	def __gt__(self, other):
		return isinstance(other, type(self)) and self._value > other._value

	def __ge__(self, other):
		return isinstance(other, type(self)) and self._value >= other._value

	def __hash__(self):
		return self._value

	def __repr__(self):
		return "Value(%s)" % self._value

	def __nonzero__(self):
		return self._value != 0

	@property
	def value(self):
		return self._value
