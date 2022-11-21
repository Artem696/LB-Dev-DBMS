import matplotlib.pyplot as plt
import re

class HashTable:
    def __init__(self):
        self.size = 30
        self.hashTable = [[],] * self.size

    def hash_function(self, key):
        s = 0
        res = 0
        if isinstance(key, str):
            for i in key:
                s += ord(i)**2
            res = s % len(self.hashTable)
            return res
        res = key % len(self.hashTable)
        return res

    def insert_data(self, key, data):
        index = self.hash_function(key) % len(self.hashTable)
        if not self.hashTable[index]:
            self.hashTable[index] = [key, data]
        else:
            self.hashTable[index][0] += ' ' + key 
            self.hashTable[index][1] += 1

    def print_table(self):
        print(self.hashTable)

    def plot_collisions(self):
        count_collision = []
        size = []
        for i in range(len(self.hashTable)):
            count_collision.append(self.hashTable[i][1])
        for j in range(1,31,1):
            size.append(j)
        plt.bar(size, count_collision, color='g')
        plt.show()

ht = HashTable()
input_symbols = []
s = ''
with open("Lb6\\lab_6.txt",'r',encoding = 'utf-8') as f:
    for i in f.read():
        if re.findall(r'\b\w+\b', i):
            s += i
        else:
            if re.findall(r'\b\w+\b', s):
                input_symbols.append(s)
                s = ''

for i in input_symbols:
    ht.insert_data(str(i), 0)

#print(input_symbols)
ht.print_table()
ht.plot_collisions()


