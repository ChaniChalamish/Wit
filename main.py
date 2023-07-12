import sys

from wit_interface import WitInterface

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("no command got")
    command = sys.argv[1]
    args = sys.argv[2:]
    print("args",args)

WitInterface.handle_commands(command, args)
