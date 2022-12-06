from .ami import Asterisk_Ami

_HOST = 'localhost'
_USERNAME = 'admin'
_PASSWORD = '642d10ac25fe5738a35cdeee77244cf3'

asterisk = Asterisk_Ami(_HOST,user=_USERNAME,password=_PASSWORD)

# asterisk.connect()