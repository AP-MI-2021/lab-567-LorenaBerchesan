from Domain.rezervare import creeaza_rezervare, get_pret, get_clasa, get_nume, get_id
from Logic.crud import add_rezervare
from Logic.operatiuni import avansare_clasa, ordonare_pret, ordonare_descrescator, get_rezervari_pret_max_per_clasa
from UI.console import ui_handle_rezervari_pret_max_per_clasa


def test_get_by_id():
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 150, "da")
    rezervare2 = creeaza_rezervare(2, "Razvi", "economy", 50, "nu")


    lista = [rezervare1, rezervare2]

    assert get_id(lista)== rezervare1

def test_avansare_clasa():
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 150, "da")
    rezervare2 = creeaza_rezervare(2, "Razvi", "economy", 50, "nu")
    rezervare3= creeaza_rezervare(1, "Mihai", "business", 150, "da")


    lista = [rezervare1,rezervare2]
    undo_list = [rezervare1,rezervare2]
    assert avansare_clasa(lista,"Mihai",undo_list) == [rezervare3,rezervare2]


def test_ordonare_descrescator():
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 150, "da")
    rezervare2 = creeaza_rezervare(2, "Razvi", "economy", 50, "nu")
    rezervare3 = creeaza_rezervare(1, "Mihai", "business", 15, "da")
    lista = [rezervare1,rezervare2,rezervare3]
    assert ordonare_descrescator(lista)==[rezervare1,rezervare2,rezervare3]

def test_get_rezervari_pret_max_per_clasa():
    rezervare1 = creeaza_rezervare(1, "Cris", "business", 145, "da")
    rezervare2 = creeaza_rezervare(2, "Andy", "business", 150, "da")
    lista_rezervari = [rezervare1,rezervare2]
    assert get_rezervari_pret_max_per_clasa(lista_rezervari) == [rezervare2]
