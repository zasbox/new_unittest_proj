import unittest

from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial", "venv": "poetry", "interptetator": "python"},
                                       "vcs", "bazaar"), "mercurial")
        self.assertEqual(dicts.get_val({"vcs": "mercurial", "venv": "poetry", "interptetator": "python"},
                                       "cms", "bazaar"), "bazaar")
        self.assertEqual(dicts.get_val({"vcs": "mercurial", "venv": "poetry", "interptetator": "python"},
                                       "cms"), "git")

