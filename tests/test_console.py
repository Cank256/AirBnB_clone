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

    # Test case for the "show" command
    def test_show_valid_instance(self):
        with patch('sys.stdout', new=self.stdout):
            # Create an instance of the class you want to test "show" on
            self.console.onecmd("create User")
            output = self.stdout.getvalue().strip()
            instance_id = output.split(".")[1]
            # Now, test the "show" command on this instance
            self.console.onecmd(f"show User {instance_id}")
            output = self.stdout.getvalue().strip()
            self.assertTrue("User" in output)
            self.assertTrue(instance_id in output)

    # Test case for the "destroy" command
    def test_destroy_valid_instance(self):
        with patch('sys.stdout', new=self.stdout):
            # Create an instance of the class you want to test "destroy" on
            self.console.onecmd("create User")
            output = self.stdout.getvalue().strip()
            instance_id = output.split(".")[1]
            # Now, test the "destroy" command on this instance
            self.console.onecmd(f"destroy User {instance_id}")
            output = self.stdout.getvalue().strip()
            self.assertEqual(output, "")

    # Test case for the "all" command
    def test_all_command(self):
        with patch('sys.stdout', new=self.stdout):
            # Test the "all" command for a specific class
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("all User")
            output = self.stdout.getvalue().strip()
            self.assertTrue("User" in output)
            self.assertTrue("1:" in output)
            self.assertTrue("2:" in output)

    # Add test cases for the "update" command
    def test_update_valid_instance(self):
        with patch('sys.stdout', new=self.stdout):
            # Create an instance of the class you want to test "update" on
            self.console.onecmd("create User")
            output = self.stdout.getvalue().strip()
            instance_id = output.split(".")[1]

            # Now, test the "update" command on this instance
            self.console.onecmd(f"update User {instance_id} first_name 'John'")
            self.console.onecmd(f"show User {instance_id}")
            output = self.stdout.getvalue().strip()
            self.assertTrue("John" in output)

    # Add test cases for the "default" function
    def test_default_show(self):
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create User")
            instance_id = self.stdout.getvalue().strip().split(".")[1]
            self.stdout.truncate(0)
            self.console.onecmd(f"User.show({instance_id})")
            output = self.stdout.getvalue().strip()
            self.assertTrue("John" in output)

    def test_do_quit(self):
        with patch('sys.stdout', new=self.stdout):
            result = self.console.onecmd("quit")
        self.assertTrue(result)  # Should return True to quit the program.

    def test_do_EOF(self):
        with patch('sys.stdout', new=self.stdout):
            result = self.console.onecmd("EOF")
        self.assertTrue(result)  # Should return True to quit the program.

    def test_emptyline(self):
        with patch('sys.stdout', new=self.stdout):
            result = self.console.onecmd("")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
