def get_obj(id:int, nume:str, clasa:str, pret:int, checkin:int):
    return[id, nume, clasa, pret, checkin]

def get_id(obiect):
    return obiect[0]

def get_nume(obiect):
    return obiect[1]

def get_clasa(obiect):
    return obiect[2]

def get_pret(obiect):
    return obiect[3]

def get_checkin(obiect):
    return obiect[4]

def get_obj_string(obiect):
    return f"Obiectul cu id{get_id(obiect)}, cu numele {get_nume(obiect)}"\
        f"de clasa {get_clasa(obiect)}, cu pretul {get_pret(obiect)}, avand checkin-ul {get_checkin(obiect)}"