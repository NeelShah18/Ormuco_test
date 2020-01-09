import collections

class LRUCache:
    def __init__(self, capacity):
        '''
        capacity: It is capacity of orderdict
        '''
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        '''
        Use to get value of specific key.
        '''
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        '''
        Use to set key and it's value.
        '''
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

'''
Here we are using collection and order dictonary to increase performance as the this should be geo located LRU, so time 
sould be minimum and performance should be acceptable in real-time as it took only 0.1 sec to perform task.

Use:
geocache = LRUCach(1000)
geocache.set(1, 1);
geocache.set(2, 2);
geocache.get(1);       // returns 1
geocache.set(3, 3);    // evicts key 2
geocache.get(2);       // returns -1 (not found)
geocache.set(4, 4);    // evicts key 1
geocache.get(1);       // returns -1 (not found)
geocache.get(3);       // returns 3
geocache.get(4);       // returns 4
'''