from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin, creeaza_rezervare
from Logic.crud import adauga_rezervare, sterge_rezervare, get_by_id, add_rezervare, delete_rezervare
from UI.console import modificare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare(1, "Mihai", "business", 250, "da", lista)
    assert get_id(lista[0]) == 1
    assert get_nume(lista[0]) == "Mihai"
    assert get_clasa(lista[0]) == "business"
    assert get_pret(lista[0]) == 250
    assert get_checkin(lista[0]) == "da"


def test_sterge_obiect():
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 234, "da")
    rezervare2 = creeaza_rezervare(2, "Alex", "economy", 78, "nu")

    lista=[rezervare1,rezervare2]
    lista=sterge_rezervare(1,lista)

    assert len(lista)==1
    assert get_by_id(lista,2) == rezervare2
    assert get_by_id(lista,1)== None


def test_get_by_id():
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 234, "da")
    rezervare2 = creeaza_rezervare(2, "Alex", "economy", 78, "nu")

    lista = [rezervare1, rezervare2]

    assert get_by_id(lista,1)==rezervare1


def test_add_rezervare():
    lista_rezervari = []
    rezervare1 = creeaza_rezervare(1, "Mihai", "economy plus", 234, "da")
    add_rezervare(lista_rezervari, rezervare1)
    assert len(lista_rezervari) == 1
    assert get_by_id(lista_rezervari, 1) == rezervare1

    rezervare2 = creeaza_rezervare(2, "Alex", "economy", 78, "nu")
    add_rezervare(lista_rezervari, rezervare2)
    assert len(lista_rezervari) == 2
    assert get_by_id(lista_rezervari, 1) == rezervare1
    assert get_by_id(lista_rezervari, 2) == rezervare2

def test_delete_rezervare():
    lista_rezervari = []
    add_rezervare(lista_rezervari, creeaza_rezervare(1, "Mihai", "economy plus", 234, "da"))
    add_rezervare(lista_rezervari, creeaza_rezervare(2, "Alex", "economy", 78, "nu"))

    lista_rezervari = delete_rezervare(lista_rezervari, 1)
    assert get_id(get_by_id(lista_rezervari, 2)) == 2
    assert get_by_id(lista_rezervari, 1) is None

    try:
        lista_rezervari = delete_rezervare(lista_rezervari, 50)
        assert False
    except Exception:
        pass