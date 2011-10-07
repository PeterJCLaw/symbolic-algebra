
from thing import Thing

class Operator(Thing):
	_left = None
	_right = None

	def __init__(self, left, right):
		self._left = left
		self._right = right

	@property
	def left(self):
		return self._left

	@property
	def right(self):
		return self._right

	def __eq__(self, other):
		return self._left == other._left and self._right == other._right

	def __ne__(self, other):
		return not (self == other)
