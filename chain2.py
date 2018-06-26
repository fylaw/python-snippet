#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Chain(object):
	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

	def __call__(self, id):
		return Chain('%s/%s' % (self._path, id))


if __name__ == '__main__':
#	print(Chain().status.user.timeline.list)
	print(Chain().users('michael').repos)