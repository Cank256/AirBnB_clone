#!/usr/bin/python3
import cmd
from models.user import User
from models.base_model import BaseModel
from models import models, storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a valid Class and print its id\n"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in models:
            print("** class doesn't exist **")
            return

        try:
            new_instance = models[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Show the string representation of an instance\n"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, arg):
        """Show all instances or instances of a specific class\n"""
        class_name = arg if arg else None
        all_objects = storage.all()
        result = []

        if class_name:
            if class_name in models:
                for key, instance in all_objects.items():
                    if key.startswith(class_name + "."):
                        result.append(str(instance))
            else:
                print("** class doesn't exist **")
                return
        else:
            for instance in all_objects.values():
                result.append(str(instance))

        print(result)

    def do_update(self, arg):
        """Update an instance's attribute\n"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name, attr_value = args[2], args[3]

        if hasattr(instance, attr_name):
            attr_value = eval(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            # print("** attribute doesn't exist **")
            attr_value = eval(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()

    def default(self, line):
        """Handle dynamic method calls"""
        class_name, method = None, None
        args = []

        # Split the input into class_name and method
        if '.' in line:
            parts = line.split('.')
            class_name = parts[0]
            if '(' in parts[1]:
                method, args_str = parts[1].split('(', 1)
                args_str = args_str.rstrip(')').strip()

                if args_str:
                    if ',' in args_str:

                        id_arg, rest_args = args_str.split(',', 1)
                        id_arg = id_arg.strip()
                        rest_args = rest_args.strip()
                        rest_dict = {}

                        if id_arg.startswith('"') and id_arg.endswith('"'):
                            args.append(id_arg.strip('"'))
                        elif id_arg.startswith("'") and id_arg.endswith("'"):
                            args.append(id_arg.strip("'"))
                        else:
                            args.append(id_arg)

                        if rest_args.startswith('{') and \
                                rest_args.endswith('}'):
                            try:
                                rest_dict_args = eval(rest_args)
                                rest_dict.update(rest_dict_args)
                            except:
                                print("** Invalid dictionary format **")
                                return
                        else:
                            # Handle quotes around attribute and value
                            if (rest_args.startswith('"') and rest_args.endswith('"')) or \
                                        (rest_args.startswith("'") and rest_args.endswith("'")):
                                attr, value = rest_args[1:-1].split(',')
                            else:
                                attr, value = rest_args.split(',')

                            attr = attr.strip()
                            value = value.strip()
                            rest_dict[attr] = value

                        args.append(rest_dict)
                    else:
                        if args_str.startswith('"') and \
                                args_str.endswith('"'):
                            args.append(args_str.strip('"'))
                        elif args_str.startswith("'") and \
                                args_str.endswith("'"):
                            args.append(args_str.strip("'"))
                        else:
                            args.append(args_str)
            else:
                method = parts[1].strip()

        # Check if class_name is valid
        if class_name not in models:
            print("** class doesn't exist **")
            return

        # Check if the method exists and is callable
        cls = models[class_name]
        if hasattr(cls, method) and callable(getattr(cls, method)):
            if args:
                # Call the method with the dictionary argument
                result = getattr(cls, method)(*args)
            else:
                # Call the method without arguments
                result = getattr(cls, method)()

            if isinstance(result, list):
                for item in result:
                    print(item)
            elif result is not None:
                print(result)
        else:
            print(f"** method {method} doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
