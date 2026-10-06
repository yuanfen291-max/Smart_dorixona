import sqlite3

DB_NAME = 'smart_dorixona.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    # Foreign key cheklovlarini yoqish
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Kategoriya (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomi TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Mahsulot (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomi TEXT NOT NULL,
            xalqaro_nomi TEXT,
            kategoriya_id INTEGER,
            shakli TEXT,
            dozasi TEXT,
            retseptli BOOLEAN,
            ishlab_chiqaruvchi TEXT,
            FOREIGN KEY (kategoriya_id) REFERENCES Kategoriya(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Partiya (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mahsulot_id INTEGER,
            seriya_raqami TEXT,
            muddati DATE,
            kelgan_narxi REAL,
            sotish_narxi REAL,
            miqdori INTEGER,
            FOREIGN KEY (mahsulot_id) REFERENCES Mahsulot(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sotuv (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mijoz_id INTEGER,
            foydalanuvchi_id INTEGER,
            sana DATETIME DEFAULT CURRENT_TIMESTAMP,
            jami_summa REAL,
            tolov_turi TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sotuv_Tarkibi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sotuv_id INTEGER,
            partiya_id INTEGER,
            miqdori INTEGER,
            narxi REAL,
            FOREIGN KEY (sotuv_id) REFERENCES Sotuv(id),
            FOREIGN KEY (partiya_id) REFERENCES Partiya(id)
        )
    ''')

    conn.commit()
    conn.close()
