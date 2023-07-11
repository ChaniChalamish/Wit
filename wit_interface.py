from wit import Wit


class WitInterface:
    @staticmethod
    def handle_commands(action, args):
        if action == "init":
            Wit.init()
            return
        if action == "add":
            Wit.add(args)
            return
        else:
            raise ValueError("not valid wit opt")
