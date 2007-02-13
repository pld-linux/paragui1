Summary:	ParaGUI - A complete GUI/Windowing system for SDL
Summary(pl.UTF-8):	ParaGUI - kompletne środowisko okienkowe dla SDL
Name:		paragui1
Version:	1.0.4
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://savannah.nongnu.org/download/paragui/paragui-%{version}.tar.gz
# Source0-md5:	fc0cfcb31e28c2f7ff7e9900d3c5f651
Patch0:		paragui-am18.patch
Patch1:		paragui-link.patch
Patch2:		%{name}-64bit.patch
Patch3:		%{name}-v1.patch
URL:		http://www.paragui.org/
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++12-devel >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	physfs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a complete GUI/Windowing system for SDL.

%description -l pl.UTF-8
Kompletne środowisko okienkowe dla SDL.

%package devel
Summary:	Includes and more to develop SDL GUI applications
Summary(pl.UTF-8):	Pliki nagłówkowe dla ParaGUI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.6
Requires:	expat-devel
Requires:	freetype-devel >= 2.1.0
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libsigc++12-devel >= 1.2.5
Requires:	libtiff-devel
Requires:	physfs-devel

%description devel
Header files for ParaGUI library - a complete GUI/Windowing system for
SDL.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla ParaGUI.

%package static
Summary:	Static paragui library
Summary(pl.UTF-8):	Statyczna biblioteka paragui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of paragui library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki paragui.

%prep
%setup -q -n paragui-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd src/physfs
# only configured, not built (system physfs is used)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
%configure \
	--with-themedir=%{_datadir}/%{name}
cp paragui-config paragui1-config
cp paragui.pc paragui1.pc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README-ParaGUI.txt AUTHORS TODO README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
# conflict with paragui.spec
#%{_aclocaldir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
