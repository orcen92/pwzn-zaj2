from math import sin, pi, exp

def myrange(x0, xn, n):
	if n==1:
		return x0
	if n <= 0:
		raise Exception("bledna liczba elementow")
	
	krok = (xn - x0)/(n-1)
	l = []
	for i in range(n):
		l.append(x0+krok*i)
	return l


class Integrator:
	
	def __init__(self, fun, a, b, n):
		self.fun = fun
		self.a = a
		self.b = b
		self.n = n
	
class RectangleIntegrator(Integrator):
	
	def integrate(self):
		x = myrange(self.a, self.b, self.n)
		s = 0
		krok = x[1]-x[0]
		for i in x:
			s+= self.fun(i)
		return s*krok


class TrapesoidIntegrator(Integrator):

	def integrate(self):	
		x = myrange(self.a, self.b, self.n)
		s = 0
		krok = x[1]-x[0]
		for xi in x[:-1]: #do -1 bo trapezow jest o jeden mniej, niz punktow
			s+= (self.fun(xi) + self.fun(xi+krok))
		return s*krok/2
		

class SimpsonIntegrator(Integrator):

	def __init__(self, *args):
		super().__init__(*args)
		self.n = self.n if self.n%2==1 else self.n+1
	
	def integrate(self):
		fun=self.fun
		x = myrange(self.a, self.b, self.n)
		k = self.n//2
		s = fun(self.a) + fun(self.b) + 4*fun(x[2*k-1])
		for i in range(1,k): # od 1 to k-1
			s+= 4*fun(x[2*i-1]) + 2*fun(x[2*i])
		return s*(x[1]-x[0])/3


class NewtonCotes:
	def __init__(self, fun, a, b):
		self.a = a
		self.b = b
		self.fun = fun
		self.c = [ ( 1/3, (1, 4, 1)), #order=3
					  ( 3/8, (1, 3, 3, 1)),
					  ( 2/45, (7, 32, 12, 32, 7)),
					  ( 5/288, (19, 75, 50, 50, 75, 19)) ]
	
	def integrate(self, order=3):
		if order<3 or order>6:
			raise Exception('wrong order (must be between 3 and 6)')
		ch, cf = self.c[order-3]
		x = myrange(self.a, self.b, order)
		s=0
		for i in range(order):
			s+=self.fun(x[i])*cf[i]
		return ch*(x[1]-x[0])*s

exact = exp(1) - exp(0)
print('exact', exact)


rect = RectangleIntegrator(exp, 0, 1, 20).integrate()
trap = TrapesoidIntegrator(exp, 0, 1, 20).integrate()
simp = SimpsonIntegrator  (exp, 0, 1, 20).integrate()
newt = NewtonCotes(exp, 0, 1).integrate(6)
print('rect', rect, '({})'.format(rect-exact))
print('trap', trap, '({})'.format(trap-exact))
print('simp', simp, '({})'.format(simp-exact))
print('newt', newt, '({})'.format(newt-exact))
print()

