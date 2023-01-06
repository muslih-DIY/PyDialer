from typing import Callable,Dict
from pystrix import ami
from pystrix.ami import core

class Error(Exception):
    "base exception for this class"

class ConnectionError(Error):
    "connection related"

class Asterisk_Ami():
    """
    _manager = pystrix.ami.manager 

    _kill_flag => True says connection lost [core shutdown/manually closed/network issue etc..]

    usage:
    -------------

    asterisk = Asterisk_Ami()

    asterisk.regiser_call_back({
            'Shutdown' : self._handle_shutdown,
            })
            
    asterisk.connect()

    """

    _manager:ami.Manager = None
    _kill_flag:bool = False
    _call_back_register : Dict[str,Callable] = {}

    def __init__(self,host='localhost',port:int = 5038,user='admin',password='admin321') -> None:
        self._host = host
        self._port = port
        self._password = password   
        self._user = user
        self._manager = ami.Manager()
        self.regiser_call_back({
            'Shutdown' : self._handle_shutdown,
            'FullyBooted':self._handle_booting
            })

    
    def regiser_call_back(self,callbacks:dict):
        "regiser callback on ami event to function"
        [
            self._manager.register_callback(event,handler) 
            for event,handler in callbacks.items()
            ]


    def connect(self):
        " Run for connecting to the asterisk"
        try:
            self._manager.connect(self._host,self._port)
            challenge_response = self._manager.send_action(core.Challenge())
            if challenge_response and challenge_response.success:
                log_action = core.Login(
                    self._user,
                    self._password,
                    challenge=challenge_response.result['Challenge']
                    )
                self._manager.send_action(log_action)
            else:
                self._kill_flag = True
                raise ConnectionError(
                    "Asterisk did not provide an MD5 challenge token"+
                    (challenge_response is None and ': timed out' or '')
                    )
        except ami.ManagerSocketError as e:
            self._kill_flag = True
            raise ConnectionError("Unable to connect to Asterisk server: %(error)s" % {
             'error': str(e),
            })
        except ami.core.ManagerAuthError as reason:
            self._kill_flag = True
            raise ConnectionError("Unable to authenticate to Asterisk server: %(reason)s" % {
             'reason': reason,
            })
        except ami.ManagerError as reason:
            self._kill_flag = True
            raise ConnectionError("An unexpected Asterisk error occurred: %(reason)s" % {
             'reason': reason,
            })
        self._manager.monitor_connection()
    
    def _handle_shutdown(self):
        self._kill_flag = True

    def _handle_booting(self):
        self._kill_flag = False

    def is_alive(self):
        return not self._kill_flag

    def close(self):
        self._manager.close()


    def Originate(
        self,channel: str, context: str,extension: str,
        priority: int=1,timeout = None,callerid: str = None,
        variables: dict = {},account: str = None,async_: bool = True):
        "originate a call to extension and join to another extension"
        return self._manager.send_action(
            core.Originate_Context(channel,context,extension,priority,timeout,callerid,variables,account,async_)
            )

        
