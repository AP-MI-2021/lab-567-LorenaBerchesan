from Domain.rezervare import creeaza_rezervare, get_nume, get_id, get_pret, get_clasa, get_checkin


def test_rezervare_domain():
    rezervare1 = creeaza_rezervare(1, "Mihai", "business", 250, "da")
    assert get_id(rezervare1)==1
    assert get_nume(rezervare1)=="Mihai"
    assert get_clasa(rezervare1)=="business"
    assert get_pret(rezervare1)==250
    assert  get_checkin(rezervare1)=="da"