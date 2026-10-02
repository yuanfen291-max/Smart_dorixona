from database import init_db
import crud

def main_menu():
    init_db()

    while True:
        print("\n" + "="*45)
        print("   SMART DORIXONA - TIZIMGA HUSH KELIBSIZ")
        print("="*45)
        print("1. Ombor qoldig'ini ko'rish (Остатки на складе)")
        print("2. Yangi kategoriya qo'shish (Добавить категорию)")
        print("3. Yangi dori qo'shish (Добавить лекарство)")
        print("4. Omborga dori qabul qilish (Приход на склад)")
        print("5. Sotuvni amalga oshirish (Продажа)")
        print("0. Chiqish (Выход)")
        print("="*45)

        choice = input("Tanlang (0-5): ")

        if choice == '1':
            print("\n--- OMBOR QOLDIG'I ---")
            items = crud.check_stock()
            if not items:
                print("Ombor bo'sh!")
            else:
                for item in items:
                    print(f"ID: {item[0]} | Nomi: {item[1]} | Seriya: {item[2]} | Muddati: {item[3]} | Narxi: {item[4]} | Miqdori: {item[5]}")

        elif choice == '2':
            nomi = input("Kategoriya nomini kiriting: ")
            crud.add_kategoriya(nomi)

        elif choice == '3':
            nomi = input("Dori nomi: ")
            xalqaro = input("Xalqaro nomi: ")
            kat_id = int(input("Kategoriya ID: "))
            shakli = input("Formasi (таблетки/сироп): ")
            dozasi = input("Dozasi (500mg): ")
            retsept = input("Retseptli (1-ha, 0-yo'q): ") == '1'
            ishlab = input("Ishlab chiqaruvchi: ")
            crud.add_mahsulot(nomi, xalqaro, kat_id, shakli, dozasi, retsept, ishlab)

        elif choice == '4':
            m_id = int(input("Mahsulot ID: "))
            seriya = input("Seriya raqami: ")
            muddati = input("Muddati (YYYY-MM-DD): ")
            kel_narx = float(input("Kelish narxi: "))
            sot_narx = float(input("Sotish narxi: "))
            miqdor = int(input("Miqdori: "))
            crud.add_partiya(m_id, seriya, muddati, kel_narx, sot_narx, miqdor)

        elif choice == '5':
            p_id = int(input("Partiya ID: "))
            miqdor = int(input("Sotiladigan miqdor: "))
            crud.make_sale(p_id, miqdor)

        elif choice == '0':
            print("Xayr!")
            break

if __name__ == "__main__":
    main_menu()
