import mysql.connector
from database.DB_connect import DBConnect
from model.corso import Corso


class CorsoDao:
    @staticmethod
    # Soluzione 1
    # @staticmethod mi dice che posso eseguire il metodo get_matricole_corso
    # senza avere un'instanza del DAO ma direttamente dalla classe.
    def get_matricole_corso(codins):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return None
        else:
            result = set()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT i.matricola
                        FROM iscrizione i
                        WHERE i.codins = %s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                result.add(row["matricola"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    # Soluzione 1
    # @staticmethod mi dice che posso eseguire il metodo get_all_corsi
    # senza avere un'instanza del DAO ma direttamente dalla classe.
    def get_all_corsi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                        FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                result.append(
                    Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
                )
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    # Soluzione 2
    # @staticmethod mi dice che posso eseguire il metodo get_corsi_periodo
    # senza avere un'instanza del DAO ma direttamente dalla classe.
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                        FROM corso c
                        WHERE c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(
                    Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
                )
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    # Soluzione 2
    # @staticmethod mi dice che posso eseguire il metodo get_numero_studenti_periodo
    # senza avere un'instanza del DAO ma direttamente dalla classe.
    def get_numero_studenti_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor()
            query = """SELECT COUNT(DISTINCT i.matricola)
                        FROM corso c, iscrizione i
                        WHERE c.pd = %s AND c.codins = i.codins"""
            cursor.execute(query, (pd,))
            result = 0
            if cursor.with_rows:
                result = cursor.fetchone()[0]
            cursor.close()
            cnx.close()
            return result
