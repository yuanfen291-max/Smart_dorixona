class Kategoriya:
    def __init__(self, id, nomi):
        self.id = id
        self.nomi = nomi

class Mahsulot:
    def __init__(self, id, nomi, xalqaro_nomi, kategoriya_id, shakli, dozasi, retseptli, ishlab_chiqaruvchi):
        self.id = id
        self.nomi = nomi
        self.xalqaro_nomi = xalqaro_nomi
        self.kategoriya_id = kategoriya_id
        self.shakli = shakli
        self.dozasi = dozasi
        self.retseptli = retseptli
        self.ishlab_chiqaruvchi = ishlab_chiqaruvchi

class Partiya:
    def __init__(self, id, mahsulot_id, seriya_raqami, muddati, kelgan_narxi, sotish_narxi, miqdori):
        self.id = id
        self.mahsulot_id = mahsulot_id
        self.seriya_raqami = seriya_raqami
        self.muddati = muddati
        self.kelgan_narxi = kelgan_narxi
        self.sotish_narxi = sotish_narxi
        self.miqdori = miqdori

class Mijoz:
    def __init__(self, id, ism, telefon, chegirma_foizi=0):
        self.id = id
        self.ism = ism
        self.telefon = telefon
        self.chegirma_foizi = chegirma_foizi

class Foydalanuvchi:
    def __init__(self, id, ism, login, parol, rol):
        self.id = id
        self.ism = ism
        self.login = login
        self.parol = parol
        self.rol = rol  # masalan: Admin, Sotuvchi, Omborchi

class Sotuv:
    def __init__(self, id, mijoz_id, foydalanuvchi_id, sana, jami_summa, tolov_turi):
        self.id = id
        self.mijoz_id = mijoz_id
        self.foydalanuvchi_id = foydalanuvchi_id
        self.sana = sana
        self.jami_summa = jami_summa
        self.tolov_turi = tolov_turi
