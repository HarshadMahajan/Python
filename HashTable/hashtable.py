class HashTable:
    """
        HasTable : Key-value MAP/Associative Array
        Operations:
            put(key, value)
            get(key)
    """

    def __init__(self):
        """
            Define an empty hashtable.
            we use lists to implement an has table
        """
        self._size = 4
        self._table = [None] * self._size
    
    def hash_function(self, key):
        return key % self._size
    
    def put(self, key, value):
        """
            Add a key-value pair into the hash table
            :param key: key is item used to calculate the hash
            :param value: Actual value stored in the slot
        """

        if self.utilization >= 0.75:
            self._resize()
        
        slot = self.hash_function(key)

        # do a linear probe until a slot is found in case of collision
        if self._table[slot] is not None and self._table[slot][0] != key:
            slot = self._find_slot(slot, key)
        
        self._table[slot] = (key, value)

    
    def get(self, key):
        """
            Return the value for a particular key.
            :param key: key for which value is returned
            :return: value corresponding to the key
        """
        slot = self.hash_function(key)

        # Do a linear probe until a lot is found in case of collision
        if self._table[slot][1]
