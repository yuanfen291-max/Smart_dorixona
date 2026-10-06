import sqlite3
from datetime import datetime

DB_NAME = 'smart_dorixona.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def make_sale(partiya_id, miqdori, mijoz_id=None, foydalanuvchi_id=1, tolov_turi="Naqd"):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Partiya va dori muddatini tekshirish
        cursor.execute("SELECT miqdori, sotish_narxi, muddati FROM Partiya WHERE id = ?", (partiya_id,))
        partiya = cursor.fetchone()

        if not partiya:
            print("Xato: Partiya topilmadi!")
            return False

        ombor_miqdori, sotish_narxi, muddati = partiya

        # Yaroqlilik muddatini tekshirish
        bugun = datetime.now().strftime('%Y-%m-%d')
        if muddati and muddati < bugun:
            print("Xato: Ushbu dori vositasining yaroqlilik muddati o'tgan!")
            return False

        if ombor_miqdori < miqdori:
            print(f"Xato: Omborda mahsulot yetarli emas! Mavjud: {ombor_miqdori}")
            return False

        jami_summa = sotish_narxi * miqdori

        # 1. Sotuv jadvaliga yozish
        cursor.execute('''
            INSERT INTO Sotuv (mijoz_id, foydalanuvchi_id, jami_summa, tolov_turi)
            VALUES (?, ?, ?, ?)
        ''', (mijoz_id, foydalanuvchi_id, jami_summa, tolov_turi))
        sotuv_id = cursor.lastrowid

        # 2. Sotuv tarkibiga yozish
        cursor.execute('''
            INSERT INTO Sotuv_Tarkibi (sotuv_id, partiya_id, miqdori, narxi)
            VALUES (?, ?, ?, ?)
        ''', (sotuv_id, partiya_id, miqdori, sotish_narxi))

        # 3. Ombordan kamaytirish
        cursor.execute("UPDATE Partiya SET miqdori = miqdori - ? WHERE id = ?", (miqdori, partiya_id))

        conn.commit()
        print(f"Sotuv muvaffaqiyatli bajarildi! Chek №{sotuv_id}")
        return sotuv_id

    except Exception as e:
        conn.rollback()  # Xatolik bo'lsa barcha amallarni bekor qilish
        print(f"Tranzaksiyada xatolik yuz berdi: {e}")
        return False
    finally:
        conn.close()

def check_stock():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT P.id, M.nomi, P.seriya_raqami, P.muddati, P.sotish_narxi, P.miqdori
        FROM Partiya P
        JOIN Mahsulot M ON P.mahsulot_id = M.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows
