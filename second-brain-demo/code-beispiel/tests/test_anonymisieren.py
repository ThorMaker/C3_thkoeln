import unittest

from lehreval.anonymisieren import anonymisiere


class TestAnonymisieren(unittest.TestCase):
    def test_mail_und_matrikel(self):
        text = "Bitte an erika@example.org schreiben, Matrikel 1234567."
        self.assertEqual(anonymisiere(text), "Bitte an [MAIL] schreiben, Matrikel [MATRIKEL].")

    def test_namen(self):
        self.assertEqual(anonymisiere("Max Mustermann fand es gut.", ["Max Mustermann"]), "[NAME] fand es gut.")


if __name__ == "__main__":
    unittest.main()
