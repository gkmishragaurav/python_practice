class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.bucket = [[]] * self.size

    def hash_function(self, key):
        return key % 10000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = self.hash_function(key)
        self.bucket[hash_key] = [key, value]

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = self.hash_function(key)
        if self.bucket[hash_key]:
            if self.bucket[hash_key][0] == key:
                return self.bucket[hash_key][1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = self.hash_function(key)
        if self.bucket[hash_key]:
            if self.bucket[hash_key][0] == key:
                self.bucket[key] = []

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
