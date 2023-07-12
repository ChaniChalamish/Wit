from wit import Wit


class WitInterface:
    @staticmethod
    def handle_commands(action, args):
        wit_instance = Wit.create_instance()
        if action == "init":
            wit_instance.init()
            return
        if action == "add":
            wit_instance.add(args)
            return
        if action == "commit":
            wit_instance.commit(args)
            return
        else:
            raise ValueError("not valid wit opt")
