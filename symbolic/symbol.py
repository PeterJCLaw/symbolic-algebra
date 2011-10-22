
from thing import Thing

class Symbol(Thing):
	_name = None
	def __init__(self, name):
		self._name = name

	def __lt__(self, other):
		return isinstance(other, type(self)) and self._name < other._name

	def __le__(self, other):
		return isinstance(other, type(self)) and self._name <= other._name

	def __eq__(self, other):
		return isinstance(other, type(self)) and self._name == other._name

	def __ne__(self, other):
		return isinstance(other, type(self)) and self._name != other._name

	def __gt__(self, other):
		return isinstance(other, type(self)) and self._name > other._name

	def __ge__(self, other):
		return isinstance(other, type(self)) and self._name >= other._name

	def __hash__(self):
		return hash(self._name)

	def __repr__(self):
		return "Symbol(%s)" % self._name

	@property
	def name(self):
		return self._name
