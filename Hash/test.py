# -*- coding: utf-8 -*-

"""

"""

import random
import string

class HashTable:
    def __init__(self):
        self.size = 12
        self.max_prime_under_size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def _hash_function(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.max_prime_under_size

    def add(self, key, data):
        hash_value = self._hash_function(key)

        if self.slots[hash_value] is None: #
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key: # same key with new data = replace
                self.data[hash_value] = data
            else: # collision = different key with same hash value
                new_hash_value = self._re_hash_function(hash_value)
                while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                    new_hash_value = self._re_hash_function(new_hash_value)

                if self.slots[new_hash_value] is None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = data
                else:
                    self.data[new_hash_value] = data  # replace

    def _re_hash_function(self, old_hash):
        return (old_hash + 1) % self.size

    def get(self, key):
        hash_value = self._hash_function(key)
        init_hash_value = hash_value

        data = None
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                data = self.data[hash_value]
                break
            else:
                hash_value = self._re_hash_function(hash_value)
                if init_hash_value == hash_value:
                    break
        return data

def main():
    myHashTable = HashTable()
    data_to_hash = dict()

    for i in range(10):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        value = i + 1
        data_to_hash[key] = value
        myHashTable.add(key, value)

    print('Data to Hash:', data_to_hash)
    print('Hash Table Slots:', myHashTable.slots)
    print('Hash Table Data Set:', myHashTable.data)
    print([myHashTable.get(key) for key in data_to_hash])

if __name__ == '__main__':
    main()
