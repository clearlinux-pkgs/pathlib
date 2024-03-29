#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pathlib
Version  : 1.0.1
Release  : 36
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
pathlib offers a set of classes to handle filesystem paths.  It offers the
following advantages over using string objects:

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
export SOURCE_DATE_EPOCH=1603397977
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
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
