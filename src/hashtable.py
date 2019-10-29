# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return "{'" + self.key +"': '" + self.value + "'}"

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if load rating is .7 * self.capacity:
        # run    self.resize()  ???

        # check if there is a linked list already going
        if self.storage[index]:
            # if so
            current = self.storage[index]
            while current:
                # if key exists already, overwrite it
                if current.key == key:
                    current.value = value
                    return
                # else if we are at the end of the list, create the new Node
                elif current.next == None:
                    current.next = LinkedPair(key, value)
                    return
                # else traverse the list
                else:
                    current = current.next
        # if not a list already, start a List Node
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if there is nothing in the index return a warning
        if self.storage[index] is None:
            print("Warning: key not found")
            return
        # create a few pointers to traverse the linked lists
        current = self.storage[index]
        prevNode = None
        # if there is a value at the node
        while current is not None:
            # check if the keys match
            if current.key == key:
                # if there is a previous node
                if prevNode:
                    # set it's next (current) to None
                    prevNode.next = None # is there a possible bug here with a potential next
                else:
                    self.storage[index] = None
            else:
                prevNode = current
                current = current.next
        return True


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print(f"INDEX: {index} ")
        if self.storage[index] is None:
            return None
        elif self.storage[index].key != key and self.storage[index].next:
            current = self.storage[index].next
            while current:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage
        for node in old_storage:
            if node is None:
                pass
            else:
                # print(f"resizing pair: {pair}")
                if not node.next:
                    # index = self._hash_mod(node.key)
                    # new_storage[index] = node
                    self.insert(node.key, node.value)

                else:
                    current = node.next
                    while current:
                        if not current.next:
                            # index = self._hash_mod(current.key)
                            # new_storage[index] = current
                            self.insert(node.key, node.value)
                        else:
                            current = current.next
        # self.storage = new_storage
        return



if __name__ == "__main__":
    ht = HashTable(2)
    print(ht.storage)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    print(ht.storage)

    print("")
