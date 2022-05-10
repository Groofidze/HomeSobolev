import socket
from .base import *

ip = socket.gethostbyname(socket.gethostname())

if ip == '194.67.119.141':
    from .production import *
else:
    from .developer import *
