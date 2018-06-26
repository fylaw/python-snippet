#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class A(object):
	def foo(self):
		print('A foo')

	def bar(self):
		print('A bar')

class B(object):
	def foo(self):
		print('B foo')
	def bar(self):
		print('B bar')

class C1(A):
	def bar(self):
		print('C1 bar')
		
class C2(B):
	def bar(self):
		print('C2 bar')

class D(C1,C2):
	pass

class E(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'E object (name:%s)' % self.name
		
	__repr__ = __str__	

if __name__ == '__main__':
	print(D.__mro__)
	d = D()
	d.foo()
	d.bar()

	e = E('Michael')
	print(e)
		

		

		
