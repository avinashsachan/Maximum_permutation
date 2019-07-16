import json
try:
    from Queue import Queue
except:
    from queue import Queue

class MaximumCombination():

    def __init__(self, keys, value):
        self.values = value
        self.keys = keys
        self.js = {}
        self._testValueError()

    def _genStairCaseFull(self,j, q):
        k = q.get()
        if k not in j:
            j[k] = {}
        if q.qsize() > 0:
            self._genStairCaseFull(j[k], q)

    def getHash(self):

        self.js = {}
        for ky in self.keys:
            q = Queue()
            for k in ky.split("."):
                q.put(k)
            self._genStairCaseFull(self.js, q)

        return self.js


    def getValueHash(self):

        self.js = self.getHash()
        self._pushParameter(self.js)
        self.js["total"] = 0
        return self.js

    def _pushParameter(self,js):
        if len(js) == 0:
            js["total"] = 0
        else:
            for k in js:
                self._pushParameter(js[k])
                ks = json.dumps(js[k])

                n = {}
                for x in self.values[k]:
                    n[x] = json.loads(ks)
                    n[x]["total"] = 0

                js[k] = n
                js[k]["total"] = 0

    def _testValueError(self):

        for s in self.keys:
            for i in s.split('.'):
                if i not in self.values:
                    print(i, " not in values")
                    raise Exception("value not found")

