Name: quazip
Summary: ZIP for Qt
Version: 1.2
Release: 1
License: LGPLv2+
URL: https://stachenov.github.io/quazip/
Source: %{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
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
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/QuaZip*/
%{_libdir}/libquazip1-qt5.so
%{_libdir}/pkgconfig/quazip1-qt5.pc
%{_libdir}/cmake/QuaZip*/*.cmake

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libquazip1-qt5.so.*
