from typing import List, Union

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
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key: str) -> Union[int, None]:
        index = self.__hash(key)
        kv_pairs = self.data_map[index]
        for (pair_key, pair_value) in kv_pairs if kv_pairs else []:
            if not pair_key == key:
                continue
            return pair_value
        return None

    def keys(self) -> List[str]:
        all_keys = []
        for entry in self.data_map:
            for key, _ in entry if entry else []:
                all_keys.append(key) 
        return all_keys
        

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())

