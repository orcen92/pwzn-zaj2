# -*- coding: utf-8 -*-

import pickle
import pathlib


def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    
    
    def weight(value, unit):
        '''
        zwraca mase w kg
        '''
        if unit=='g':
            return value*1e-3
        elif unit=='Mg':
            return value*1e3
        elif unit=='mg':
            return value*1e-6
        else:
            return value
    
    genres = sorted(set(x['genus'] for x in animal_list))

#    animals = {genre:None for genre in genres }    
#    males=dict()
#    females=dict()
    animals={'male': dict(), 'female': dict()}
    # stworz slownik z pierwszym wystapieniem kazdego gatunku
    for animal in animal_list:
        for sex in ('male', 'female'):
            if len(animals[sex].keys()) < len(genres) and animal['sex'] == sex:
                animals[sex][animal['genus']] = animal
        if len(animals['female'].keys()) >= len(genres) and len(animals['female'].keys()) >= len(genres):
            break
    
#    print (sorted(set(animals['male'])))
 #   print (sorted(set(animals['female'])))
    
    for animal in animal_list:
        sex = animal['sex']
        genre = animal['genus']
        mass = weight(*animal['mass'])
        if mass < weight(*animals[sex][genre]['mass']):
            animals[sex][genre] = animal
#    print (animals)
    
    l=[]
    for genre in sorted(genres):
        z = sorted( [animals['male'][genre], animals['female'][genre] ] , key=lambda x: x['name'] )
        l.append(z[0])
        l.append(z[1])
    return l
    
if __name__ == "__main__":
    animals = load_animals()
#    print (animals[0])
    filter_animals(animals)

