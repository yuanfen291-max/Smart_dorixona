import sqlite3
from database import init_db

def asosiy_menyu():
    # Dastur boshlanishida bazani tekshiramiz/yaratamiz
    init_db()

    while True:
        print("\n" + "="*40)
        print("   SMART DORIXONA - TIZIMGA HUSH KELIBSIZ")
        print("="*40)
        print("1. Mahsulotlar ro'yxatini ko'rish")
        print("2. Yangi mahsulot qo'shish")
        print("3. Sotuvni amalga oshirish")
        print("4. Ombor qoldig'ini ko'rish")
        print("0. Tizimdan chiqish")
        print("="*40)
        
        tanlov = input("Tanlovingizni kiriting (0-4): ")

        if tanlov == '1':
            print("\n[Mahsulotlar ro'yxati menyusi selected]")
            # Mahsulotlarni ko'rsatish funksiyasi
        elif tanlov == '2':
            print("\n[Yangi mahsulot qo'shish menyusi selected]")
            # Mahsulot qo'shish funksiyasi
        elif tanlov == '3':
            print("\n[Sotuv oynasi selected]")
            # Sotuv funksiyasi
        elif tanlov == '4':
            print("\n[Ombor qoldig'i selected]")
            # Ombor funksiyasi
        elif tanlov == '0':
            print("\nE'tiboringiz uchun rahmat! Tizim ishini yakunladi.")
            break
        else:
            print("\nNoto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    asosiy_menyu()
