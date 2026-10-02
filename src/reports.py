import sqlite3
from datetime import datetime

DB_NAME = 'smart_dorixona.db'

def generate_receipt(sotuv_id):
    """Генерация и сохранение текстового чека"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Получаем данные о продаже
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
        print("Продажа не найдена!")
        return

    s_id, sana, jami_summa, tolov_turi, mahsulot_nomi, miqdor, narx = rows[0]

    filename = f"chek_{s_id}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("===================================\n")
        file.write("        SMART DORIXONA CHEKI       \n")
        file.write("===================================\n")
        file.write(f"Чек №: {s_id}\n")
        file.write(f"Дата: {sana}\n")
        file.write("-----------------------------------\n")
        file.write(f"Товар: {mahsulot_nomi}\n")
        file.write(f"Количество: {miqdor} шт.\n")
        file.write(f"Цена за шт: {narx} сум\n")
        file.write("-----------------------------------\n")
        file.write(f"ИТОГО К ОПЛАТЕ: {jami_summa} сум\n")
        file.write(f"Тип оплаты: {tolov_turi}\n")
        file.write("===================================\n")
        file.write("    Спасибо за покупку! Будьте здоровы!\n")

    print(f"Чек успешно сохранен в файл: {filename}")

def get_daily_report():
    """Отчёт по продажам за текущий день"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(id), SUM(jami_summa)
        FROM Sotuv
        WHERE DATE(sana) = DATE('now')
    ''')
    
    result = cursor.fetchone()
    conn.close()

    total_sales = result[0] or 0
    total_revenue = result[1] or 0.0

    print("\n" + "="*35)
    print("      ОТЧЁТ ПО ПРОДАЖАМ ЗА СЕГОДНЯ    ")
    print("="*35)
    print(f"Всего совершенных продаж: {total_sales}")
    print(f"Общая выручка: {total_revenue} сум")
    print("="*35)
