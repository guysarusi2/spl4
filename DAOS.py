from DTOS import *


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""
                       INSERT INTO vaccines (id, name,supplier, quantity) VALUES (?,?,?,?)
                   """, [vaccine.id, vaccine.name, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, supplier, quantity FROM vaccines WHERE id = ?
        """, [vaccine_id])
        return Vaccine(*c.fetchone())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                  INSERT INTO suppliers (id, name,logistic) VALUES (?,?,?)
                 """, [supplier.id, supplier.name, supplier.logistic])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, logistic FROM suppliers WHERE id = ?
        """, [supplier_id])
        return Supplier(*c.fetchone())


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
                   INSERT INTO clinics (id, location,demand,logistic) VALUES (?,?,?,?)
                """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT id, location,demand, logistic FROM clinics WHERE id = ?
                """, [clinic_id])
        return Clinic(*c.fetchone())


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
                    INSERT INTO logistics (id, name,count_sent,count_received) VALUES (?,?,?,?)
                 """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, logistic_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT id, name,count_sent, count_received FROM logistics WHERE id = ?
                """, [logistic_id])
        return Logistic(*c.fetchone())
