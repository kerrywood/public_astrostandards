r"""Wrapper for new_SpVecDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . --compile-libdir=/opt/openastrostandards_v96 -l libspvec.so ./new_SpVecDll.h -o ./SpVecDll.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['/opt/openastrostandards_v96']

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libspvec.so"] = load_library("libspvec.so")

# 1 libraries
# End libraries

# No modules

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 23
if _libs["libspvec.so"].has("SpVecInit", "cdecl"):
    SpVecInit = _libs["libspvec.so"].get("SpVecInit", "cdecl")
    SpVecInit.argtypes = [c_int64]
    SpVecInit.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 29
if _libs["libspvec.so"].has("SpVecGetInfo", "cdecl"):
    SpVecGetInfo = _libs["libspvec.so"].get("SpVecGetInfo", "cdecl")
    SpVecGetInfo.argtypes = [c_char * int(128)]
    SpVecGetInfo.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 40
if _libs["libspvec.so"].has("SpVecLoadFile", "cdecl"):
    SpVecLoadFile = _libs["libspvec.so"].get("SpVecLoadFile", "cdecl")
    SpVecLoadFile.argtypes = [c_char * int(512)]
    SpVecLoadFile.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 51
if _libs["libspvec.so"].has("SpVecSaveFile", "cdecl"):
    SpVecSaveFile = _libs["libspvec.so"].get("SpVecSaveFile", "cdecl")
    SpVecSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    SpVecSaveFile.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 58
if _libs["libspvec.so"].has("SpVecRemoveSat", "cdecl"):
    SpVecRemoveSat = _libs["libspvec.so"].get("SpVecRemoveSat", "cdecl")
    SpVecRemoveSat.argtypes = [c_int64]
    SpVecRemoveSat.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 63
if _libs["libspvec.so"].has("SpVecRemoveAllSats", "cdecl"):
    SpVecRemoveAllSats = _libs["libspvec.so"].get("SpVecRemoveAllSats", "cdecl")
    SpVecRemoveAllSats.argtypes = []
    SpVecRemoveAllSats.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 70
if _libs["libspvec.so"].has("SpVecGetCount", "cdecl"):
    SpVecGetCount = _libs["libspvec.so"].get("SpVecGetCount", "cdecl")
    SpVecGetCount.argtypes = []
    SpVecGetCount.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 79
if _libs["libspvec.so"].has("SpVecGetLoaded", "cdecl"):
    SpVecGetLoaded = _libs["libspvec.so"].get("SpVecGetLoaded", "cdecl")
    SpVecGetLoaded.argtypes = [c_int, POINTER(c_int64)]
    SpVecGetLoaded.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 89
if _libs["libspvec.so"].has("SpVecAddSatFrLines", "cdecl"):
    SpVecAddSatFrLines = _libs["libspvec.so"].get("SpVecAddSatFrLines", "cdecl")
    SpVecAddSatFrLines.argtypes = [c_char * int(512), c_char * int(512)]
    SpVecAddSatFrLines.restype = c_int64

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 96
if _libs["libspvec.so"].has("SpVecAddSatFrLinesML", "cdecl"):
    SpVecAddSatFrLinesML = _libs["libspvec.so"].get("SpVecAddSatFrLinesML", "cdecl")
    SpVecAddSatFrLinesML.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int64)]
    SpVecAddSatFrLinesML.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 113
if _libs["libspvec.so"].has("SpVecAddSatFrFields", "cdecl"):
    SpVecAddSatFrFields = _libs["libspvec.so"].get("SpVecAddSatFrFields", "cdecl")
    SpVecAddSatFrFields.argtypes = [c_double * int(3), c_double * int(3), c_char, c_int, c_char * int(8), c_char * int(17), c_int, c_int, c_double, c_double, c_double, c_char * int(5)]
    SpVecAddSatFrFields.restype = c_int64

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 130
if _libs["libspvec.so"].has("SpVecAddSatFrFieldsML", "cdecl"):
    SpVecAddSatFrFieldsML = _libs["libspvec.so"].get("SpVecAddSatFrFieldsML", "cdecl")
    SpVecAddSatFrFieldsML.argtypes = [c_double * int(3), c_double * int(3), c_char, c_int, c_char * int(8), c_char * int(17), c_int, c_int, c_double, c_double, c_double, c_char * int(5), POINTER(c_int64)]
    SpVecAddSatFrFieldsML.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 147
if _libs["libspvec.so"].has("SpVecUpdateSatFrFields", "cdecl"):
    SpVecUpdateSatFrFields = _libs["libspvec.so"].get("SpVecUpdateSatFrFields", "cdecl")
    SpVecUpdateSatFrFields.argtypes = [c_int64, c_double * int(3), c_double * int(3), c_char, c_char * int(8), c_int, c_int, c_double, c_double, c_double, c_char * int(5)]
    SpVecUpdateSatFrFields.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 176
if _libs["libspvec.so"].has("SpVecGetField", "cdecl"):
    SpVecGetField = _libs["libspvec.so"].get("SpVecGetField", "cdecl")
    SpVecGetField.argtypes = [c_int64, c_int, c_char * int(512)]
    SpVecGetField.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 186
if _libs["libspvec.so"].has("SpVecSetField", "cdecl"):
    SpVecSetField = _libs["libspvec.so"].get("SpVecSetField", "cdecl")
    SpVecSetField.argtypes = [c_int64, c_int, c_char * int(512)]
    SpVecSetField.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 204
if _libs["libspvec.so"].has("SpVecGetAllFields", "cdecl"):
    SpVecGetAllFields = _libs["libspvec.so"].get("SpVecGetAllFields", "cdecl")
    SpVecGetAllFields.argtypes = [c_int64, c_double * int(3), c_double * int(3), String, POINTER(c_int), c_char * int(8), c_char * int(17), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_char * int(5)]
    SpVecGetAllFields.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 223
if _libs["libspvec.so"].has("SpVecParse", "cdecl"):
    SpVecParse = _libs["libspvec.so"].get("SpVecParse", "cdecl")
    SpVecParse.argtypes = [c_char * int(512), c_char * int(512), c_double * int(3), c_double * int(3), String, POINTER(c_int), c_char * int(8), c_char * int(17), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_char * int(5)]
    SpVecParse.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 233
if _libs["libspvec.so"].has("SpVecLinesToArray", "cdecl"):
    SpVecLinesToArray = _libs["libspvec.so"].get("SpVecLinesToArray", "cdecl")
    SpVecLinesToArray.argtypes = [c_char * int(512), c_char * int(512), c_double * int(512), c_char * int(512)]
    SpVecLinesToArray.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 241
if _libs["libspvec.so"].has("SpVecGetLines", "cdecl"):
    SpVecGetLines = _libs["libspvec.so"].get("SpVecGetLines", "cdecl")
    SpVecGetLines.argtypes = [c_int64, c_char * int(512), c_char * int(512)]
    SpVecGetLines.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 260
if _libs["libspvec.so"].has("SpVecFieldsToLines", "cdecl"):
    SpVecFieldsToLines = _libs["libspvec.so"].get("SpVecFieldsToLines", "cdecl")
    SpVecFieldsToLines.argtypes = [c_double * int(3), c_double * int(3), c_char, c_int, c_char * int(8), c_char * int(17), c_int, c_int, c_double, c_double, c_double, c_char * int(5), c_char * int(512), c_char * int(512)]
    SpVecFieldsToLines.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 270
if _libs["libspvec.so"].has("SpVecArrayToLines", "cdecl"):
    SpVecArrayToLines = _libs["libspvec.so"].get("SpVecArrayToLines", "cdecl")
    SpVecArrayToLines.argtypes = [c_double * int(512), c_char * int(512), c_char * int(512), c_char * int(512)]
    SpVecArrayToLines.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 277
if _libs["libspvec.so"].has("SpVecGetSatKey", "cdecl"):
    SpVecGetSatKey = _libs["libspvec.so"].get("SpVecGetSatKey", "cdecl")
    SpVecGetSatKey.argtypes = [c_int]
    SpVecGetSatKey.restype = c_int64

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 284
if _libs["libspvec.so"].has("SpVecGetSatKeyML", "cdecl"):
    SpVecGetSatKeyML = _libs["libspvec.so"].get("SpVecGetSatKeyML", "cdecl")
    SpVecGetSatKeyML.argtypes = [c_int, POINTER(c_int64)]
    SpVecGetSatKeyML.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 292
if _libs["libspvec.so"].has("SpVecFieldsToSatKey", "cdecl"):
    SpVecFieldsToSatKey = _libs["libspvec.so"].get("SpVecFieldsToSatKey", "cdecl")
    SpVecFieldsToSatKey.argtypes = [c_int, c_char * int(20)]
    SpVecFieldsToSatKey.restype = c_int64

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 300
if _libs["libspvec.so"].has("SpVecFieldsToSatKeyML", "cdecl"):
    SpVecFieldsToSatKeyML = _libs["libspvec.so"].get("SpVecFieldsToSatKeyML", "cdecl")
    SpVecFieldsToSatKeyML.argtypes = [c_int, c_char * int(20), POINTER(c_int64)]
    SpVecFieldsToSatKeyML.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 307
if _libs["libspvec.so"].has("SpVecAddSatFrArray", "cdecl"):
    SpVecAddSatFrArray = _libs["libspvec.so"].get("SpVecAddSatFrArray", "cdecl")
    SpVecAddSatFrArray.argtypes = [c_double * int(512), c_char * int(512)]
    SpVecAddSatFrArray.restype = c_int64

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 314
if _libs["libspvec.so"].has("SpVecAddSatFrArrayML", "cdecl"):
    SpVecAddSatFrArrayML = _libs["libspvec.so"].get("SpVecAddSatFrArrayML", "cdecl")
    SpVecAddSatFrArrayML.argtypes = [c_double * int(512), c_char * int(512), POINTER(c_int64)]
    SpVecAddSatFrArrayML.restype = None

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 322
if _libs["libspvec.so"].has("SpVecUpdateSatFrArray", "cdecl"):
    SpVecUpdateSatFrArray = _libs["libspvec.so"].get("SpVecUpdateSatFrArray", "cdecl")
    SpVecUpdateSatFrArray.argtypes = [c_int64, c_double * int(512), c_char * int(512)]
    SpVecUpdateSatFrArray.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 330
if _libs["libspvec.so"].has("SpVecDataToArray", "cdecl"):
    SpVecDataToArray = _libs["libspvec.so"].get("SpVecDataToArray", "cdecl")
    SpVecDataToArray.argtypes = [c_int64, c_double * int(512), c_char * int(512)]
    SpVecDataToArray.restype = c_int

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 449
for _lib in _libs.values():
    if not _lib.has("LoadSpVecDll", "cdecl"):
        continue
    LoadSpVecDll = _lib.get("LoadSpVecDll", "cdecl")
    LoadSpVecDll.argtypes = []
    LoadSpVecDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 450
for _lib in _libs.values():
    if not _lib.has("FreeSpVecDll", "cdecl"):
        continue
    FreeSpVecDll = _lib.get("FreeSpVecDll", "cdecl")
    FreeSpVecDll.argtypes = []
    FreeSpVecDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 14
try:
    SpVecDll = 'libspvec.so'
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 334
try:
    XF_SPVEC_POS1 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 335
try:
    XF_SPVEC_POS2 = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 336
try:
    XF_SPVEC_POS3 = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 337
try:
    XF_SPVEC_VEL1 = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 338
try:
    XF_SPVEC_VEL2 = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 339
try:
    XF_SPVEC_VEL3 = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 340
try:
    XF_SPVEC_SECCLASS = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 341
try:
    XF_SPVEC_SATNUM = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 342
try:
    XF_SPVEC_SATNAME = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 343
try:
    XF_SPVEC_EPOCH = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 344
try:
    XF_SPVEC_REVNUM = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 345
try:
    XF_SPVEC_ELSETNUM = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 346
try:
    XF_SPVEC_BTERM = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 347
try:
    XF_SPVEC_AGOM = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 348
try:
    XF_SPVEC_OGPARM = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 349
try:
    XF_SPVEC_INPCOORD = 17
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 354
try:
    XA_SPVEC_SATNUM = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 355
try:
    XA_SPVEC_EPOCH = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 356
try:
    XA_SPVEC_REVNUM = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 357
try:
    XA_SPVEC_ELSETNUM = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 358
try:
    XA_SPVEC_BTERM = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 359
try:
    XA_SPVEC_AGOM = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 360
try:
    XA_SPVEC_OGPARM = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 361
try:
    XA_SPVEC_INPCOORD = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 363
try:
    XA_SPVEC_POS1 = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 364
try:
    XA_SPVEC_POS2 = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 365
try:
    XA_SPVEC_POS3 = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 366
try:
    XA_SPVEC_VEL1 = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 367
try:
    XA_SPVEC_VEL2 = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 368
try:
    XA_SPVEC_VEL3 = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 370
try:
    XA_SPVEC_HASOWNCRL = 70
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 371
try:
    XA_SPVEC_GEOIDX = 71
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 372
try:
    XA_SPVEC_BULGEFLG = 72
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 373
try:
    XA_SPVEC_DRAGFLG = 73
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 374
try:
    XA_SPVEC_RADFLG = 74
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 375
try:
    XA_SPVEC_LUNSOLFLG = 75
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 376
try:
    XA_SPVEC_F10 = 76
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 377
try:
    XA_SPVEC_F10AVG = 77
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 378
try:
    XA_SPVEC_AP = 78
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 379
try:
    XA_SPVEC_TRUNC = 79
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 380
try:
    XA_SPVEC_CONVERG = 80
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 381
try:
    XA_SPVEC_OGFLG = 81
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 382
try:
    XA_SPVEC_TIDESFLG = 82
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 383
try:
    XA_SPVEC_NTERMS = 84
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 384
try:
    XA_SPVEC_REEVAL = 85
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 385
try:
    XA_SPVEC_INTEGCTRL = 86
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 386
try:
    XA_SPVEC_VARSTEP = 87
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 387
try:
    XA_SPVEC_INITSTEP = 88
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 389
try:
    XA_SPVEC_RMS = 99
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 390
try:
    XA_SPVEC_COVELEMS = 100
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 392
try:
    XA_SPVEC_SIZE = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 397
try:
    XS_SPVEC_SECCLASS_1 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 398
try:
    XS_SPVEC_SATNAME_8 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 400
try:
    XS_SPVEC_SIZE = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 404
try:
    XS_SPVEC_SECCLASS_0_1 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 405
try:
    XS_SPVEC_SATNAME_1_8 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 407
try:
    XS_SPVEC_LENGTH = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 412
try:
    SPVEC_INPCOORD_4P = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 413
try:
    SPVEC_INPCOORD_TMDAT = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpVecDll.h: 414
try:
    SPVEC_INPCOORD_MMJ2K = 2
except:
    pass

# No inserted files

# No prefix-stripping

