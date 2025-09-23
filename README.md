# public_astrostandards

Author : Kerry Wood (kerry.wood@asterism.ai)

# Overview

These are pre-packaged Python harnesses for the AstroStandards.  Though the AstroStandards come with Python harnesses..
I like these better.

They're made via `ctypesgen` against the C harnesses.  They tend to be more predictable and allow more low-level access
to the underlying FORTRAN functions.

## Setup

1. First, you'll need to go get a copy of the appropriate DLL's.  (USSF is particular about distributing the DLL's, so..
tough luck).

2. Unzip your appropriate architecture DLL's somewhere.

3. Add that to your `$PATH` (Windows) or `LD_LIBRARY_PATH` so that the linker can find them.

4. Add `ASTROSTANDARDS_LIBDIR` to your environment (in both Windows and Linux).  The harnesses will look for this to
know where to find the DLL's.  (**NOTE** you can do this on a per-call basis for Linux, see below).

5. (optional) Test by running `python -c "import public_astrostandards as PA; PA.get_versions()"`

## Questions and Notes

*Why the environment variables and manual download?*
    
    - I could definitely make this easier by getting rid of this.  I could even auto-package the Dll's for the
      architectures and set the path to be the same as the Python library.  But, that would violate the terms of use.
      This method also requires more configuration and gives you more control; important things for networks that have
      lots of ... limitations.

    - Maybe I'll add a utility that does exactly that.. you point it at a directory with the Dll's and it auto-sets up
      the Dll's for you.

*Why not use the other harnesses?*
    
    - Those harnesses are fine.  These are more standardized and allow more granular control over things like float
      arrays.  I like these better.




