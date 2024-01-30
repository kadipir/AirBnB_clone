#!/usr/bin/python3
"""
update on the console to increase its functionality
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """
    class used to create the console
    """
    prompt = "(hbnb)"
    valid_class = ["BaseModel"]
    def do_quit(self,arg):
         """
         command to exit the program
         """
         return True

    def help_quit(self,arg):
         """
         documents the function of quit
         """
         print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def do_create(self, arg):
        """
        create new instance of the BaseModel and save it the json file
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self,arg):
        """
        prints the string representation of an instance based on the class name and id.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            object = storage.all()
            key = "{}.{}".format(commands[0],commands[1])
            if key in object:
                print(str(object[key]))
            else:
                print("** no instance found **")

    def do_destroy(self,arg):
        """
        Deletes an instance based on the class name and id
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_class:
            print("** class doesn't exist ** ")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0],commands[1])
            if key in objects:
                del(objects[key])
            else:
                print("** no instance found ** ")

    def do_all(self,arg):
        """
         Prints all string representation of all 
         instances based or not on the class name.
        """
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
           for key, value in objects.items():
              print(str(value))
        elif commands[0] not in self.valid_class:
           print("** class doesn't exist **")
        else:
           for key,value in objects.items():
              if key.split('.')[0] == commands[0]:
                   print(str(value))
    def do_update(self,arg):
        commands = shlex.split(args)
        if len(commands) == 0:
           print(" ** class name missing ** ")
        elif commands[0] not in valid_class:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print(" ** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0],commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing ** (")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attribute_name = commands[2]
                attribute_value = commands[3]
                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(obj,attribute_name,attribute_value)
                obj.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
