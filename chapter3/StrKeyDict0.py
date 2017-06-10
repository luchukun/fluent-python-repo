import collections
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        print ('missing key: %s'%key)
        return self[str(key)]
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains(self,key):
        return key in self.keys() or str(key) in self.keys()
class StrKeyDict(collections.UserDict):
    def __missing__(self,key):
        if isinstance(key, str):
            raise KeyError
        return self.data[str(key)]
    def __setitem__(self, key, item):
        self.data[str(key)] = item
    def __contains(self,key):
        return str(key) in self.data
