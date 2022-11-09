
from Modules.Cloud import Cloud

# entender object 
class GCP(Cloud):

    def __init__(self):
        self.url = "http://gcp"
        self.token = "12345"

    #entender self
    def criar_vm(self):
        self.connect()
        print("Creating a CGP VM")

