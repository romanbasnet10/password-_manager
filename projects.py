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

    def load_key(self,path):
        with open (path,"rb") as f:
            self.key=f.read()

    def create_password_file(self,path,intial_values=None):
        self.password_file=path

        if intial_values is not None:
            for key,value in initial_values.items():
                self.add_password(key,value)
    def load_password_file(self,path):
        self.password_file=path

        with open(path,"r")as f:
            for line in f:
                site,encrypted=line.split(":")
                self.password_dict[site]=fernet(self.key).decrypted(encrypted.encoded())
    
    def add_password (self,site,password):
        self.password_dict[site]=password

        if self.password_file is not None:
            with open (self.password_file,"a+")as file:
                 encrypted= fernet(self,key).encerypt(password_encode())
                 f.write(site+":"+encrypted.decode()+"\n")
    
    def get_password(self,site):
            return self.password_dict[site]