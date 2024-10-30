class File:
    def __init__(self):
        self.file=[]
    def est_vide(self):
        if self.file:
            return False
        else:
            return True
    def enfiler(self,x):
        self.file.insert(0,x)
    def defiler(self):
        return self.file.pop(-1)
    def contenue(self):
        return self.file
    def bout_file(self):
        return self.file[-1]
    def changement_file(self,fileBase):
        self.enfiler(fileBase.defiler())
"""
file1=File()
file2=File()
print(file1.est_vide())
file1.enfiler(9)
file1.enfiler(5)
file1.enfiler(8)
file1.enfiler(7)
print(file1.defiler())
print(file1.file)

file2.changement_file(file1)

print(file1.file,file2.file)
"""
