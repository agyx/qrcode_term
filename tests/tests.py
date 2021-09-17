import base64
import unittest

from src import qrcode_term


class TestQRCodeTerm(unittest.TestCase):
    """
    venv/bin/python -m unittest discover -s tests
    """

    def generic_test(self, output, expected):
        print()
        print(output)
        text_output = base64.b64encode(output.encode("utf-8"))
        self.assertEqual(text_output, expected)

    def test_basic_1(self):
        """
        Test that basic use is OK
        """
        self.generic_test(qrcode_term.qrcode_string("Hello"),
                          (b'G1s5N23ilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilogK4paI4paI4paI4paA4paA4paA4paA4paA4paA'
                           b'4paA4paI4paI4paA4paA4paA4paA4paI4paA4paA4paA4paA4paA4paA4paA4paI4paI4paICuKW'
                           b'iOKWiOKWiCDilojiloDiloDiloDilogg4paI4paA4paI4paA4paIIOKWiCDilojiloDiloDiloDi'
                           b'logg4paI4paI4paICuKWiOKWiOKWiCDiloggICDilogg4paIIOKWgOKWhOKWiOKWgOKWiCDilogg'
                           b'ICDilogg4paI4paI4paICuKWiOKWiOKWiCDiloDiloDiloDiloDiloAg4paIIOKWhOKWgOKWhOKW'
                           b'gOKWiCDiloDiloDiloDiloDiloAg4paI4paI4paICuKWiOKWiOKWiOKWgOKWiOKWgOKWgOKWgOKW'
                           b'gOKWgOKWiOKWhOKWgOKWhOKWgOKWiOKWiOKWgOKWgOKWgOKWgOKWgOKWiOKWiOKWiOKWiOKWiAri'
                           b'lojilojilojilojilojiloAg4paA4paA4paA4paI4paE4paA4paA4paEIOKWhCDiloDiloggIOKW'
                           b'gOKWhOKWiOKWiOKWiArilojilojilojilojiloAg4paA4paI4paE4paAICDiloAg4paEIOKWhOKW'
                           b'hOKWgOKWiOKWhOKWhOKWiOKWgOKWiOKWiOKWiArilojilojilojiloDiloDiloDiloDiloDiloDi'
                           b'loDilojiloTiloDilojiloDiloTiloDilojiloTiloDiloTiloDiloDilojilojilojilogK4paI'
                           b'4paI4paIIOKWiOKWgOKWgOKWgOKWiCDilogg4paI4paE4paA4paI4paA4paI4paEIOKWhOKWhCDi'
                           b'lojilojilojilogK4paI4paI4paIIOKWiCAgIOKWiCDiloggIOKWiOKWhCDiloQgIOKWiOKWhOKW'
                           b'gOKWiOKWiOKWiOKWiOKWiArilojilojilogg4paA4paA4paA4paA4paAIOKWiOKWgCDilojiloQg'
                           b'4paE4paE4paIIOKWhOKWhOKWgOKWiOKWiOKWiOKWiArilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilogK'
                           b'4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA'
                           b'4paA4paA4paA4paA4paA4paA4paA4paAG1szOW0='))

    def test_frame_1(self):
        """
        Test that frame width parameter works with some arbitrary value
        """
        self.generic_test(qrcode_term.qrcode_string("QRCode with frame 5", frame_width=5),
                          (b'G1s5N23ilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilogK4paI'
                           b'4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI'
                           b'4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paICuKWiOKWiOKWiOKW'
                           b'iOKWiOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWiOKWiOKWiOKWiOKWgOKWiOKWiOKWiOKWiOKWiOKW'
                           b'iOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWiOKWiOKWiOKWiOKWiArilojilojilojilojilogg4paI'
                           b'4paA4paA4paA4paIIOKWiOKWgCDilojilojilojilojiloggIOKWiCDilojiloDiloDiloDilogg'
                           b'4paI4paI4paI4paI4paICuKWiOKWiOKWiOKWiOKWiCDiloggICDilogg4paIIOKWhCDiloTiloDi'
                           b'loTiloDiloTiloDilogg4paIICAg4paIIOKWiOKWiOKWiOKWiOKWiArilojilojilojilojilogg'
                           b'4paA4paA4paA4paA4paAIOKWiCDiloTiloDiloQg4paIIOKWhCDilogg4paA4paA4paA4paA4paA'
                           b'IOKWiOKWiOKWiOKWiOKWiArilojilojilojilojilojiloDilojiloDiloDiloDiloDiloDiloji'
                           b'loTiloTilojiloDiloDilojiloTiloTiloTilojiloDiloDiloDiloDiloDilojilojilojiloji'
                           b'lojilojilogK4paI4paI4paI4paI4paIIOKWiCDiloTiloTilojiloAg4paE4paAIOKWgCAg4paA'
                           b'4paAICDiloAg4paI4paE4paA4paAIOKWiOKWiOKWiOKWiOKWiArilojilojilojilojilojiloDi'
                           b'loAg4paAIOKWgOKWgCDilojiloAg4paE4paA4paE4paAIOKWiOKWgCDilogg4paA4paA4paI4paA'
                           b'4paI4paI4paI4paI4paICuKWiOKWiOKWiOKWiOKWiCDilojiloQg4paE4paA4paA4paEIOKWgOKW'
                           b'gOKWgOKWgOKWiOKWiOKWgOKWhOKWiOKWiCDiloDiloggICDilojilojilojilojilogK4paI4paI'
                           b'4paI4paI4paIIOKWiOKWgOKWhOKWgOKWgOKWgOKWgOKWiOKWgCAg4paI4paI4paE4paA4paA4paA'
                           b'ICDiloDiloDiloDiloQg4paI4paI4paI4paI4paICuKWiOKWiOKWiOKWiOKWiOKWgOKWgOKWgOKW'
                           b'gOKWgOKWgOKWgOKWiOKWhCDiloTilojiloQgIOKWiCDilojiloDilogg4paA4paIICDilojiloji'
                           b'lojilojilogK4paI4paI4paI4paI4paIIOKWiOKWgOKWgOKWgOKWiCDilogg4paA4paI4paIIOKW'
                           b'hOKWgOKWgCDiloDiloDiloAg4paA4paA4paE4paA4paI4paI4paI4paI4paICuKWiOKWiOKWiOKW'
                           b'iOKWiCDiloggICDilogg4paIICAg4paA4paA4paI4paI4paE4paE4paI4paEIOKWhOKWiOKWiOKW'
                           b'hCDilojilojilojilojilogK4paI4paI4paI4paI4paIIOKWgOKWgOKWgOKWgOKWgCDilojiloDi'
                           b'loDiloQg4paI4paI4paE4paE4paE4paIIOKWiOKWiCDiloDiloAg4paI4paI4paI4paI4paICuKW'
                           b'iOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKW'
                           b'iOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiArilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilogK4paA4paA4paA4paA4paA4paA'
                           b'4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA'
                           b'4paA4paA4paA4paA4paA4paA4paA4paA4paA4paAG1szOW0='))

    def test_inverse_1(self):
        """
        Test that inverse parameter works with some arbitrary value
        """
        self.generic_test(qrcode_term.qrcode_string("inverse=True", inverse=True),
                          (b'G1s5N20gICAgICAgICAgICAgICAgICAgICAgICAgICAKICAg4paE4paE4paE4paE4paE4paE4paE'
                           b'ICAgICAgIOKWhOKWhOKWhOKWhOKWhOKWhOKWhCAgIAogICDilogg4paE4paE4paEIOKWiCDiloTi'
                           b'logg4paE4paIIOKWiCDiloTiloTiloQg4paIICAgCiAgIOKWiCDilojilojilogg4paIIOKWiOKW'
                           b'iOKWiOKWiOKWiCDilogg4paI4paI4paIIOKWiCAgIAogICDilojiloTiloTiloTiloTiloTilogg'
                           b'4paIIOKWiCDilogg4paI4paE4paE4paE4paE4paE4paIICAgCiAgIOKWhCDiloTiloTiloTiloTi'
                           b'loQg4paAIOKWiOKWgOKWiCDiloTiloTiloTiloTiloQgICAgIAogICDiloTilojiloDiloTiloTi'
                           b'lojiloTiloDiloTilogg4paE4paA4paI4paA4paE4paA4paAIOKWhOKWgCAgIAogICAg4paIIOKW'
                           b'gOKWhOKWiOKWhCDiloDilojilojiloQg4paIICAg4paI4paA4paA4paEICAgCiAgIOKWhOKWhOKW'
                           b'hOKWhOKWhOKWhOKWhCDiloDiloDiloQg4paI4paAIOKWgOKWgOKWgOKWgOKWhOKWgCAgIAogICDi'
                           b'logg4paE4paE4paEIOKWiCDilojiloQg4paI4paI4paI4paE4paE4paA4paA4paA4paE4paEICAg'
                           b'CiAgIOKWiCDilojilojilogg4paIIOKWiOKWiOKWiOKWhOKWhCDiloQg4paA4paI4paIICAgICAK'
                           b'ICAg4paI4paE4paE4paE4paE4paE4paIIOKWhCAg4paI4paI4paI4paE4paI4paA4paI4paA4paE'
                           b'ICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg'
                           b'ICAgG1szOW0='))

    def test_ansi_white_1(self):
        """
        Test that ansi_white parameter works with False
        """
        self.generic_test(qrcode_term.qrcode_string("ansi_white=False", ansi_white=False),
                          (b'4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI'
                           b'4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paICuKWiOKWiOKWiOKWgOKWgOKWgOKW'
                           b'gOKWgOKWgOKWgOKWiOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWiOKWgOKWiOKWgOKWgOKWgOKWgOKW'
                           b'gOKWgOKWgOKWiOKWiOKWiArilojilojilogg4paI4paA4paA4paA4paIIOKWiOKWiCDilojiloTi'
                           b'loDiloQg4paE4paI4paIIOKWiOKWgOKWgOKWgOKWiCDilojilojilogK4paI4paI4paIIOKWiCAg'
                           b'IOKWiCDilogg4paE4paA4paIIOKWiOKWiOKWiOKWhOKWiCDiloggICDilogg4paI4paI4paICuKW'
                           b'iOKWiOKWiCDiloDiloDiloDiloDiloAg4paIIOKWhCDiloTiloDilojiloDilogg4paIIOKWgOKW'
                           b'gOKWgOKWgOKWgCDilojilojilogK4paI4paI4paI4paA4paI4paI4paI4paA4paI4paA4paAIOKW'
                           b'gOKWgCAgIOKWiOKWhOKWiOKWgOKWgOKWgOKWgOKWgOKWiOKWiOKWgOKWiOKWiOKWiArilojiloji'
                           b'lojiloDiloDiloQgIOKWgOKWgCDiloDiloDilojilogg4paE4paEIOKWhOKWiOKWiOKWiOKWhOKW'
                           b'iOKWiOKWhOKWiOKWiOKWiOKWiArilojilojilojilojiloTiloQg4paA4paE4paA4paEIOKWgOKW'
                           b'iOKWiOKWiOKWgCDilogg4paI4paA4paE4paI4paIICDiloTilojilojilogK4paI4paI4paI4paE'
                           b'4paI4paA4paIIOKWhOKWgOKWiOKWgOKWhOKWgOKWgCDiloDiloAgIOKWhOKWgOKWgOKWhOKWiCDi'
                           b'lojilojilojilojilogK4paI4paI4paI4paA4paA4paIIOKWgOKWhOKWgOKWhOKWhCDiloTiloTi'
                           b'loAg4paIIOKWgOKWgOKWgOKWgCDiloDiloTilojiloDilojilojilogK4paI4paI4paI4paA4paA'
                           b'4paA4paA4paA4paA4paA4paIIOKWgOKWgOKWiOKWiOKWhOKWhOKWiCDilojiloDilogg4paE4paE'
                           b'4paI4paI4paI4paI4paICuKWiOKWiOKWiCDilojiloDiloDiloDilogg4paI4paAIOKWhOKWgOKW'
                           b'hOKWgCDilogg4paA4paA4paAIOKWgCDiloTiloDilojilojilogK4paI4paI4paIIOKWiCAgIOKW'
                           b'iCDilojilogg4paE4paAIOKWgOKWgCDiloAg4paEIOKWiOKWhOKWiCDiloTilojilojilogK4paI'
                           b'4paI4paIIOKWgOKWgOKWgOKWgOKWgCDilojiloDiloTiloTiloTiloAg4paIIOKWiOKWiOKWiOKW'
                           b'gOKWiOKWiCAg4paA4paI4paI4paICuKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKW'
                           b'iOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKW'
                           b'iAriloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDi'
                           b'loDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloDiloA='))

    def test_version_1(self):
        """
        Test that version parameter works with some arbitrary value
        """
        self.generic_test(qrcode_term.qrcode_string("version=5", version=5),
                          (b'G1s5N23ilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilogK4paI4paI4paI4paA4paA4paA4paA4paA4paA4paA4paI4paA'
                           b'4paA4paA4paA4paA4paI4paA4paI4paA4paA4paA4paA4paI4paI4paA4paI4paA4paI4paA4paI'
                           b'4paA4paI4paA4paA4paA4paA4paA4paA4paA4paI4paI4paICuKWiOKWiOKWiCDilojiloDiloDi'
                           b'loDilogg4paI4paI4paA4paAIOKWgOKWiOKWiOKWiOKWiOKWhOKWiOKWgCDiloDilojiloDiloji'
                           b'loDilojiloTilojilogg4paI4paA4paA4paA4paIIOKWiOKWiOKWiArilojilojilogg4paIICAg'
                           b'4paIIOKWiCDiloDiloTilojiloDilogg4paE4paE4paEICAgICDiloTilojiloAg4paI4paI4paI'
                           b'IOKWiCAgIOKWiCDilojilojilogK4paI4paI4paIIOKWgOKWgOKWgOKWgOKWgCDilogg4paE4paA'
                           b'4paI4paA4paEIOKWiCDilogg4paE4paA4paEIOKWhCDiloQg4paIIOKWiCDiloDiloDiloDiloDi'
                           b'loAg4paI4paI4paICuKWiOKWiOKWiOKWgOKWiOKWiOKWiOKWgOKWiOKWgOKWgCDiloDiloDiloDi'
                           b'loTiloAg4paA4paI4paEIOKWgOKWiOKWiCDiloAg4paAIOKWhCDiloDiloDiloDiloDiloDiloji'
                           b'lojiloDilojilojilogK4paI4paI4paI4paE4paEIOKWhOKWgOKWhOKWgCDiloAg4paA4paAIOKW'
                           b'iOKWhOKWiCDiloDilojiloQg4paE4paI4paI4paI4paE4paI4paA4paI4paE4paEIOKWhOKWiOKW'
                           b'gOKWhOKWiOKWiOKWiOKWiArilojilojilojiloDiloTilojiloDilojiloTiloAg4paA4paA4paA'
                           b'IOKWhCDiloTiloDiloDiloQg4paA4paA4paIIOKWgOKWhOKWgCDiloTiloTilojiloDilojilogg'
                           b'4paE4paA4paA4paI4paI4paICuKWiOKWiOKWiOKWhCDiloQgIOKWgOKWgOKWgCDiloTilojiloDi'
                           b'lojiloDiloDiloDilojiloTiloAg4paI4paA4paA4paAIOKWgOKWgOKWiCDiloggIOKWhOKWgOKW'
                           b'iOKWiCDilojilojilogK4paI4paI4paI4paE4paEIOKWgOKWhOKWgOKWgOKWiOKWgCAg4paAIOKW'
                           b'gOKWhOKWhCDilojilojiloQg4paE4paI4paE4paIIOKWiOKWgOKWiCDiloQgIOKWgCAg4paE4paI'
                           b'4paI4paICuKWiOKWiOKWiOKWiCDiloTiloDiloTiloDiloDiloTiloDiloDiloDiloDiloDiloji'
                           b'loDiloDilojiloQgIOKWiOKWgCDiloAg4paAIOKWiCDilogg4paI4paAIOKWhOKWiOKWiOKWiOKW'
                           b'iOKWiArilojilojilojilogg4paAICDiloTiloDilojilojilogg4paA4paI4paEIOKWhOKWhOKW'
                           b'iOKWiOKWhOKWhOKWhOKWiOKWhOKWgCDilojiloDiloAg4paE4paE4paE4paI4paIICDilojiloji'
                           b'logK4paI4paI4paI4paA4paEIOKWhOKWhOKWgOKWgCDiloTiloDiloDiloDilojilojilojilogg'
                           b'4paA4paE4paEIOKWhOKWhOKWiOKWiOKWhOKWhOKWgOKWiOKWgOKWhOKWhCDilojilogg4paE4paI'
                           b'4paI4paICuKWiOKWiOKWiOKWiCAg4paI4paI4paE4paAICDilojilogg4paA4paEIOKWgOKWiOKW'
                           b'hCDiloDilojilogg4paAIOKWgCDiloQg4paI4paA4paEIOKWiCDilojiloDilojilojilogK4paI'
                           b'4paI4paI4paE4paI4paI4paI4paI4paI4paA4paE4paE4paA4paA4paE4paI4paEIOKWiCDiloDi'
                           b'lojiloQg4paE4paI4paI4paI4paE4paI4paA4paIIOKWhCDiloTilojiloDiloTilojilojiloji'
                           b'logK4paI4paI4paI4paA4paA4paEIOKWiCDiloAg4paA4paA4paE4paE4paIIOKWiOKWgOKWgOKW'
                           b'hCDiloDiloDilogg4paA4paE4paAIOKWhCDiloDiloDiloDiloAg4paE4paI4paI4paI4paI4paI'
                           b'CuKWiOKWiOKWiOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWiCDiloTiloQg4paA4paE4paA4paA4paI'
                           b'4paE4paAIOKWiOKWgOKWgOKWgCDiloDiloDiloAg4paI4paA4paIIOKWiCDilogg4paI4paI4paI'
                           b'CuKWiOKWiOKWiCDilojiloDiloDiloDilogg4paI4paA4paI4paE4paI4paA4paAIOKWhCDiloji'
                           b'lojiloQg4paE4paI4paE4paIIOKWiOKWgCDiloDiloDiloAg4paIICDiloTilojilojilogK4paI'
                           b'4paI4paIIOKWiCAgIOKWiCDilojilojiloDiloTiloDiloDiloDiloTiloDilojiloQgIOKWiOKW'
                           b'gCDiloAg4paAIOKWiOKWhOKWiOKWhCDilogg4paE4paA4paE4paI4paI4paICuKWiOKWiOKWiCDi'
                           b'loDiloDiloDiloDiloAg4paI4paA4paAIOKWgCDiloAg4paE4paE4paI4paI4paE4paE4paE4paI'
                           b'4paE4paAIOKWiCAg4paI4paE4paE4paE4paI4paIIOKWgOKWiOKWiOKWiArilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'lojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojilojiloji'
                           b'logK4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA'
                           b'4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA4paA'
                           b'4paA4paA4paA4paA4paA4paAG1szOW0='))


if __name__ == '__main__':
    unittest.main()
