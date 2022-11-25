import time

import pystrix
from pystrix.ami.core import Originate_Context

_HOST = 'localhost'
_USERNAME = 'admin'
_PASSWORD = '642d10ac25fe5738a35cdeee77244cf3'

def originate(endpoint,context='from-internal',extension='s'):
    manager = pystrix.ami.Manager()
    manager.connect(_HOST)
    challenge_response = manager.send_action(pystrix.ami.core.Challenge())
    action = pystrix.ami.core.Login(
        _USERNAME, _PASSWORD, challenge=challenge_response.result['Challenge'])
    manager.send_action(action)
    manager.send_action(Originate_Context(channel=f'PJSIP/{endpoint}', context=context, extension=extension))
    manager.send_action(pystrix.ami.core.Logoff())