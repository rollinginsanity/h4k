#This file contains the h4k class.
from h4k import opsys
from h4k import programs

import time
import random

class h4k:
    def __init__(self):
        pass

    def run(self):
        print("Test")
        osi = opsys.opsys("testpc", "test", ["billy", "bobby"], "192.168.11.1", "linux_clone")
        runtime = programs.programs(osi)
        bootup = osi.bootup()
        print(bootup['header'])
        for line in bootup['output']:
            print(line.rstrip())
            time.sleep(random.randrange(3))
        command = input(osi.prompt)
        print(runtime.runprogram(command))
        quit()

    def start(self):
        self.run()
