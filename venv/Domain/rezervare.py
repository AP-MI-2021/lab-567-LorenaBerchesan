def creeaza_rezervare(id, nume, clasa, pret, checkin):
    """


    :param id: string, id-ul rezervarii, trebuie sa fie unic
    :param nume: string, numele rezervarii
    :param clasa: string, clasa rezervarii
    :param pret: float, pretul rezervarii
    :param checkin: int, checkin-ul rezervarii
    :return: un obiect rezervare
    """
    tip_clasa = ['economy', 'economy plus', 'business']
    if id < 0:
        raise ValueError('Id-ul trebuie sa fie pozitiv')
    if clasa not in tip_clasa:
        raise ValueError('Clasa nu este valida')
    if pret < 0:
        raise ValueError('Pretul trebuie sa fie pozitiv')
    if not (checkin == 'da' or checkin == 'nu'):
        raise ValueError('Checkin incorect')
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin,
    }
    #return [id,nume,clasa,pret,checkin]


def get_id(rezervare):
    """
    Id ul rezervarii

    :param rezervare:
    :return: id ul rezervarii
    """
    return rezervare["id"]
    #return rezervare[1]


def get_nume(rezervare):
    """
    Numele rezervarii

    :param rezervare:
    :return: numele rezervarii
    """
    return rezervare["nume"]
    #return rezervare[2]


def get_clasa(rezervare):
    """
    Descrierea rezervarii

    :param rezervare:
    :return: clasa rezervarii
    """
    return rezervare["clasa"]
    #return rezervare[3]


def get_pret(rezervare):
    """
    Pretul rezervarii

    :param rezervare:
    :return: pretul rezervarii
    """
    return rezervare["pret"]
    #return rezervare[4]


def get_checkin(rezervare):
    """
    Checkin rezervarii

    :param rezervare:
    :return: checkin-ul rezervarii
    """
    return rezervare["checkin"]
    #return rezervare[5]


def to_string(rezervare):
    """
    Creaza un string cu proprietatiile rezervarii

    :param rezervare:
    :return: un string format cu prop. rezervarii
    """
    return "id: {}, nume: {}, descriere: {}, pret: {}, check-in: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )

