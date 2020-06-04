Name: quazip
Summary: ZIP for Qt
Version: 0.9.1
Release: 1
License: LGPLv2.1+
URL: https://stachenov.github.io/quazip/
Source: %{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(zlib)

%description
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that can
be used to access ZIP archives. It uses the Qt toolkit.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that can
be used to access ZIP archives. It uses the Qt toolkit.

This packages contains the development files for building QuaZIP-based apps.

%prep
%autosetup -n %{name}-%{version}/quazip

%build
%cmake .
%make_build

%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot}
# Remove static library
rm %{buildroot}%{_libdir}/libquazip5.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/quazip5/*.h
%{_libdir}/libquazip5.so
%{_libdir}/pkgconfig/quazip.pc
%{_libdir}/cmake/QuaZip5/QuaZip5Config.cmake

%files
%defattr(-,root,root,-)
%{_libdir}/libquazip5.so.*
