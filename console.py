#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """do nothing upon empty line and enter
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
