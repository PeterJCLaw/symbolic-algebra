
from thing import Thing

class Operator(Thing):
	_left = None
	_right = None
	# The type of operator, this should be provided by implementing classes
	_type = None

	def __init__(self, left, right):
		self._left = left
		self._right = right

	def __eq__(self, other):
		return isinstance(other, type(self)) and self._left == other._left and self._right == other._right

	def __ne__(self, other):
		return not (self == other)

	def __repr__(self):
		return "%s(%s %s %s)" % (self.__class__.__name__, self._left, self._type, self._right)

	@property
	def left(self):
		return self._left

	@property
	def right(self):
		return self._right
