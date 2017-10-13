from math import sqrt



class Point(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def func(self):
		return sqrt(self.x **2 + self.y ** 2)	

	def __repr__(self):
		return "Point({}, {}) ".format(self.x, self.y)


class Rectangle(object):

	def __init__(self, p1, p2, p3, p4):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4		


class NewRectangle(Rectangle):
	
	def __repr__(self):
		return "Rectangle({}, {}, {}, {})".format(self.p1,self.p2,self.p3,self.p4)
