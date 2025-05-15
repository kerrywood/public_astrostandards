# the harnesses point at either the .so or the .dll... 
import platform
import ctypes

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

#############################################################################
# must be loaded after the Dll loads above (they are used by the libs)
#############################################################################

# helpers that you might need
from .V95.utils import helpers 

# -----------------------------------------------------------------------------------------------------
def Cstr( S, slen=128 ):
    stbuf = ctypes.create_string_buffer( slen )
    stbuf.value = S.encode()
    return stbuf

# -----------------------------------------------------------------------------------------------------
def get_last_errmsg( ):
    stbuf = ctypes.create_string_buffer( 128 )
    DllMainDll.GetLastErrMsg( stbuf )
    return stbuf.value.decode('utf-8')

# -----------------------------------------------------------------------------------------------------
def init_main( logfile='aslog.txt', verbose=True ):
    ptr = DllMainDll.DllMainInit()
    if logfile: DllMainDll.OpenLogFile( Cstr( logfile, 512) )
    return ptr
# =====================================================================================================
FUNC_ORDER = (
    EnvConstDll.EnvInit,
    TimeFuncDll.TimeFuncInit,
    AstroFuncDll.AstroFuncInit,
    TleDll.TleInit,
    SpVecDll.SpVecInit,
    VcmDll.VcmInit,
    ExtEphemDll.ExtEphInit,
    Sgp4PropDll.Sgp4Init,
    SatStateDll.SatStateInit,
    SensorDll.SensorInit,
    ObsDll.ObsInit,
)

# -----------------------------------------------------------------------------------------------------
def init_all( logfile='aslog.txt', verbose=False ):
    ptr = DllMainDll.DllMainInit()
    if verbose: 
        print('--- INITIALIZING DLLs ---')
        print('{:20}   : {}'.format( 'DllMainInit', ptr ) )
    if logfile: DllMainDll.OpenLogFile( Cstr( logfile, 512) )
    for F in FUNC_ORDER:
        rv = F( ptr )
        if verbose: print('{:20}   : {}'.format( F.__name__, rv ) )
        assert rv == 0
    return ptr

# -----------------------------------------------------------------------------------------------------
def get_versions( ):
    glob = globals()
    dll  = list( filter( lambda X: X.endswith('Dll'), glob ) )
    vstr = Cstr('',128)
    for D in dll:
        lib  = glob[D]
        info = list(filter( lambda X : 'GetInfo' in X, dir(lib) ) )
        if len(info) == 0: 
            print('{:30} no version function found'.format(D))
            continue
        vfc = getattr( lib, info[0] )
        vfc( vstr )
        print('{:30}  {}'.format( D, vstr.value.decode('utf-8')))

# =====================================================================================================
if __name__ == "__main__":
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    # some dates checks
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    ptr = init_all()
    test_dates() 
    get_versions()
