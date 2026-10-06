import sqlite3
import os

DB_NAME = 'smart_dorixona.db'

def generate_receipt(sotuv_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT S.id, S.sana, S.jami_summa, S.tolov_turi, M.nomi, ST.miqdori, ST.narxi
        FROM Sotuv S
        JOIN Sotuv_Tarkibi ST ON S.id = ST.sotuv_id
        JOIN Partiya P ON ST.partiya_id = P.id
        JOIN Mahsulot M ON P.mahsulot_id = M.id
        WHERE S.id = ?
    ''', (sotuv_id,))
    
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return

    # Cheklar uchun papka ochish
    os.makedirs("cheklar", exist_ok=True)
    
    s_id, sana, jami_summa, tolov_turi, mahsulot_nomi, miqdor, narx = rows[0]
    filename = f"cheklar/chek_{s_id}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("===================================\n")
        file.write("        SMART DORIXONA CHEKI       \n")
        file.write("===================================\n")
        file.write(f"Chek №: {s_id}\n")
        file.write(f"Sana: {sana}\n")
        file.write("-----------------------------------\n")
        file.write(f"Mahsulot: {mahsulot_nomi}\n")
        file.write(f"Miqdori: {miqdor} dona\n")
        file.write(f"Narxi: {narx} so'm\n")
        file.write("-----------------------------------\n")
        file.write(f"JAMI: {jami_summa} so'm\n")
        file.write(f"To'lov turi: {tolov_turi}\n")
        file.write("===================================\n")
