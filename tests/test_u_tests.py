import unittest

from main import create_folder
from main import token


class TestFunc(unittest.TestCase):
    def setUp(self):
        print('setUp - work')

    def tearDown(self):
        print('tearDown - work')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass - work')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass - work')

    def test_create_folder(self):
        self.assertEqual(create_folder(token), 409)

    @unittest.expectedFailure
    def test_create_folderFail(self):
        self.assertEqual(create_folder(token), 201)
        