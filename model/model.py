from database.corso_dao import CorsoDao


class Model:
    def __init__(self):
        # Soluzione 1: leggo tutti i corsi e poi programmaticamente selezioni i corsi che
        # ti interessano
        self.corsi = CorsoDao.get_all_corsi()

    def get_corsi_periodo(self, pd):
        # Soluzione 1: soluzione con filtro sul periodo fatto da python
        corsi_periodo = []
        for corso in self.corsi:
            if corso.pd == pd:
                corsi_periodo.append(corso)
        return corsi_periodo

        # Soluzione 2: soluzione con filtro sul periodo fatto nella query
        # return CorsoDao.get_corsi_periodo(pd)

    def get_numero_studenti_periodo(self, pd):
        # Soluzione 1: soluzione programmatica (abbiamo aggiunto la relazione
        # matricole nel DTO corso)
        matricole_iscritti = set()
        for corso in self.corsi:
            if corso.pd == pd:
                if corso.matricole is None:
                    corso.matricole = CorsoDao.get_matricole_corso(corso.codins)
                matricole_iscritti = matricole_iscritti.union(corso.matricole)
        return len(matricole_iscritti)

        # Soluzione 2: con join da SQL
        # return CorsoDao.get_numero_studenti_periodo(pd)
