#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : lz4
Version  : 1.9.4
Release  : 52
URL      : https://github.com/lz4/lz4/archive/v1.9.4/lz4-1.9.4.tar.gz
Source0  : https://github.com/lz4/lz4/archive/v1.9.4/lz4-1.9.4.tar.gz
Summary  : extremely fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: lz4-bin = %{version}-%{release}
Requires: lz4-lib = %{version}-%{release}
Requires: lz4-license = %{version}-%{release}
Requires: lz4-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
LZ4 - Extremely fast compression
================================
LZ4 is lossless compression algorithm,
providing compression speed > 500 MB/s per core,
scalable with multi-cores CPU.
It features an extremely fast decoder,
with speed in multiple GB/s per core,
typically reaching RAM speed limits on multi-core systems.

%package bin
Summary: bin components for the lz4 package.
Group: Binaries
Requires: lz4-license = %{version}-%{release}

%description bin
bin components for the lz4 package.


%package dev
Summary: dev components for the lz4 package.
Group: Development
Requires: lz4-lib = %{version}-%{release}
Requires: lz4-bin = %{version}-%{release}
Provides: lz4-devel = %{version}-%{release}
Requires: lz4 = %{version}-%{release}

%description dev
dev components for the lz4 package.


%package dev32
Summary: dev32 components for the lz4 package.
Group: Default
Requires: lz4-lib32 = %{version}-%{release}
Requires: lz4-bin = %{version}-%{release}
Requires: lz4-dev = %{version}-%{release}

%description dev32
dev32 components for the lz4 package.


%package lib
Summary: lib components for the lz4 package.
Group: Libraries
Requires: lz4-license = %{version}-%{release}

%description lib
lib components for the lz4 package.


%package lib32
Summary: lib32 components for the lz4 package.
Group: Default
Requires: lz4-license = %{version}-%{release}

%description lib32
lib32 components for the lz4 package.


%package license
Summary: license components for the lz4 package.
Group: Default

%description license
license components for the lz4 package.


%package man
Summary: man components for the lz4 package.
Group: Default

%description man
man components for the lz4 package.


%prep
%setup -q -n lz4-1.9.4
cd %{_builddir}/lz4-1.9.4
pushd ..
cp -a lz4-1.9.4 build32
popd
pushd ..
cp -a lz4-1.9.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702030694
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
make
popd
pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
make
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -Os -falign-functions=32 -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702030694
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lz4
cp %{_builddir}/lz4-%{version}/contrib/debian/copyright %{buildroot}/usr/share/package-licenses/lz4/2f38265e78715b5aa3ecf5b1ae2478bcaa74ab15 || :
cp %{_builddir}/lz4-%{version}/contrib/djgpp/LICENSE %{buildroot}/usr/share/package-licenses/lz4/693c355ac3857d8a8af6acec22075ef344492a1c || :
cp %{_builddir}/lz4-%{version}/examples/COPYING %{buildroot}/usr/share/package-licenses/lz4/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/lz4-%{version}/lib/LICENSE %{buildroot}/usr/share/package-licenses/lz4/63aa9e87fdd44f2c9627db9a6b6d29a95e6ef53d || :
cp %{_builddir}/lz4-%{version}/programs/COPYING %{buildroot}/usr/share/package-licenses/lz4/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/lz4-%{version}/tests/COPYING %{buildroot}/usr/share/package-licenses/lz4/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd ../build32/
%make_install32 PREFIX=/usr LIBDIR=/usr/lib64 PREFIX=/usr LIBDIR=/usr/lib32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3 PREFIX=/usr LIBDIR=/usr/lib64
popd
%make_install PREFIX=/usr LIBDIR=/usr/lib64
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lz4
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4

%files dev
%defattr(-,root,root,-)
/usr/include/lz4.h
/usr/include/lz4frame.h
/usr/include/lz4frame_static.h
/usr/include/lz4hc.h
/usr/lib64/liblz4.so
/usr/lib64/pkgconfig/liblz4.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblz4.so
/usr/lib32/pkgconfig/32liblz4.pc
/usr/lib32/pkgconfig/liblz4.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/liblz4.so.1.9.4
/usr/lib64/liblz4.so.1
/usr/lib64/liblz4.so.1.9.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblz4.so.1
/usr/lib32/liblz4.so.1.9.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lz4/2f38265e78715b5aa3ecf5b1ae2478bcaa74ab15
/usr/share/package-licenses/lz4/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/lz4/63aa9e87fdd44f2c9627db9a6b6d29a95e6ef53d
/usr/share/package-licenses/lz4/693c355ac3857d8a8af6acec22075ef344492a1c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lz4.1
/usr/share/man/man1/lz4c.1
/usr/share/man/man1/lz4cat.1
/usr/share/man/man1/unlz4.1
