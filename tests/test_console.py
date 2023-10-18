import unittest
from unittest.mock import patch
from console import HBNBCommand
import io
import sys


class ConsoleTest(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('create User')
            self.assertEqual(f.getvalue(), '12345678-90ab-cdef-ghij-klmnopqrstuvwx\n')

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('show User 12345678-90ab-cdef-ghij-klmnopqrstuvwx')
            self.assertEqual(f.getvalue(), '[User]\n')

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('destroy User 12345678-90ab-cdef-ghij-klmnopqrstuvwx')
            self.assertEqual(f.getvalue(), '\n')

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('all User')
            self.assertEqual(f.getvalue(), '[User]\n')

    def test_update(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('update User 12345678-90ab-cdef-ghij-klmnopqrstuvwx name="Bard"')
            self.assertEqual(f.getvalue(), '\n')

    def test_invalid_command(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('invalid_command')
            self.assertEqual(f.getvalue(), 'Unknown command: invalid_command\n')

    def test_help(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('help')
            self.assertIn('create', f.getvalue())
            self.assertIn('show', f.getvalue())
            self.assertIn('destroy', f.getvalue())
            self.assertIn('all', f.getvalue())
            self.assertIn('update', f.getvalue())

    def test_help_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('help show')
            self.assertIn('Show the string representation of an instance', f.getvalue())
            self.assertIn('Usage:', f.getvalue())
            self.assertIn('Example:', f.getvalue())


if __name__ == '__main__':
    unittest.main()