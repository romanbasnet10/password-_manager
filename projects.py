from cryptography.fernet import Fernet
class password_manager:
    def __init__(self):
        self.key= None
        self.passwordfile=None
        self.password_dict={}

    def create_key(self,path):
        self.key=Fernet.generate_key()
        print(self.key)
        with open(path,"wb") as f:
            f.write(self.key)

pm=password_manager()
pm.create_key("mykey.key")