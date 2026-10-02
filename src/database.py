import sqlite3

def init_db():
    conn = sqlite3.connect('smart_dorixona.db')
    cursor = conn.cursor()

    # 1. Kategoriya jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Kategoriya (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomi TEXT NOT NULL
    )''')

    # 2. Mahsulot jadvali
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
    )''')

    # 3. Partiya (Ombor qoldig'i) jadvali
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
    )''')

    # 4. Mijoz jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mijoz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        telefon TEXT,
        chegirma_foizi REAL DEFAULT 0
    )''')

    # 5. Foydalanuvchi (Xodimlar) jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Foydalanuvchi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        login TEXT UNIQUE NOT NULL,
        parol TEXT NOT NULL,
        rol TEXT NOT NULL
    )''')

    # 6. Sotuv jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sotuv (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mijoz_id INTEGER,
        foydalanuvchi_id INTEGER,
        sana DATETIME DEFAULT CURRENT_TIMESTAMP,
        jami_summa REAL,
        tolov_turi TEXT,
        FOREIGN KEY (mijoz_id) REFERENCES Mijoz(id),
        FOREIGN KEY (foydalanuvchi_id) REFERENCES Foydalanuvchi(id)
    )''')

    # 7. Sotuv tarkibi jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sotuv_Tarkibi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sotuv_id INTEGER,
        partiya_id INTEGER,
        miqdori INTEGER,
        narxi REAL,
        FOREIGN KEY (sotuv_id) REFERENCES Sotuv(id),
        FOREIGN KEY (partiya_id) REFERENCES Partiya(id)
    )''')

    conn.commit()
    conn.close()
    print("Ma'lumotlar bazasi va jadvallar muvaffaqiyatli yaratildi!")

if __name__ == "__main__":
    init_db()
