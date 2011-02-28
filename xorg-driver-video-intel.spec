%define	libdrm_ver	2.4.23
Summary:	X.org video driver for Intel integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela
Name:		xorg-driver-video-intel
Version:	2.14.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-intel-%{version}.tar.bz2
# Source0-md5:	05f187582aeabda57fcd6f2782cfbf8e
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
#BuildRequires:	autoconf >= 2.60
#BuildRequires:	automake >= 1.10.2-2
BuildRequires:	libdrm-devel >= %{libdrm_ver}
#BuildRequires:	libtool
BuildRequires:	libxcb-devel >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-dri2proto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.6.3
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= %{libdrm_ver}
Requires:	xorg-lib-libpciaccess >= 0.10
Requires:	xorg-xserver-libdri >= 1.6.3
Requires:	xorg-xserver-libglx >= 1.6.3
Requires:	xorg-xserver-server >= 1.6.3
Provides:	xorg-driver-video-i810
Obsoletes:	X11-driver-i810 < 1:7.0.0
Obsoletes:	XFree86-driver-i810 < 1:7.0.0
Obsoletes:	XFree86-i810
Obsoletes:	xorg-driver-video-i810 < 1.7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel integrated graphics chipsets. It
supports:
- i810, i810-DC100, i810e, i815, 830M, 845G, 852GM, 855GM, 865G, 915G,
  915GM, 945G, 945GM, 965G, 965Q, 946GZ, 965GM, 945GME, G33, Q33, G35,
  Q35, GM45, G45, Q45, G43, G41 chipsets,
- Pineview-M in Atom N400 series,
- Pineview-D in Atom D400/D500 series.

Requires Kernel Mode Setting (KMS) to be active.

%description -l pl.UTF-8
Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela.
Obsługuje:
- układy i810, i810-DC100, i810e, i815, 830M, 845G, 852GM, 855GM,
  865G, 915G, 915GM, 945G, 945GM, 965G, 965Q, 946GZ, 965GM, 945GME, G33,
  Q33, G35, Q35, GM45, G45, Q45, G43, G41,
- Pineview-M w procesorach Atom z serii N400,
- Pineview-D w procesorach Atom z serii D400/D500.

Wymaga aktywnego Kernel Mode Setting (KMS).

%prep
%setup -q -n xf86-video-intel-%{version}

%build
%configure \
	--disable-silent-rules

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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libI810XvMC.so.1
%attr(755,root,root) %{_libdir}/libIntelXvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIntelXvMC.so.1
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/intel_drv.so
%{_mandir}/man4/intel.4*
