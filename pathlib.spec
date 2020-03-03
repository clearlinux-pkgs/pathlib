#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pathlib
Version  : 1.0.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/ac/aa/9b065a76b9af472437a0059f77e8f962fe350438b927cb80184c32f075eb/pathlib-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/aa/9b065a76b9af472437a0059f77e8f962fe350438b927cb80184c32f075eb/pathlib-1.0.1.tar.gz
Summary  : Object-oriented filesystem paths
Group    : Development/Tools
License  : MIT
Requires: pathlib-license = %{version}-%{release}
Requires: pathlib-python = %{version}-%{release}
Requires: pathlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
**Attention:** this backport module isn't maintained anymore. If you want to report issues or contribute patches, please consider the `pathlib2 <https://pypi.python.org/pypi/pathlib2/>`_ project instead.

Description
-----------

pathlib offers a set of classes to handle filesystem paths.  It offers the
following advantages over using string objects:

* No more cumbersome use of os and os.path functions.  Everything can be
  done easily through operators, attribute accesses, and method calls.

* Embodies the semantics of different path types.  For example, comparing
  Windows paths ignores casing.

* Well-defined semantics, eliminating any warts or ambiguities (forward vs.
  backward slashes, etc.).

Requirements
------------

Python 3.2 or later is recommended, but pathlib is also usable with Python 2.7
and 2.6.

Install
-------

In Python 3.4, pathlib is now part of the standard library.  For Python 3.3
and earlier, ``easy_install pathlib`` or ``pip install pathlib`` should do
the trick.

Examples
--------

Importing the module classes::

   >>> from pathlib import *

Listing Python source files in a directory::

   >>> list(p.glob('*.py'))
   [PosixPath('test_pathlib.py'), PosixPath('setup.py'),
    PosixPath('pathlib.py')]

Navigating inside a directory tree::

   >>> p = Path('/etc')
   >>> q = p / 'init.d' / 'reboot'
   >>> q
   PosixPath('/etc/init.d/reboot')
   >>> q.resolve()
   PosixPath('/etc/rc.d/init.d/halt')

Querying path properties::

   >>> q.exists()
   True
   >>> q.is_dir()
   False

Opening a file::

   >>> with q.open() as f: f.readline()
   ...
   '#!/bin/bash\n'


Documentation
-------------

The full documentation can be read at `Read the Docs
<https://pathlib.readthedocs.org/>`_.


Contributing
------------

Main development now takes place in the Python standard library: see
the `Python developer's guide <http://docs.python.org/devguide/>`_, and
report issues on the `Python bug tracker <http://bugs.python.org/>`_.

However, if you find an issue specific to prior versions of Python
(such as 2.7 or 3.2), you can post an issue on the
`BitBucket project page <https://bitbucket.org/pitrou/pathlib/>`_.


History
-------

Version 1.0.1
^^^^^^^^^^^^^

- Pull request #4: Python 2.6 compatibility by eevee.

Version 1.0
^^^^^^^^^^^

This version brings ``pathlib`` up to date with the official Python 3.4
release, and also fixes a couple of 2.7-specific issues.

- Python issue #20765: Add missing documentation for PurePath.with_name()
  and PurePath.with_suffix().
- Fix test_mkdir_parents when the working directory has additional bits
  set (such as the setgid or sticky bits).
- Python issue #20111: pathlib.Path.with_suffix() now sanity checks the
  given suffix.
- Python issue #19918: Fix PurePath.relative_to() under Windows.
- Python issue #19921: When Path.mkdir() is called with parents=True, any
  missing parent is created with the default permissions, ignoring the mode
  argument (mimicking the POSIX "mkdir -p" command).
- Python issue #19887: Improve the Path.resolve() algorithm to support
  certain symlink chains.
- Make pathlib usable under Python 2.7 with unicode pathnames (only pure
  ASCII, though).
- Issue #21: fix TypeError under Python 2.7 when using new division.
- Add tox support for easier testing.

Version 0.97
^^^^^^^^^^^^

This version brings ``pathlib`` up to date with the final API specified
in :pep:`428`.  The changes are too long to list here, it is recommended
to read the `documentation <https://pathlib.readthedocs.org/>`_.

.. warning::
   The API in this version is partially incompatible with pathlib 0.8 and
   earlier.  Be sure to check your code for possible breakage!

Version 0.8
^^^^^^^^^^^

- Add PurePath.name and PurePath.anchor.
- Add Path.owner and Path.group.
- Add Path.replace().
- Add Path.as_uri().
- Issue #10: when creating a file with Path.open(), don't set the executable
  bit.
- Issue #11: fix comparisons with non-Path objects.

Version 0.7
^^^^^^^^^^^

- Add '**' (recursive) patterns to Path.glob().
- Fix openat() support after the API refactoring in Python 3.3 beta1.
- Add a *target_is_directory* argument to Path.symlink_to()

Version 0.6
^^^^^^^^^^^

- Add Path.is_file() and Path.is_symlink()
- Add Path.glob() and Path.rglob()
- Add PurePath.match()

Version 0.5
^^^^^^^^^^^

- Add Path.mkdir().
- Add Python 2.7 compatibility by Michele Lacchia.
- Make parent() raise ValueError when the level is greater than the path
  length.

%package license
Summary: license components for the pathlib package.
Group: Default

%description license
license components for the pathlib package.


%package python
Summary: python components for the pathlib package.
Group: Default
Requires: pathlib-python3 = %{version}-%{release}

%description python
python components for the pathlib package.


%package python3
Summary: python3 components for the pathlib package.
Group: Default
Requires: python3-core
Provides: pypi(pathlib)

%description python3
python3 components for the pathlib package.


%prep
%setup -q -n pathlib-1.0.1
cd %{_builddir}/pathlib-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583201079
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pathlib
cp %{_builddir}/pathlib-1.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pathlib/10b3841df96ef4b2a0a36acbacf968dfde75ecfe
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pathlib/10b3841df96ef4b2a0a36acbacf968dfde75ecfe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
