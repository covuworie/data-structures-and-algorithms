# 62. HT: Big O

## What is Big O for the Hash Table methods?

To figure out Big O for the hash table methods let's look at the following hash table. It uses linked lists instead of lists as this is visually easier to look at.

![Hash Table Linked List](./images/hash-table-linked-list.jpg?raw=true "Hash Table Linked List")

Since the `get_item` and `set_item` methods use the hash method, we need to know what Big O is for the hash method.

### What is Big O for the Hash Method?

For a given key of a fixed size (i.e. certain number of letters), it will always be the same number of operations to calculate the hash. This means that the hash method itself is O(1).

![Hash Table Hash Method O(1)](./images/hash-table-hash-method-O(1).jpg?raw=true "Hash Table Hash Method O(1)")

## What is Big O for Set?

Let's say we wish to do `set_item('washers', 1000)`, then we run the key through the hash method and it will produce the address 2. Then we will append that on to the end of the linked list. This is also O(1).

![Hash Table Set Method O(1)](./images/hash-table-set-method-O(1).jpg?raw=true "Hash Table Set Method O(1)")

## What is Big O for Get?

Let's say we wish to do `get_item('screws')`, then we run the key through the hash method and it will produce the address 6. Then it will take us one operation to find the value. This is also O(1).

![Hash Table Get Method O(1)](./images/hash-table-get-method-O(1).jpg?raw=true "Hash Table Get Method O(1)")

However, what if our hash table looks like this?

![Hash Table Get Method O(n)](./images/hash-table-get-method-O(n).jpg?raw=true "Hash Table Get Method O(n)")

Then we need to iterate through the list until we get to the value that we want. This would be O(n). So it would seem to be that the worse case scenario is having all the items put at the same address.

But the assumption with a hash table is that the distribution is going to be more like this.

![Hash Table Distribution](./images/hash-table-distribution.jpg?raw=true "Hash Table Distribution")

Even with the very primitive hash method that we created, it gave us a very good distribution of the items. The hash method that is built into python is going to be even more efficient at distributing the items. Also it will be dealing with a much larger address space so collisions will be fairly rare.

So for all intents and purposes, hash tables are O(1) for both inserting an element and looking up a value by key.

## What is Big O for Keys?

Clearly this is O(n) since we have to loop through the address space to return the keys. The same would be true for a method which returns the key-value pairs.
