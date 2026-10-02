import sqlite3

DB_NAME = 'smart_dorixona.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

# --- 1. КАТЕГОРИИ И ТОВАРЫ ---

def add_kategoriya(nomi):
    """Новая категория"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Kategoriya (nomi) VALUES (?)", (nomi,))
    conn.commit()
    conn.close()
    print(f"Категория '{nomi}' успешно добавлена!")

def add_mahsulot(nomi, xalqaro_nomi, kategoriya_id, shakli, dozasi, retseptli, ishlab_chiqaruvchi):
    """Новое лекарственное средство"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Mahsulot (nomi, xalqaro_nomi, kategoriya_id, shakli, dozasi, retseptli, ishlab_chiqaruvchi)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nomi, xalqaro_nomi, kategoriya_id, shakli, dozasi, retseptli, ishlab_chiqaruvchi))
    conn.commit()
    conn.close()
    print(f"Товар '{nomi}' успешно добавлен!")

# --- 2. ПРИЁМ ТОВАРА НА СКЛАД (PARTIYA) ---

def add_partiya(mahsulot_id, seriya_raqami, muddati, kelgan_narxi, sotish_narxi, miqdori):
    """Приход партии товара на склад"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Partiya (mahsulot_id, seriya_raqami, muddati, kelgan_narxi, sotish_narxi, miqdori)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (mahsulot_id, seriya_raqami, muddati, kelgan_narxi, sotish_narxi, miqdori))
    conn.commit()
    conn.close()
    print("Партия товара успешно принята на склад!")

# --- 3. ПРОДАЖА (SOTUV) ---

def make_sale(partiya_id, miqdori, mijoz_id=None, foydalanuvchi_id=1, tolov_turi="Naqd"):
    """Проведение продажи товара"""
    conn = connect_db()
    cursor = conn.cursor()

    # Проверяем остаток на складе
    cursor.execute("SELECT miqdori, sotish_narxi FROM Partiya WHERE id = ?", (partiya_id,))
    partiya = cursor.fetchone()

    if not partiya:
        print("Ошибка: Партия не найдена!")
        conn.close()
        return

    ombor_miqdori, sotish_narxi = partiya

    if ombor_miqdori < miqdori:
        print(f"Ошибка: Недостаточно товара на складе! В наличии: {ombor_miqdori}")
        conn.close()
        return

    jami_summa = sotish_narxi * miqdori

    # 1. Создаем запись о продаже
    cursor.execute('''
        INSERT INTO Sotuv (mijoz_id, foydalanuvchi_id, jami_summa, tolov_turi)
        VALUES (?, ?, ?, ?)
    ''', (mijoz_id, foydalanuvchi_id, jami_summa, tolov_turi))
    sotuv_id = cursor.lastrowid

    # 2. Записываем состав продажи
    cursor.execute('''
        INSERT INTO Sotuv_Tarkibi (sotuv_id, partiya_id, miqdori, narxi)
        VALUES (?, ?, ?, ?)
    ''', (sotuv_id, partiya_id, miqdori, sotish_narxi))

    # 3. Списываем количество со склада
    yangi_miqdor = ombor_miqdori - miqdori
    cursor.execute("UPDATE Partiya SET miqdori = ? WHERE id = ?", (yangi_miqdor, partiya_id))

    conn.commit()
    conn.close()
    print(f"Продажа успешно совершена! Чек №{sotuv_id}, Сумма: {jami_summa} сум.")

# --- 4. ОТЧЕТЫ И ОСТАТКИ ---

def check_stock():
    """Просмотр остатков на складе"""
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
