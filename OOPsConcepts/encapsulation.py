'''encapsulation: is the mechanism for restricting the access to some of an
 	object's components, this means that the internal representation of an object 
 	can't be seen from outside of the objects definition. Access to this data is 
 	typically only achieved through special methods: Getters and Setters. By using 
 	solely get() and set() methods, we can make sure that the internal data cannot 
 	be accidentally set into an inconsistent or invalid state.
'''

class Encapsultion(object):
 	def __init__(self, a, b, c):
 		self.public = a
 		self._protected = b
 		self.__private = c

x = Encapsultion(11,13,17)
print "x.public : ", x.public
print "x._protected : ", x._protected
print "x.__private : ", x.__private