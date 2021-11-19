# 61. HT: Keys

The `keys` method simply returns a list of keys present in the hash table. We can see that we will need two for loops. One that loops through the addresses in the hash table checking if there is any data there.

![Hash Table Keys Address Loop](./images/hash-table-keys-address-loop.jpg?raw=true "Hash Table Keys Address Loop")

When data is found, then there will be another loop that loops through the key-value pairs and extracts the keys.

![Hash Table Keys Key Values Loop](./images/hash-table-keys-key-values-loop.jpg?raw=true "Hash Table Keys Key Values Loop")

The keys will be inserted into a list that is returned from the function. You can clearly see all of this in the code.
