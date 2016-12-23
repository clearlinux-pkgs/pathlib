#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pathlib
Version  : 1.0.1
Release  : 9
URL      : https://pypi.python.org/packages/source/p/pathlib/pathlib-1.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pathlib/pathlib-1.0.1.tar.gz
Summary  : Object-oriented filesystem paths
Group    : Development/Tools
License  : MIT
Requires: pathlib-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
pathlib offers a set of classes to handle filesystem paths.  It offers the
following advantages over using string objects:

%package python
Summary: python components for the pathlib package.
Group: Default

%description python
python components for the pathlib package.


%prep
%setup -q -n pathlib-1.0.1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
