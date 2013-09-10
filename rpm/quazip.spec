Name: quazip
Summary: ZIP for Qt
Version: 0.5.1
Release: 1
Group: System/Libraries
License: LGPL
URL: http://quazip.sourceforge.net/
Source: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(QtCore)
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
%setup -q

%build
cd quazip
qmake PREFIX=%{_prefix}
make

%install
rm -rf %{buildroot}
cd quazip
make install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/quazip/*.h
%{_libdir}/libquazip.so

%files
%defattr(-,root,root,-)
%{_libdir}/libquazip.so.*
