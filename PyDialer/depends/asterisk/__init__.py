from .ami import Asterisk_Ami

_HOST = 'localhost'
_USERNAME = 'Pydialer'
_PASSWORD = 'admin123'

asterisk = Asterisk_Ami(_HOST,user=_USERNAME,password=_PASSWORD)

#asterisk.connect()
print("manager got connected :",asterisk.is_alive())