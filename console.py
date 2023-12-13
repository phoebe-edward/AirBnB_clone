#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb) "
    __classes = {"BaseModel",
                 "User",
                 "State",
                 "City",
                 "Amenity",
                 "Place",
                 "Review"}

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

    def do_create(self, arg):
        """creates a new BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in HBNBCommand.__classes:
            BM = eval(arg)()
            BM.save()
            print(BM.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """shows the instance with given id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg.split()[0],
                             arg.split()[1])) not in (storage.all()).keys():
            print("** no instance found **")
        else:
            objs = storage.all()
            print(objs["{}.{}".format(arg.split()[0], arg.split()[1])])

    def do_destroy(self, arg):
        """destroys the instance with given id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg.split()[0],
                             arg.split()[1])) not in (storage.all()).keys():
            print("** no instance found **")
        else:
            objs = storage.all()
            del objs["{}.{}".format(arg.split()[0], arg.split()[1])]
            storage.save()

    def do_all(self, arg):
        """prints all string representations of all instances
        based or not on the class name
        """
        if len(arg) == 0:
            objs = storage.all()
            str_arr = []
            for k, v in objs.items():
                str_arr.append(v.__str__())
            print(str_arr)
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for c in HBNBCommand.__classes:
                if c == arg.split()[0]:
                    break
            str_arr = []
            objs = storage.all()
            for k, v in objs.items():
                if k.split(".")[0] == c:
                    str_arr.append(v.__str__())
            print(str_arr)

    def do_update(self, arg):
        """updates obj based on args passed
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg.split()[0],
                             arg.split()[1])) not in (storage.all()).keys():
            print("** no instance found **")
        elif len(arg.split()) == 2:
            print("** attribute name missing **")
        elif len(arg.split()) == 3:
            print("** value missing **")
        else:
            argl = arg.split()
            objs = storage.all()
            obj = objs["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                type_v = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = type_v(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
