import copy

from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import adauga_rezervare, afisare_rezervari, update_rezervare, get_by_id, sterge_rezervare
from Logic.operatiuni import ordonare_pret, avansare_clasa, ieftinire_procentaj, \
    sume_pe_nume, get_rezervari_pret_max_per_clasa
from UI.console2 import run_console_2


def afiseaza_meniu():
    print('0. Exit')
    print('1. Adauga rezervare')
    print('2. Sterge rezervare')
    print('3. Afiseaza rezervari ')
    print('4. Update')
    print('5. Avansare clasa')
    print('6. Ieftinire')
    print('7. Pret maxim')
    print('8. Ordonare dupa pret')
    print('9. Sume preturi per nume')
    print('10. Undo')
    print('11. Redo')
    print('12. console_2')



def adauga_rezervare_ui(lista, id, nume, clasa, pret, check_in, undo_list, redo_list):
    before_add = lista[:]
    rezervare = creeaza_rezervare(id, nume, clasa, pret, check_in)
    adauga_rezervare(lista, rezervare)
    undo_list.append(before_add)
    redo_list.append(lista)


def afiseaza_rezervari_ui(lista):
    if len(lista) == 0:
        print('Lista de rezervari este goala')
    else:
        afisare_rezervari(lista)


def sterge_rezervare_ui(lista_rezervari, idd):
    ok = False
    i = 0
    while i <= len(lista_rezervari) - 1:
        if get_id(lista_rezervari[i]) == idd:
            sterge_rezervare(lista_rezervari, lista_rezervari[i])
            ok = True
        else:
            i += 1
    if ok == False:
        print('Rezervarea cu acest id nu exista!!')


def ui_handle_rezervari_pret_max_per_clasa(lista_rezervari):
    print(get_rezervari_pret_max_per_clasa(lista_rezervari))


def undo(istoric):
    ultima_lista = []
    if len(istoric) > 0:
        ultima_lista = istoric.pop(-1)
        return ultima_lista
    else:
        raise ValueError('Can not undo anymore')


def modificare(lista_rezervari,undo_list,redo_list):
    try:
        id = int(input('Dati id-ul: '))
        rezervare_existenta = get_by_id(lista_rezervari, id)
        if rezervare_existenta is None:
            raise ValueError('Nici o rezervare cu id-ul dat')

        nume = input('Dati numele (lasati gol pentru a nu se schimba): ')
        if nume == '':
            nume = get_nume(rezervare_existenta)
        else:
            nume = str(nume)

        clasa = input('Dati clasa (lasati gol pentru a nu se schimba): ')
        if clasa == '':
            clasa = get_clasa(rezervare_existenta)
        else:
            clasa = str(clasa)

        pret = input('Dati pret (lasati gol pentru a nu se schimba): ')
        if pret == '':
            pret = get_pret(rezervare_existenta)
        else:
            pret = float(pret)

        checkin = input('Dati checkin-ul (lasati gol pentru a nu se schimba): ')
        if clasa == '':
            checkin = get_checkin(rezervare_existenta)
        else:
            checkin = str(checkin)

        undo_list.append(lista_rezervari)
        rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
        lista_rezervari = update_rezervare(lista_rezervari, rezervare_noua)
        redo_list.append(lista_rezervari)

        print('Rezervarea a fost modificata!')
        return lista_rezervari
    except ValueError as ve:
        print('Eroare:', ve, ',reincearca!')
    return lista_rezervari


def run_undo(undo_list):
    if len(undo_list) > 0:
        return undo_list.pop()

def run_redo(redo_list):
    if len(redo_list) > 0:
        return redo_list.pop()

def undo(lista_rezervari, undo_list):
    undone = run_undo(undo_list)
    if undone is not None:
        lista_rezervari = undone
    return lista_rezervari

def redo(lista_rezervari, redo_list):
    undone = run_redo(redo_list)
    if undone is not None:
        lista_rezervari = undone
    return lista_rezervari


def run_console(lista_rezervari, undo_list, redo_list):
    done = False
    istoric = []
    while not done:
        afiseaza_meniu()
        x = int(input('Da o comanda: '))

        if x == 0:
            done = True
            print('Goodbye!')
        elif x == 1:
            istoric.append(lista_rezervari.copy())
            id_ = int(input('Id rezervare: '))
            for r in lista_rezervari:
                if get_id(r) == id_:
                    raise ValueError('Id deja existent')
            nume = input('Nume rezervare: ')
            clasa = input('Tip clasa: ')
            pret = int(input('Pret: '))
            check_in = input('Check-in: ')
            try:
                adauga_rezervare_ui(lista_rezervari, id_, nume, clasa, pret, check_in, undo_list, redo_list)
            except ValueError as ve:
                print(str(ve))

        elif x == 2:
            istoric.append(lista_rezervari.copy())
            idd = int(input('Id rezervare: '))
            sterge_rezervare_ui(lista_rezervari, idd)

        elif x == 3:
            afiseaza_rezervari_ui(lista_rezervari)

        elif x == 4:
            lista_rezervari = modificare(lista_rezervari,undo_list,redo_list)

        elif x == 5:
            nm = input('Nume: ')
            avansare_clasa(lista_rezervari, nm, undo_list)

        elif x == 6:
            procentaj = float(input('Da procentaj: '))
            ieftinire_procentaj(lista_rezervari, procentaj , undo_list)

        elif x == 7:
            ui_handle_rezervari_pret_max_per_clasa(lista_rezervari)

        elif x == 8:
            ordonare_pret(lista_rezervari, undo_list)

        elif x == 9:
            sume_pe_nume(lista_rezervari)

        elif x == 10:
            if len(undo_list)>0:
                redo_list.append(copy.deepcopy(lista_rezervari))
                lista_rezervari = undo(lista_rezervari, undo_list)

        elif x == 11:
            if len(redo_list) > 0:
                undo_list.append(copy.deepcopy(lista_rezervari))
                lista_rezervari = redo(lista_rezervari, redo_list)

        elif x == 12:
            lista_rezervari = run_console_2(lista_rezervari)

        else:
            print('Optiune invalida, reincearca!')