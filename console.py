#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Class to command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing for an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
