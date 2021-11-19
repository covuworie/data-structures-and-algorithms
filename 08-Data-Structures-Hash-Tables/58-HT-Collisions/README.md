# 57. HT: Collisions

## What is a Hash Collision

A **hash collision** occurs when an attempt is made to place a key-value pair at an address where there is already a key-value pair.

![Hash Table Collision](./images/hash-table-collision.jpg?raw=true "Hash Table Collision")

## How are Collisions Dealt With?

How do we place a key-value pair when a collision occurs without overriding the value stored at that address space? There are the following two techniques.

1. **Separate Chaining**. The key value pairs at an address location are stored within another list. This is the approach we will be taking.

```
[ ['nails', 1000], ['nuts', 1200]]
```

Another way of doing separate chaining is to use linked lists instead of lists. 

![Hash Table Separate Chaining](./images/hash-table-separate-chaining.jpg?raw=true "Hash Table Separate Chaining")

2. **Linear Probing** is one form of *open addressing*. In this method you go down the hash table until you find the first available address and store the key-value pair there. This makes sure there is no more than one key-value pair at any address.

![Hash Table Linear Probing](./images/hash-table-linear-probing.jpg?raw=true "Hash Table Linear Probing")
