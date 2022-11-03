import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1)
        self.varasto3 = Varasto(1, 2)
        self.varasto4 = Varasto(1, -2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(12)

        # lisää liikaa, mutta tilaa on silti jäljellä 0
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ota_liikaa(self):
        #self.varasto.lisaa_varastoon(12)
        self.varasto.ota_varastosta(14)

        #10+14 = 4, mutta palauttaa tasan 10
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_ota_negatiivinen_maara(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_lisaa_liian_vahan(self):
        miinus = self.varasto.lisaa_varastoon(-1)
        
        self.assertEqual(miinus, None)

    def test_str(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(self.varasto.__str__(), f"saldo = 8, vielä tilaa 2")

    def test_tilavuus(self):
        self.assertEqual(self.varasto2.tilavuus, 0)
    
    def test_saldoa_liikaa(self):
        #alkusaldo on isompi kuin tilavuus
        self.assertAlmostEqual(self.varasto3.saldo, 1)

    def test_saldo(self):
        #alkusaldo on negatiivinen
        self.assertAlmostEqual(self.varasto4.saldo, 0.0)