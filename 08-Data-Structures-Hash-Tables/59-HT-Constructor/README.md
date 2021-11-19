# 58. HT: Constructor

The code defines a **HashTable** class with a few methods.

The constructor takes as a parameter the *size* of the address space of the hash table. We simply create a list of this size and initialize every value to None.

![Hash Table Constructor](./images/hash-table-constructor.jpg?raw=true "Hash Table Constructor")

## Hash Method

Remember the hash is what we pass the key to in order to determine the address where we store the key-value pair. So clearly the hash takes the key as its parameter. 

We can see that the in the function we loop through the letters in the key and we run a mathematical function on it. Note that the *ord* function gets the ascii number for each letter. This gets multiplied by 23 which is a prime number (we could use any prime number). The key part is that the function takes the modulo (%) of the length of the `data_map`. Remember that the modulo function gives the remainder when you divide. Remember that the size is 7 so if you divide any number by 7 the remainder will be anywhere from 0 to 6 which is our address space.

![Hash Table Hash Method](./images/hash-table-hash.jpg?raw=true "Hash Table Hash Method")


## Address Scheme

Note that a hash table should always have a *prime number of addresses*. A better address scheme would be to remove the last slot so that we have 0 - 6 (i.e. 7) slots. The reason is that a prime number increases the amount of randomness for how the key-value pairs will be distributed in the hash table. In other words, it reduces the number of collisions. 
