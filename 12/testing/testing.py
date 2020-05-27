import unittest

from name import format_name

class NameTest(unittest.TestCase):
    """Тесты для функции format_name"""

    def test1(self):
        formated = format_name('ivan', 'ivanov')
        self.assertEqual(formated, 'Ivan Ivanov')

    def test2(self):
        formated = format_name('ivan', 'ivanov', 'ivanovich')
        self.assertEqual(formated, 'Ivan Ivanov Ivanovich')
        self.assertNotEqual()
        self.assertTrue()
        self.assertFalse()
        self.assertIn()


unittest.main()
print(dir(unittest.TestCase))