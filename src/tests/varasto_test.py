import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_til_alle_0 = Varasto(-5)
        self.varasto_saldo_alle_0 = Varasto(10, -2)
        self.varasto_saldo_yli_til = Varasto(10, 13)

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

    # Omia
    def test_oikea_str_format(self):
        self.assertAlmostEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
    
    def test_tilavuus_alle_0(self):
        self.assertAlmostEqual(self.varasto_til_alle_0.tilavuus, 0.0)

    def test_alku_saldo_alle_0(self):
        self.assertAlmostEqual(self.varasto_saldo_alle_0.saldo, 0.0)
    
    def test_alku_saldo_yli_tilavuus(self):
        self.assertAlmostEqual(self.varasto_saldo_yli_til.saldo, self.varasto_saldo_yli_til.tilavuus)
    
    def test_lisays_alle_0_ei_tee_mitaan(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        # pysyy samana
        self.assertAlmostEqual(saldo_ennen, self.varasto.saldo)
    
    def test_lisays_yli_paljonko_mahtuu(self):
        # tilavuus 10
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_alle_0_palauttaa_0(self):
        otettu = self.varasto.ota_varastosta(-4)
        self.assertAlmostEqual(otettu, 0.0)
    
    def test_ota_yli_saldo_menee_0(self):
        # tilavuus 10
        self.varasto.ota_varastosta(69)
        self.assertAlmostEqual(self.varasto.saldo, 1.0)
    
    def test_ota_yli_palauttaa_kaiken_mita_voi(self):
        # tilavuus 10
        saldo_ennen = self.varasto.saldo
        otettu = self.varasto.ota_varastosta(69)
        self.assertAlmostEqual(saldo_ennen, otettu)