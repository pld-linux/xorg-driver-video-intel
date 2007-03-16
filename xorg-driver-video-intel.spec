Summary:	X.org video driver for Intel integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela
Name:		xorg-driver-video-intel
Version:	1.9.92
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-intel-%{version}.tar.bz2 
# Source0-md5:	e86af80d07c7e694897b46c95bfe9c08
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.3
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.2.99.902
Requires:	xorg-xserver-server >= 1.2.99.902
Provides:	xorg-driver-video-i810
Obsoletes:	xorg-driver-video-i810
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel integrated graphics chipsets. It supports
the i810, i810-DC100, i810e, i815, 830M, 845G, 852GM, 855GM, 865G,
915G, 915GM, 945G, 945GM, 965G, 965Q and 946GZ chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela.
Obsługuje układy i810, i810-DC100, i810e, i815, 830M, 845G, 852GM,
855GM, 865G, 915G, 915GM, 945G, 945GM, 965G, 965Q i 946GZ.

%prep
%setup -q -n xf86-video-intel-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libI810XvMC.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*.*
%{_mandir}/man4/intel.4*
