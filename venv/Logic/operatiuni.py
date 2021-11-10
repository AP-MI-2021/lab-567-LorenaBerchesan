import copy

from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin


def ordonare_pret(lista_rezervari, undo_list):
    new_list = copy.deepcopy(lista_rezervari)
    undo_list.append(new_list)
    lista_rezervari.sort(key=get_pret, reverse=True)


def ordonare_descrescator(lista_rezervari):
    '''
    rezervarile ordonate descrescator dupa pret
    :param lista_rezervari:
    :return: rezervarile ordonate descrescator dupa pret
    '''
    lista_rezervari = lista_rezervari[:]
    lista_rezervari.sort(key=lambda rezervare: get_pret(rezervare), reverse=True)
    return lista_rezervari

def avansare(rez):
    if get_clasa(rez) == 'economy':
        rez["clasa"] = 'economy plus'
    elif get_clasa(rez) == 'economy plus':
        rez["clasa"] = 'business'


def ieftinire(rez, procentaj):
    x = get_pret(rez)
    rez["pret"] = x - x * procentaj / 100



def avansare_clasa(lista_rezervari, nm, undo_list):
    ok = False
    new_list = copy.deepcopy(lista_rezervari)
    undo_list.append(new_list)
    for rez in lista_rezervari:
        if get_nume(rez) == nm:
            avansare(rez)
            ok = True
    if not ok:
        print('Nu exista rezervare cu acest nume')


def ieftinire_procentaj(lista_rezervari, procentaj, undo_list):
    ok = False
    new_list = copy.deepcopy(lista_rezervari)
    undo_list.append(new_list)
    for rez in lista_rezervari:
        if get_checkin(rez) == 'da':
            ok = True
            ieftinire(rez, procentaj)


def pret_maxim(lista_prajituri):
    preturi = []
    for rez in lista_prajituri:
        if get_clasa(rez) == 'economy':
            preturi[0] += get_pret(rez)
        elif get_clasa(rez) == 'economy plus':
            preturi[1] += get_pret(rez)
        else:
            preturi[2] += get_pret(rez)
    x = max(preturi[0], preturi[1], preturi[2])
    if preturi[0] == x:
        print('Pretul maxim este: ', x, ' al clasei economy')
    elif preturi[1] == x:
        print('Pretul maxim este: ', x, ' al clasei economy plus')
    else:
        print('Pretul maxim este: ', x, ' al clasei business')


def sume_pe_nume(lista_rezervari):
    lista_nume = []
    lista_preturi = []
    for rez in lista_rezervari:
        if get_nume(rez) not in lista_nume:
            lista_nume.append(get_nume(rez))
            lista_preturi.append(get_pret(rez))
        else:
            pos_nume = lista_nume.index(get_nume(rez))
            lista_preturi[pos_nume] += get_pret(rez)
    i = 0
    while i <= len(lista_nume) - 1:
        print(str(lista_nume[i]) + ' - ' + str(lista_preturi[i]))
        i += 1

def get_rezervari_pret_max_per_clasa(lista_rezervari):
    '''
    Determina rezervarea cu pret maxim din fiecare clasa.
    :param lista_rezervari:
    :return: un dictionar unde cheile sunt clasele si valorile sunt raspunsurile asociate
    '''

    result = {}
    for rezervare in lista_rezervari:
        pret = get_pret(rezervare)
        clasa = get_clasa(rezervare)

        if clasa not in result or pret > get_pret(result[clasa]):
            result[clasa] = rezervare

    return result

