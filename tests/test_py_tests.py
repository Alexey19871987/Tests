import pytest
from main import create_folder
from main import token


class TestFunctions:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_create_folder(self):
            assert create_folder(token) == 409
