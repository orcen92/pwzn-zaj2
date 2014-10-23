# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=1):
	"""
	Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
	która działa dla liczb całkowitych.
	"""
	
	if stop is None:
		start = 0
		stop = start_stop
	else:
		start = start_stop
	i = start
	while stop is None or i<stop:
		yield i
		i+=step


