from unittest import TestCase
from handlers import pulls
from tests import test_shnipov


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_get_git_json(self):
        """Test git key"""
        self.assertTrue(pulls.get_git_json())

    def test_get_pulls(self):
        """"Test states"""
        result = pulls.get_pulls("accepted")
        self.assertIsInstance(result, list)
        result = pulls.get_pulls("open")
        self.assertIsInstance(result, list)
        result = pulls.get_pulls("closed")
        self.assertIsInstance(result, list)
        result = pulls.get_pulls("needs work")
        self.assertIsInstance(result, list)

    def test_get_data_all(self):
        """Test get all data"""
        self.assertEqual(pulls.get_data_all(test_shnipov),
                         test_shnipov.result_data_all)

    def tearDown(self):
        """Finish"""
