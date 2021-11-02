# 59. HT: Set

The `set_item` method takes a key and a value as its parameters and inserts the key-value pair at the hash table address location produced by running the key through the hash method.

From the code we can see that it first computes the hash to find the address location (i.e index) in the hash table.

![Hash Table Set Hash](./images/hash-table-set-hash.jpg?raw=true "Hash Table Set Hash")

Next, the code initializes the hash table at that index to an empty list (to allow separate chaining for collisions) in the situation where there is no list at that index.

![Hash Table Set Empty List](./images/hash-table-set-empty-list.jpg?raw=true "Hash Table Set Empty List")

Finally the code inserts the value-pair at that index in the hash table.

![Hash Table Set Key Value](./images/hash-table-set-key-value.jpg?raw=true "Hash Table Set Key Value")

Below is how the hash table looks for multiple items as in the test cases in the code.

![Hash Table Set Key Value Multiple](./images/hash-table-set-key-value-multiple.jpg?raw=true "Hash Table Set Key Value Multiple")
