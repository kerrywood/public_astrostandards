# the harnesses point at either the .so or the .dll... 
import platform
import ctypes

# init helpers (init_all is deprecated, but it helps with debugging)
from .V95.utils.load_utils import init_all, get_versions, get_last_errmsg

# helpers that you might need
from .V95.utils import helpers 

if platform.system() == 'Linux':
    from .V95.linux import AstroFuncDll
    from .V95.linux import DllMainDll
    from .V95.linux import ElOpsDll
    from .V95.linux import EnvConstDll
    from .V95.linux import ExtEphemDll
    from .V95.linux import ObsDll
    from .V95.linux import SatStateDll
    from .V95.linux import SensorDll
    from .V95.linux import Sgp4PropDll
    from .V95.linux import SpVecDll
    from .V95.linux import TimeFuncDll
    from .V95.linux import TleDll
    from .V95.linux import VcmDll


if platform.system() == 'Windows':
    from .V95.win import AstroFuncDll
    from .V95.win import DllMainDll
    from .V95.win import ElOpsDll
    from .V95.win import EnvConstDll
    from .V95.win import ExtEphemDll
    from .V95.win import ObsDll
    from .V95.win import SatStateDll
    from .V95.win import SensorDll
    from .V95.win import Sgp4PropDll
    from .V95.win import SpVecDll
    from .V95.win import TimeFuncDll
    from .V95.win import TleDll
    from .V95.win import VcmDll
    