# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return "{'" + self.key +"': '" + self.value + "'} "

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
        # check if there is a linked list already going
        if self.storage[index] is not None:
            # if so set pointers to track if key is present already
            current = self.storage[index]
            exists = False
            while current and not exists:
                # if key exists already, overwrite it
                if current.key == key:
                    current.value = value
                    exists = True
                # else if we are at the end of the list, create the new Node
                elif current.next == None:
                    current.next = LinkedPair(key, value)
                    exists = True
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
        # if there is nothing in the index return a warning
        index = self._hash_mod(key)
        if self.storage[index] == None:
            print("No value for that key!")
            return
        # create a few pointers to traverse the linked lists
        current = self.storage[index]
        prevNode = None
        # # if there is a value at the node
        while current != None:
            # check if the keys match
            if current.key == key:
                # if there is a previous node
                if prevNode:
                    # set it's next (current) to None, possible bug if there is a next node
                    prevNode.next = None
                else:
                    self.storage[index] = None
                current = None

            else:
                prevNode = current
                current = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        # check if node exists
        if node:
            current = self.storage[index]
            # if it does
            while current != None:
                # check if there is a key matching existing key
                if current.key == key:
                    # if so, overwrite value
                    return current.value
                else:
                    # if not keep traversing linked list
                    current = current.next
            # if reach end of list, value wasn't found
            return None
        # if no node, value doesn't exist
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Double capacity
        self.capacity *= 2
        # create new list with size `capacity`
        new_storage = [None] * self.capacity
        # copy old storage
        old_storage = self.storage
        # set new list to storage
        self.storage = new_storage
        # iterate through old storage list
        for node in old_storage:
            if node is not None:
                # track current position
                current = node
                # iterate through linked list
                while current != None:
                    # insert new node of current value
                    self.insert(current.key, current.value)
                    # move to next node
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(2)
    print(ht.storage)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.storage)

    print("")
