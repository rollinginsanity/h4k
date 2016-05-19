#Programs used inside operating systems.
#defined as a class with functions.

class programs:
    def __init__(self, osi):
        self.osi = osi

    def ifconfig(self):
        return self.osi.network_addr

    def computer_name(self):
        return self.osi.name

    def runprogram(self, command):
        if command == "ifconfig":
            return self.ifconfig()
        if command == "computer_name":
            return self.computer_name()
