class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, word: str):
        value = 0
        for char in word:
            value += ord(char)
        return value
    
    def add(self, key: str, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed]={}
        self.collection[hashed][key] =value         
    
    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
            if not self.collection[hashed]:
                del self.collection[hashed]


    
    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]
        else:
            return None
