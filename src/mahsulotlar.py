import sqlite3
from database import connect_db

def mahsulot_qoshish(nomi, narxi, miqdori):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Mahsulot (nomi) VALUES (?)", (nomi,))
    m_id = cursor.lastrowid
    
    cursor.execute('''
        INSERT INTO Partiya (mahsulot_id, sotish_narxi, miqdori)
        VALUES (?, ?, ?)
    ''', (m_id, narxi, miqdori))
    
    conn.commit()
    conn.close()
    print(f"'{nomi}' bazaga muvaffaqiyatli qo'shildi.")

def qoldiq_tekshir(nomi):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT M.nomi, SUM(P.miqdori) 
        FROM Mahsulot M 
        JOIN Partiya P ON M.id = P.mahsulot_id 
        WHERE LOWER(M.nomi) = LOWER(?)
    ''', (nomi,))
    row = cursor.fetchone()
    conn.close()
    
    if row and row[0]:
        print(f"{row[0]} qoldig'i: {row[1]} dona")
    else:
        print("Mahsulot topilmadi.")
