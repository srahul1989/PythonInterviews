__author__ = 'rahul'
'''
There are three ways that the parent and child classes can interact:
1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.

'''
#
## Implicit Inheritance::

class Parent(object):
    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

#print "dad.implicit() : ", dad.implicit()
#print "son.implicit() : ", son.implicit()
###############################################
#
## Override explicitly

class Parent1(object):
    def override(self):
        print "Parent override ====>>"

class Child1(Parent1):
    def override(self):
        print "Child override ====>>"

dad1 = Parent1()
son1 = Child1()

#print "dad1.override() : ", dad1.override()
#print "son1.override() : ", son1.override()
##################################################
#
## After Before or After

class Parent2(object):
    def altered(self):
        print "Inside Parent2 altered==>"

class Parent3(object):
    def altered(self):
        print "Inside Parent3 altered==>"


class Child2(Parent2, Parent3):
    def altered(self):
        print "before calling to parent class inside child"
        super(Child2, self).altered()
        print "after calling to parent class inside child"

dad2 = Parent2()
son2 = Child2()
print "dad2 altered ==: ", dad2.altered()
print "son2 altered ==: ", son2.altered()
