from Domain.rezervare import to_string, get_id


def adauga_rezervare(lista, rezervare):
    lista.append(rezervare)


def afisare_rezervari(lista):
    for rez in lista:
        print(to_string(rez))

def sterge_rezervare(list_rezervari, idd):

    list_rezervari.remove(idd)


def get_by_id(lista_rezervari,id):
    '''
    Gaseste rezervarile dupa id.
    :param rezervari:
    :param id:
    :return: rezervarea sau none daca nu exista
    '''
    for rezervare in lista_rezervari:
        if get_id(rezervare) == id:
            return rezervare
    return None

def update_rezervare(lista_rezervari, rezervare):
    result = [rezervare_existenta for rezervare_existenta in lista_rezervari if get_id(rezervare) != get_id(rezervare_existenta)] + [rezervare]
    return result

def add_rezervare(lista_rezervari, rezervare):
    '''
   :param rezervare: rezervarea de adaugat
   :param lista_rezervari: rezervarile
   :raises: ValueError daca id-ul nu este unic
   '''
    rezervare_existenta=get_by_id(lista_rezervari,id)
    if rezervare_existenta is not None:
        raise ValueError('Id-ul exista deja!')
    lista_rezervari.append(rezervare)


def delete_rezervare(lista_rezervari,id):
    '''
    Sterge o cheltuiala.
    :param cheltuieli:lista de cheltuieli.
    :param id:id-ul cheltuielii care trb sters.
    :return:o noua lista din care va lipsi prajitura cu id-ul id.
    :raises: ValueError, daca id-ul nu exista

    '''
    rezervare_existenta=get_by_id(lista_rezervari,id)
    if rezervare_existenta is None:
        raise ValueError('Id-ul dat nu exista!')
    rezultat=[rezervare for rezervare in lista_rezervari if get_id(rezervare) != id]
    return rezultat