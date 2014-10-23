# -*- coding: utf-8 -*-

import math

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


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    .. note::

        Używamy wzorów NC nie dlatego że są super przydatne (zresztą gorąco
        zniechęcam Państwa przed pisaniem własnych podstawowych algorytmów
        numerycznych --- zbyt łatwo o głupi błąd) ale dlatego żebyście
        jescze raz napisali jakiś algorytm w którym nie opłaca się zrobić 11
        ifów.

    """

    @classmethod
    def get_level_parameters(cls, level):
        """

        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        
        if level < 2 or level > 11:
            raise Exception()
        return {
            2: (0.5, (1, 1)),
            3: (1/3, (1, 4, 1)),
            4: (3/8, (1, 3, 3, 1)),
            5: (2/45, (7, 32, 12, 32, 7)),
            6: (5/288, (19, 75, 50, 50, 75, 19)),
            7: (1/140, (41, 216, 27, 272, 27, 216, 45)),
            8: (7/17280, (751, 3577, 1323, 2989, 2989, 1323, 3577, 751) ),
            9: (4/14175, (989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989)),
            10: (9/89600, (2857, 15741, 1080, 19344, 5778, 5778, 19344, 1080, 15741, 2857)),
            11: (5/299376, (16067, 106300, -48525, 272400, -260550, 427368, -260550, 272400, -48525, 106300, 16067))
        }[level]

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        """
        Funkcja dokonuje całkowania metodą NC.

        :param callable func: Całkowana funkcja, funkcja ta ma jeden argument,
                              i jest wołana w taki sposób: `func(1.0)`.
        :param Tuple[int] func_range: Dwuelementowa krotka zawiera początek i koniec
                                 przedziału całkowania.
        :param int num_evaluations: Przybliżona lość wywołań funkcji ``func``,
            generalnie algorytm jest taki:

            1. Dzielimy zakres na ``num_evaluations/self.level`` przdziałów.
               Jeśli wyrażenie nie dzieli się bez reszty, należy wziąć najmiejszą
               liczbę całkowitą większą od `num_evaluations/self.level``. 
            2. Na każdym uruchamiamy metodę NC stopnia ``self.level``
            3. Wyniki sumujemy.

            W tym algorytmie wykonamy trochę więcej wywołań funkcji niż ``num_evaluations``,
            dokłanie ``num_evaluations`` byłoby wykonywane gdyby keszować wartości
            funkcji na brzegach przedziału całkowania poszczególnych przedziałów.

        :return: Wynik całkowania.
        :rtype: float
        """
        ch, cf = Integrator.get_level_parameters(self.level)
        a, b = func_range
        
        n = (num_evaluations+0.5)//self.level + 1
        x1 = myrange(a, b, n)
        s = 0
        for i in range(n-1):
            xa, xb = x1[i], x1[i+1]
            x2 = myrange(xa, xb, self.level)
            h=x2[1] - x2[0]
            s+=h*ch*sum( cf[j] * fun(x2[j]) for j in range(self.level) )
        return s

if __name__ == '__main__':
    i = Integrator(3)
    print(i.integrate(math.sin, (0, 2*math.pi), 30))
    print(i.integrate(lambda x: x*x, (0, 1), 30))

