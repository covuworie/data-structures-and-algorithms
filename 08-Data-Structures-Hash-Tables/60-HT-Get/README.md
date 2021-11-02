# 60. HT: Get

The `get_item` method takes a key as its parameter and returns the value in the hash table associated with that key.

We have two scenarios. 

1. The key exists, e.g. washers. We will run this through the hash which will give the address 4. We will go that address in the hash table and loop through the key-value pairs to find the key. We will return the value at that key 50.

![Hash Table Get](./images/hash-table-get.jpg?raw=true "Hash Table Get")

2. The key does not exist, e.g. lumber. We will run this through the hash which will give the address 6. We will go that address in the hash table and see the value does not exist. We will return None in this scenario.

You can clearly see these two scenarios in the code.
