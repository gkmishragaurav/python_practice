# Implementation of separate chaining collision hashtable of given size n.
# Allocate an array of size n
# Search/insert/delete option should be implemented.
# features:
# resize the hash when bucket is full.

class HashTable():
    bucket_size = 4
    total_buckets = 5
    size=0
    def __init__(self, capacity=bucket_size*total_buckets):
        self.capacity = capacity
        self.bucket=[[]]*self.total_buckets

    def hash_Function(self, key):
        return key%self.total_buckets

    def resize(self):
        self.bucket_size+=1
        self.capacity = self.bucket_size*self.total_buckets
        print(self.bucket_size, self.capacity)

    def set(self, key, value):
        hash_key = self.hash_Function(key)
        bucket = self.bucket[hash_key]
        if not bucket:
            self.bucket[hash_key] = [(key, value)]
        else:
            found = self.search_in_bucket(bucket, key)
            if found[1]:
                if found[1] != value:
                    self.bucket[hash_key].remove((key, value))
                else:
                    return
            else:
                self.bucket[hash_key].append((key, value))
                self.size+=1
                if len(self.bucket[hash_key]) == self.bucket_size:
                    self.resize()
        return 0

    def search_in_bucket(self, bucket, key):
        found=False
        for n, item in enumerate(bucket):
            if item[0] == key:
                return item
        return found, None

    def get(self, item):
        hash_key = self.hash_Function(item)
        bucket = self.bucket[hash_key]
        if bucket:
            found = self.search_in_bucket(bucket, item)
            if found[0]:
                return found[1]
        return False

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __str__(self):
        return str(self.bucket)

h = HashTable()
h[12] = 'fwgwe'
h[2] = "rgrg"
h[22] = 'rgrger'
h[32] = "rgrg"
h[42] = "rgrg"
h[52] = "rgrg"
print(h[22])
print(h.size, h.capacity, h)