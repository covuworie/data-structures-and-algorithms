# 56. Hash Table: Intro

To demonstrate the hash table we will create a hardware store with items and their quantity. However, before we create one let's look at the built-in hash table that python has. 

## Dictionaries

Python already has a built-in hash table -  a **dictionary**.

```
{"nails": 1000}
```

Dictionaries contain a *key - value pair*. In this example, *nails* is the *key* and *1000* is the *value*.

## How Does a Hash Table Work?

The way a hash table works is it uses a mathematical function called a *hash function* (or *hash method*). The hash is performed on the key.

![Hash Table Input](./images/hash-table-input.jpg?raw=true "Hash Table Input")

In addition to getting the key-value pair back from the hash function it also produces an address.

![Hash Table Output](./images/hash-table-output.jpg?raw=true "Hash Table Output")

The key-value pair is then stored at that address in the hash table.

![Hash Table Output Store](./images/hash-table-output-store.jpg?raw=true "Hash Table Output Store")

This is how a dictionary is stored.

## Characteristics of the hash function

The hash function is:

1. *One-way*. It takes the key and produces the address. However, it cannot take the address and reproduce the key.
2. *Deterministic*. For a particular hash function and given input we always get the same address.

## How will we create a hash table?

Even though python includes dictionaries, we will be building our own hash table. We will create our own address space by creating a list. Then we will create methods such as `set_item(key, value)`. We will also create our own method to hash the key. The key-value pair will be a list and the hash will produce an address. At this address in our list we will store the key-value pair. It is possible to have an address collision. We will store multiple values at the same address and later we will talk about how we deal with this. e.g. `set_item('nails', 1000) ` creates the first item at address 2.

![Hash Table Store](./images/hash-table.jpg?raw=true "Hash Table Store")

We will also have a `get_item(key)` method where we will run the key through the hash. Because the hash is deterministic we will get the same address back. We can go directly to this address in the hash table to retrieve the value. e.g. `get_item('bolts')` will give 4 and the value at that address will be 1400.

## What is a hash table?

A **hash table** is a data structure that is used to store *key-value pairs*. It uses a *hash function* to compute an index into an array in which an element will be inserted or searched.
