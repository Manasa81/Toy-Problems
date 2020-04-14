from queue import Queue 
  
# Initializing a queue 
class LRU:
    url = ''
    date=''
    l=[]
    q = Queue(maxsize = 3) 
    def __init__(self, u,d): 
        self.url=u
        self.date=d
    def put(self,url):
        if len(self.l) == 3:
            self.l.pop(0)
        self.l.append(url)
        return 'done'
    def get(self):
        return len(self.l) == 3
    def get_cache(self):
        return self.l
# o = LRU('a',1)
# o.put('a')
# o.put('b')
# o.put('c')
# o.put('d')

# print(o.get())
# print(o.get_cache())




