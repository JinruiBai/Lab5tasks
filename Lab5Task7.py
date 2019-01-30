class Kangaroo(object):
    def __init__(self, name,pouch_contents = []):
        self.pouch_contents = pouch_contents
        self.name = name
        
    def put_in_pouch(self, stuff):
        self.pouch_contents.append(stuff)
    
    def __str__(self,):
        return "I have {} in my pouch".format(self.pouch_contents)
    

kanga = Kangaroo('Kanga')
roo = Kangaroo('roo')
kanga.put_in_pouch('Wallet')
kanga.put_in_pouch('car key')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)