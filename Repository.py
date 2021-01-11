import sqlite3
import atexit
import DAOS


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = _Vaccines(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.clinics = _Clinics(self._conn)
        self.logistics = _Logistics(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        _conn.executescript("""
        CREATE TABLE logistics (
            id               INT        PRIMARY KEY,
            name             TEXT       NOT NULL,
            count_sent       INT        NOT NULL,
            count_received   INT        NOT NULL,
        );
        CREATE TABLE clinics (
            id               INT        PRIMARY KEY,
            location         TEXT       NOT NULL,
            demand           INT        NOT NULL,

            FOREIGN KEY(logistic_id)    REFERENCES logistics(id),
        );
        CREATE TABLE suppliers (
            id               INT        PRIMARY KEY,
            name             TEXT       NOT NULL,
            FOREIGN KEY(logistic_id)    REFERENCES logistics(id),
        );
        
        
        CREATE TABLE vaccines(
        id                   INT        PRIMARY KEY,
        date                 DATE       NOT NULL,
        FOREIGN KEY(supplier_id)        REFERENCES suppliers(id),
        quantity             INT        NOT NULL,
        );
    """)


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
