#!/usr/bin/python3
"""
"""
import cmd
class HBNBCommand(cmd.Cmd):
    """
    class used to create the console
    """
    prompt = "(hbnb)"
    def do_quit(self,arg):
         """
         command to exit the program
         """
         return True

    def help_quit(self):
         """
         documents the function of quit
         """
         print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
