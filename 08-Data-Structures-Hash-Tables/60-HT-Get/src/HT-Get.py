from typing import Union

class HashTable:
    def __init__(self, size: int = 7) -> None:
        self.data_map = [None] * size
      
    def __hash(self, key: str) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self) -> None:
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key: str, value: int) -> None:
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key: str) -> Union[int, None]:
        index = self.__hash(key)
        kv_pairs = self.data_map[index]
        for kv_pair in kv_pairs if kv_pairs else []:
            if not kv_pair[0] == key:
                continue
            return kv_pair[1]
        return None
             

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

