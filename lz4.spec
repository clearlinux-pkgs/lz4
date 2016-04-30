#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lz4
Version  : 131
Release  : 11
URL      : https://github.com/Cyan4973/lz4/archive/r131.tar.gz
Source0  : https://github.com/Cyan4973/lz4/archive/r131.tar.gz
Summary  : fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: lz4-bin
Requires: lz4-lib
Requires: lz4-doc
BuildRequires : cmake
BuildRequires : valgrind

%description
LZ4 - Extremely fast compression
================================
LZ4 is lossless compression algorithm,
providing compression speed at 400 MB/s per core,
scalable with multi-cores CPU.
It also features an extremely fast decoder,
with speed in multiple GB/s per core,
typically reaching RAM speed limits on multi-core systems.

%package bin
Summary: bin components for the lz4 package.
Group: Binaries

%description bin
bin components for the lz4 package.


%package dev
Summary: dev components for the lz4 package.
Group: Development
Requires: lz4-lib
Requires: lz4-bin

%description dev
dev components for the lz4 package.


%package doc
Summary: doc components for the lz4 package.
Group: Documentation

%description doc
doc components for the lz4 package.


%package lib
Summary: lib components for the lz4 package.
Group: Libraries

%description lib
lib components for the lz4 package.


%prep
%setup -q -n lz4-r131

%build
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd programs ; make test ; popd

%install
rm -rf %{buildroot}
%make_install PREFIX=/usr LIBDIR=/usr/lib64

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
