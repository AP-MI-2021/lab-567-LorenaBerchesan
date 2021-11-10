from Tests.test_crud import test_get_by_id, test_delete_rezervare, test_add_rezervare
from Tests.test_operatiuni import test_avansare_clasa, test_ordonare_descrescator, \
    test_get_rezervari_pret_max_per_clasa
from Tests.test_rezervare import test_rezervare_domain

def run_all():
    test_rezervare_domain()
    test_add_rezervare()
    test_delete_rezervare()
    test_get_by_id()
    test_ordonare_descrescator()