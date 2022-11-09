
from Modules.Cloud import Cloud

class Azure(Cloud):

    def __init__(self):
        self.url = "http://azure"
        self.token = "12345"


    def criar_vm(self):
        self.connect()
        print("Creating a Azure VM")