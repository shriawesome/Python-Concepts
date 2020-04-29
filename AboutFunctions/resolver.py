
# Understanding the importance of __call__ in class definition.
import socket

class Resolver:
    # Constructor for the class
    def __init__(self):
        # '_cache' Private Variable to class
        self._cache={}

    # when a normal instance call is made it can help to act it as a function.
    def __call__(self,host):
        if host not in self._cache:
            self._cache[host]=socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self,host):
        return host in self._cache

if __name__=='__main__':
    resolver=Resolver()   # Instance is created
    print("Checking if google.com is present initially")
    print(resolver.has_host('google.com'))
    print("Adding google.com")
    print(resolver('google.com'))   # __call__ makes it behave as a function
    print(resolver.has_host('google.com'))
    resolver.clear()    # clears the dictionary
    print(resolver.has_host('google.com'))
