import unittest
from tarifKeretaApi import tarif_keretaapi

class Testing(unittest.TestCase):

    def test_kelas1(self):
        self.assertEqual(tarif_keretaapi(99, 1), 100_000, "kesalahan kereta api 1")
        self.assertEqual(tarif_keretaapi(100, 1), 100_000, "mamah, aku takut! 1")
        self.assertEqual(tarif_keretaapi(104, 1), 140_000, "mamah, aku takut! 1")
        self.assertEqual(tarif_keretaapi(4531, 1), 44410000, "mamah, aku takut! 1")
        
    def test_kelas2(self):
        self.assertEqual(tarif_keretaapi(99, 2), 150000, "mamah, aku takut! 2")
        self.assertEqual(tarif_keretaapi(100, 2), 150000, "mamah, aku takut! 2")
        self.assertEqual(tarif_keretaapi(104, 2), 210000, "mamah, aku takut! 2")
        self.assertEqual(tarif_keretaapi(4531, 2), 66615000, "mamah, aku takut! 2")
        
    def test_kelas3(self):
        self.assertEqual(tarif_keretaapi(99, 3), 200000, "mamah, aku takut! 3")
        self.assertEqual(tarif_keretaapi(100, 3), 200000, "mamah, aku takut! 3")
        self.assertEqual(tarif_keretaapi(104, 3), 280000, "mamah, aku takut! 3")
        self.assertEqual(tarif_keretaapi(4531, 3), 88820000, "mamah, aku takut! 3")

    def test_kelas4(self):
        self.assertEqual(tarif_keretaapi(99, 4), 250000, "mamah, aku takut! 4")
        self.assertEqual(tarif_keretaapi(100, 4), 250000, "mamah, aku takut! 4")
        self.assertEqual(tarif_keretaapi(104, 4), 350000, "mamah, aku takut! 4")
        self.assertEqual(tarif_keretaapi(4531, 4), 111025000, "mamah, aku takut! 4")

        self.assertEqual(tarif_keretaapi(99), 250000, "butuh default argument. Jika tidak ada informasi Tipe Kereta Api, maka diasumsikan memggunakan masuk dalam Kelas 4. ")
        self.assertEqual(tarif_keretaapi(100), 250000, "butuh default argument. Jika tidak ada informasi Tipe Kereta Api, maka diasumsikan memggunakan masuk dalam Kelas 4. ")
        self.assertEqual(tarif_keretaapi(104), 350000, "butuh default argument. Jika tidak ada informasi Tipe Kereta Api, maka diasumsikan memggunakan masuk dalam Kelas 4. ")
        self.assertEqual(tarif_keretaapi(4531), 111025000, "butuh default argument. Jika tidak ada informasi Tipe Kereta Api, maka diasumsikan memggunakan masuk dalam Kelas 4. ")

unittest.main()