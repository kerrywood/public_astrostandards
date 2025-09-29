if __name__ == '__main__':
    # the harnesses point at either the .so or the .dll... 
    import platform
    import ctypes
    import glob
    import sys
    import os
    import shutil

    SUFFIX = None
    if platform.system() == 'Linux':
        SUFFIX = "*.so"

    if platform.system() == 'Windows':
        SUFFIX = "*.dll"

    if len(sys.argv) < 2:
        print('*'*100)
        print('Usage')
        print('{} <path with libraries>'.format(sys.argv[0]))
        print('*'*100)
        sys.exit(1)

    if SUFFIX is None:
        print('Only support windows and linux for now.')
        print(' you are running on {}'.format( platform.system() ) )
        sys.exit(1)

    # make sure they passed in a directory
    INDIR = sys.argv[1]
    assert os.path.isdir( INDIR )

    DESTDIR = os.path.dirname( os.path.abspath(__file__) )
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # set your paths here
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if platform.system() == 'Linux':
        DESTDIR = os.path.join( DESTDIR, 'V96','linux' )
    if platform.system() == 'Windows':
        DESTDIR = os.path.join( DESTDIR, 'V96','win' )

    print('Your architecture is          : {}'.format( platform.system() ) )
    print('Looking for files with suffix : {}'.format( SUFFIX ) )
    print('Looking in                    : {}'.format( INDIR ) )
    print('Will copy to                  : {}'.format( DESTDIR ) )
    print()
    
    FILES = sorted( glob.glob( os.path.join(INDIR,SUFFIX) ) )
    print('Found the following dlls : ')
    for f in FILES: print('\t{}'.format(f))

     
    print()
    for f in FILES:
        rv = shutil.copy( f, DESTDIR )
        print('Copying {}, returned : {}'.format( f, rv ))

