from Domain.rezervare import creeaza_rezervare
from Tests.run_all_tests import run_all
from UI.console import run_console

run_all()
def main():
    lista_rezervari = []
    lista_rezervari.append(creeaza_rezervare(1, 'Alexandra', 'economy plus', 300, 'da'))
    lista_rezervari.append(creeaza_rezervare(2, 'Mihai', 'economy plus', 280, 'da'))
    lista_rezervari.append(creeaza_rezervare(3, 'Ionut', 'business', 450, 'nu'))
    lista_rezervari.append(creeaza_rezervare(4, 'Alex', 'economy', 150, 'da'))
    lista_rezervari.append(creeaza_rezervare(5, 'Maria', 'economy', 98, 'nu'))
    lista_rezervari.append(creeaza_rezervare(6, 'Simina', 'economy plus', 234, 'nu'))
    lista_rezervari.append(creeaza_rezervare(7, 'Paul', 'economy plus', 238, 'nu'))
    lista_rezervari.append(creeaza_rezervare(8, 'Cristina', 'business', 502, 'da'))
    lista_rezervari.append(creeaza_rezervare(9, 'Alexandra', 'economy plus', 268, 'da'))

    lista_rezervari = run_console(lista_rezervari)

main()