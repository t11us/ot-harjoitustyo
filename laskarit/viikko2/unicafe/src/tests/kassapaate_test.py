import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kp = Kassapaate()
        self.kortti = Maksukortti(1000)


    #Testataan setup-asiat
    def test_rahamaara_oikein(self):
        self.assertEqual(self.kp.kassassa_rahaa, 100000)
    
    def test_edulliset_maara_oikein(self):
        self.assertEqual(self.kp.edulliset, 0)

    def test_maukkaat_maara_oikein(self):
        self.assertEqual(self.kp.maukkaat, 0)

    #Testataan edullisesti syomista kateisella
    def test_kateinen_riittaa_syo_edullisesti_oikea_vaihtoraha(self):
        self.assertEqual(self.kp.syo_edullisesti_kateisella(241), 1)
    
    def test_kateinen_riittaa_syo_edullisesti_kassassa_oikea_rahamaara(self):
        self.kp.syo_edullisesti_kateisella(241)
        self.assertEqual(self.kp.kassassa_rahaa, 100240)
    
    def test_kateinen_riittaa_syo_edullisesti_lounasmaara_kasvaa(self):
        self.kp.syo_edullisesti_kateisella(241)
        self.assertEqual(self.kp.edulliset, 1)
        self.assertEqual(self.kp.maukkaat, 0)

    def test_kateinen_ei_riita_syo_edullisesti_oikea_vaihtoraha(self):
        self.assertEqual(self.kp.syo_edullisesti_kateisella(239), 239)

    def test_kateinen_ei_riita_syo_edullisesti_kassassa_oikea_rahamaara(self):
        self.kp.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kp.kassassa_rahaa, 100000)
    
    def test_kateinen_ei_riita_syo_edullisesti_lounasmaara_kasvaa(self):
        self.kp.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)

    #Testataan maukkaasti syomista kateisella
    def test_kateinen_riittaa_syo_maukkaasti_oikea_vaihtoraha(self):
        self.assertEqual(self.kp.syo_maukkaasti_kateisella(401), 1)
    
    def test_kateinen_riittaa_syo_maukkaasti_kassassa_oikea_rahamaara(self):
        self.kp.syo_maukkaasti_kateisella(401)
        self.assertEqual(self.kp.kassassa_rahaa, 100400)
    
    def test_kateinen_riittaa_syo_maukkaasti_lounasmaara_kasvaa(self):
        self.kp.syo_maukkaasti_kateisella(401)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 1)

    def test_kateinen_ei_riita_syo_maukkaasti_oikea_vaihtoraha(self):
        self.assertEqual(self.kp.syo_maukkaasti_kateisella(239), 239)

    def test_kateinen_ei_riita_syo_maukkaasti_kassassa_oikea_rahamaara(self):
        self.kp.syo_maukkaasti_kateisella(239)
        self.assertEqual(self.kp.kassassa_rahaa, 100000)
    
    def test_kateinen_ei_riita_syo_maukkaasti_lounasmaara_kasvaa(self):
        self.kp.syo_maukkaasti_kateisella(239)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)

    #Testataan edullisesti syomista kortilla
    def test_kortilla_riittaa_syo_edullisesti_palauttaa_true(self):
        self.assertEqual(self.kp.syo_edullisesti_kortilla(self.kortti), True)

    def test_kortilla_riittaa_syo_edullisesti_kortilta_veloitetaan(self):
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_kortilla_riittaa_syo_edullisesti_lounasmaara_kasvaa(self):
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 1)
        self.assertEqual(self.kp.maukkaat, 0)

    def test_kortilla_ei_riita_syo_edullisesti_palauttaa_false(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kp.syo_edullisesti_kortilla(self.kortti), False)

    def test_kortilla_ei_riita_syo_edullisesti_kortilta_veloitetaan(self):
        self.kortti.ota_rahaa(900)
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_kortilla_ei_riita_syo_edullisesti_lounasmaara_kasvaa(self):
        self.kortti.ota_rahaa(900)
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)

    #Testataan maukkaasti syomista kortilla
    def test_kortilla_riittaa_syo_maukkaasti_palauttaa_true(self):
        self.assertEqual(self.kp.syo_maukkaasti_kortilla(self.kortti), True)

    def test_kortilla_riittaa_syo_maukkaasti_kortilta_veloitetaan(self):
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_kortilla_riittaa_syo_maukkaasti_lounasmaara_kasvaa(self):
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 1)

    def test_kortilla_ei_riita_syo_maukkaasti_palauttaa_false(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kp.syo_maukkaasti_kortilla(self.kortti), False)

    def test_kortilla_ei_riita_syo_maukkaasti_kortilta_veloitetaan(self):
        self.kortti.ota_rahaa(900)
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_kortilla_ei_riita_syo_maukkaasti_lounasmaara_kasvaa(self):
        self.kortti.ota_rahaa(900)
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)

    #Testataan rahan lataamista kortille
    def test_lataa_rahaa_kortille_positiivinen_luku_oikea_maara_kortilla(self):
        self.kp.lataa_rahaa_kortille(self.kortti, 9)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.09 euroa")

    def test_lataa_rahaa_kortille_positiivinen_luku_oikea_maara_kassassa(self):
        self.kp.lataa_rahaa_kortille(self.kortti, 9)
        self.assertEqual(self.kp.kassassa_rahaa, 100009)

    def test_lataa_rahaa_kortille_negatiivinen_luku_oikea_maara_kortilla(self):
        self.kp.lataa_rahaa_kortille(self.kortti, -9)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kortille_negatiivinen_luku_oikea_maara_kassassa(self):
        self.kp.lataa_rahaa_kortille(self.kortti, -9)
        self.assertEqual(self.kp.kassassa_rahaa, 100000)

    