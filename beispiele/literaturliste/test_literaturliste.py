"""Tests für die Literaturliste. Sie beschreiben das gewünschte Verhalten."""
import unittest

from literaturliste import formatiere, sortiere


class TestSortierung(unittest.TestCase):
    def test_umlaute_nach_din_5007(self):
        eintraege = [
            {"autor": "Zimmer, A.", "jahr": 2020, "titel": "Z"},
            {"autor": "Özdemir, B.", "jahr": 2021, "titel": "Ö"},
            {"autor": "Ober, C.", "jahr": 2019, "titel": "O"},
            {"autor": "Abel, D.", "jahr": 2018, "titel": "A"},
        ]
        namen = [e["autor"] for e in sortiere(eintraege)]
        self.assertEqual(namen, ["Abel, D.", "Ober, C.", "Özdemir, B.", "Zimmer, A."])

    def test_gleicher_autor_nach_jahr(self):
        eintraege = [
            {"autor": "Luhmann, N.", "jahr": 1984, "titel": "Soziale Systeme"},
            {"autor": "Luhmann, N.", "jahr": 1981, "titel": "Kommunikation mit Zettelkästen"},
        ]
        jahre = [e["jahr"] for e in sortiere(eintraege)]
        self.assertEqual(jahre, [1981, 1984])


class TestFormatierung(unittest.TestCase):
    def test_normaler_eintrag(self):
        eintrag = {"autor": "Luhmann, N.", "jahr": 1981, "titel": "Kommunikation mit Zettelkästen"}
        self.assertEqual(formatiere(eintrag), "Luhmann, N. (1981). Kommunikation mit Zettelkästen.")

    def test_ohne_jahr(self):
        eintrag = {"autor": "TH Köln", "titel": "Handreichung für Lehrende"}
        self.assertEqual(formatiere(eintrag), "TH Köln (o. J.). Handreichung für Lehrende.")


if __name__ == "__main__":
    unittest.main()
