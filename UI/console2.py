from Domain.rezervare import to_string,creeaza_rezervare
from Logic.crud import add_rezervare, delete_rezervare
from Logic.operatiuni import ordonare_descrescator, ordonare_pret, get_rezervari_pret_max_per_clasa

def print_meniu():
    print('Citeste stringul cu operatiuni separate prin virgula')
    print('Adaugare,<id>,<nume>,<clasa>,<pret>,<checkin>')
    print('Stergere,<id> - este pentru stergere')
    print('Showall - pentru afisare')
    print('Ordonare - ordonare descarescator dupa pret')
    print('OrdonarePret - pret')
    print('Rezervare - rezervare pret maxim per clasa')


def run_console_2(lista_rezervari):
    def handle_show_all(revervari_to_show):
        for rezervare in revervari_to_show:
            print(to_string(rezervare))
        if len(revervari_to_show) == 0:
            print('Lista este goala!')

    while True:
        print_meniu()
        str = input('Dati stringul:')
        new_str = str.split(';')
        for r in new_str:
            comanda = r.split(',')
            if comanda[0] == 'Adaugare':
                try:
                    id = int(comanda[1])
                    nume = comanda[2]
                    clasa = comanda[3]
                    pret = int(comanda[4])
                    checkin = comanda[5]

                    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
                    add_rezervare(lista_rezervari, rezervare)

                    print('Rezervarea a fost adaugata')
                except Exception as ve:
                    print('Eroare:', ve, ',reincearca!')


            elif comanda[0] == 'Stergere':
                try:
                    id = int(comanda[1])
                    lista_rezervari = delete_rezervare(lista_rezervari, id)
                    print('Rezervarea a fost stearsa!')
                except ValueError as ve:
                    print('Eroare:', ve, ', reincearca!')
            elif comanda[0] == 'Showall':
                handle_show_all(lista_rezervari)
            elif comanda[0] == 'Ordonare':
                for rezervare in ordonare_descrescator(lista_rezervari):
                    print(to_string(rezervare))
            elif comanda[0] == 'OdonarePret':
                for rezervare in ordonare_pret(lista_rezervari):
                    print(to_string(rezervare))
            elif comanda[0] =='Rezervare':
                for rezervare in get_rezervari_pret_max_per_clasa(lista_rezervari):
                    print(to_string(rezervare))
            elif comanda[0] == 'Back':
                break
