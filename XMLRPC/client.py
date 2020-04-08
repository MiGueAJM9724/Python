from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:20064', allow_none=True)
s.set('lenguaje', 'python')
s.set('version', '3.7.7')
s.keys()
