#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = StringIO()

    def tearDown(self):
        self.stdout.close()

    def test_create_valid_class(self):
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create User")
            output = self.stdout.getvalue().strip()
            self.assertTrue(output.startswith("User."))

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create InvalidClass")
            output = self.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    # Add more test cases for other features (show, destroy, update, all, etc.)

if __name__ == '__main__':
    unittest.main()
