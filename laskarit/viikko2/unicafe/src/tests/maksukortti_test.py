import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    def test_kortin_saldo_alussa(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa(self):
        self.kortti.lataa_rahaa(2500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_jos_rahaa(self):
        self.kortti.ota_rahaa(500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_liian_vahan_rahaa(self):
        self.kortti.ota_rahaa(1500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_tarpeeksi_rahaa(self):
        self.assertEqual(self.kortti.ota_rahaa(500), True)

    def test_metodi_palauttaa_false_jos_liian_vahan_rahaa(self):
        self.assertEqual(self.kortti.ota_rahaa(1500), False)
