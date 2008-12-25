Summary:	X.org video driver for Intel integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela
Name:		xorg-driver-video-intel
Version:	2.5.99.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-intel-%{version}.tar.bz2
# Source0-md5:	fb7a7d9e068682aecdd077f2b99a9106
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.1
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1.3
BuildRequires:	xorg-xserver-server-devel >= 1.3.0.0
%requires_xorg_xserver_videodrv
Requires:	libdrm >= 2.4.1
Requires:	xorg-xserver-libdri
Requires:	xorg-xserver-libglx
Requires:	xorg-xserver-server >= 1.3.0.0
Provides:	xorg-driver-video-i810
Obsoletes:	X11-driver-i810 < 1:7.0.0
Obsoletes:	XFree86-i810
Obsoletes:	XFree86-driver-i810 < 1:7.0.0
Obsoletes:	xorg-driver-video-i810
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel integrated graphics chipsets. It supports
the i810, i810-DC100, i810e, i815, 830M, 845G, 852GM, 855GM, 865G,
915G, 915GM, 945G, 945GM, 965G, 965Q, 946GZ, 965GM, 945GME, G33, Q33
and Q35 chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela.
Obsługuje układy i810, i810-DC100, i810e, i815, 830M, 845G, 852GM,
855GM, 865G, 915G, 915GM, 945G, 945GM, 965G, 965Q, 946GZ, 965GM,
945GME, G33, Q33 i Q35.

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

rm $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/lib*XvMC.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/intel_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/i810_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ch7017.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ch7xxx.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ivch.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sil164.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/tfp410.so
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libI810XvMC.so.1
%attr(755,root,root) %{_libdir}/libIntelXvMC.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libIntelXvMC.so.1
%{_mandir}/man4/intel.4*
%{_mandir}/man4/i810.4*
