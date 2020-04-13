class LRU:
    websiteName = ''
    url = ''
    date=''
    def __init__(self, w, u,d): 
        self.websiteName = w 
        self.url=u
        self.date=d
    def put(self,a):
        return 'done'
    def get(self):
        pass
    def get_cache(self):
        pass
