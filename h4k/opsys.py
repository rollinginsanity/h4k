#The Operating System class, simulates a computer.
import os

class opsys:
    def __init__(self, directory, name, users, network_address, os_type):
        self.directory = "os/"+directory
        self.name = name
        self.users = users
        self.network_addr = network_address
        self.os_type = os_type
        self.prompt = self.name+"> "

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)


    def __repr__(self):
        return self.name+" at "+self.network_addr

    def bootup(self):
        bootup_txt = open("h4k/boot-types/"+self.os_type+".txt")
        bootup_header = open("h4k/boot-types/"+self.os_type+"-header.txt").read()
        return {"header": bootup_header, "output": bootup_txt}

    def prompt(self):
        return self.prompt
