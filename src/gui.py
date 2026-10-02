import tkinter as tk
from tkinter import ttk, messagebox
import crud

class SmartDorixonaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Dorixona - Boshqaruv Tizimi")
        self.root.geometry("800x500")

        # Tab (Vkladka)lar yaratish
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # 1. Ombor qoldig'i oynasi
        self.ombor_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.ombor_frame, text="Ombor qoldig'i")
        self.setup_ombor_tab()

        # 2. Sotuv oynasi
        self.sotuv_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.sotuv_frame, text="Sotuv (Kassa)")
        self.setup_sotuv_tab()

    def setup_ombor_tab(self):
        # Ombor jadvali
        columns = ("id", "nomi", "seriya", "muddati", "narxi", "miqdori")
        self.tree = ttk.Treeview(self.ombor_frame, columns=columns, show='headings')
        
        self.tree.heading("id", text="ID")
        self.tree.heading("nomi", text="Dori nomi")
        self.tree.heading("seriya", text="Seriya")
        self.tree.heading("muddati", text="Muddati")
        self.tree.heading("narxi", text="Sotish narxi")
        self.tree.heading("miqdori", text="Ombor miqdori")

        self.tree.column("id", width=40)
        self.tree.column("nomi", width=180)
        self.tree.column("seriya", width=100)
        self.tree.column("muddati", width=100)
        self.tree.column("narxi", width=100)
        self.tree.column("miqdori", width=100)

        self.tree.pack(fill='both', expand=True, pady=10)

        # Yangilash tugmasi
        btn_refresh = ttk.Button(self.ombor_frame, text="Ro'yxatni yangilash", command=self.load_stock)
        btn_refresh.pack(pady=5)

        self.load_stock()

    def load_stock(self):
        # Jadvalni tozalash
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ma'lumotlarni bazadan yuklash
        items = crud.check_stock()
        for row in items:
            self.tree.insert('', 'end', values=row)

    def setup_sotuv_tab(self):
        # Sotuv formasi
        frame_form = ttk.LabelFrame(self.sotuv_frame, text="Sotuvni rasmiylashtirish")
        frame_form.pack(fill='x', padx=10, pady=10)

        ttk.Label(frame_form, text="Partiya ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_partiya = ttk.Entry(frame_form)
        self.entry_partiya.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Miqdori:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_miqdor = ttk.Entry(frame_form)
        self.entry_miqdor.grid(row=1, column=1, padx=5, pady=5)

        btn_sotish = ttk.Button(frame_form, text="Sotishni amalga oshirish", command=self.sotish_bajar)
        btn_sotish.grid(row=2, column=0, columnspan=2, pady=10)

    def sotish_bajar(self):
        try:
            partiya_id = int(self.entry_partiya.get())
            miqdor = int(self.entry_miqdor.get())
            
            crud.make_sale(partiya_id, miqdor)
            messagebox.showinfo("Muvaffaqiyatli", "Sotuv amalga oshirildi!")
            
            self.entry_partiya.delete(0, tk.END)
            self.entry_miqdor.delete(0, tk.END)
            self.load_stock()
        except Exception as e:
            messagebox.showerror("Xatolik", f"Sotuvda xatolik yuz berdi: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartDorixonaGUI(root)
    root.mainloop()
