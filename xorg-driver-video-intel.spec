#
# Conditional build:
%bcond_with	glamor	Glamor acceleration
%bcond_without	sna	SandyBridge's New Acceleration (also for older generations)
%bcond_without	dri3	DRI3 support
#
%define	libdrm_ver	2.4.41
%define	pixman_ver	0.28.0
%if %{with sna}
%define	xserver_ver	1.10
%else
%define	xserver_ver	1.6.3
%endif
Summary:	X.org video driver for Intel integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych Intela
Name:		xorg-driver-video-intel
Version:	2.99.917
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-intel-%{version}.tar.bz2
# Source0-md5:	fa196a66e52c0c624fe5d350af7a5e7b
URL:		http://xorg.freedesktop.org/
Patch0:		%{name}-xserver_1_8_0.patch
Patch1:		git.patch
BuildRequires:	Mesa-libGL-devel
#BuildRequires:	autoconf >= 2.63
#BuildRequires:	automake >= 1:1.10.2-2
%{?with_glamor:BuildRequires:	glamor-devel >= 0.3.1}
BuildRequires:	libdrm-devel >= %{libdrm_ver}
#BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxcb-devel >= 1.5
BuildRequires:	pixman-devel >= %{pixman_ver}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-dri2proto-devel >= 2.6
%{?with_dri3:BuildRequires:	xorg-proto-dri3proto-devel}
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= %{xserver_ver}
%{?requires_xorg_xserver_videodrv}
%{?with_glamor:Requires:	glamor >= 0.3.1}
Requires:	libdrm >= %{libdrm_ver}
Requires:	pixman >= %{pixman_ver}
Requires:	xorg-lib-libpciaccess >= 0.10
Requires:	xorg-xserver-libdri >= %{xserver_ver}
Requires:	xorg-xserver-libglx >= %{xserver_ver}
Requires:	xorg-xserver-server >= %{xserver_ver}
Provides:	xorg-driver-video
Provides:	xorg-driver-video-i810
Obsoletes:	X11-driver-i810 < 1:7.0.0
Obsoletes:	XFree86-driver-i810 < 1:7.0.0
Obsoletes:	XFree86-i810
Obsoletes:	xorg-driver-video-i810 < 1.7.2
Conflicts:	vbetool
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
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_glamor:--enable-glamor} \
	--with-default-accel=%{?with_sna:sna}%{!?with_sna:uxa} \
	--enable-uxa \
	--enable-sna%{!?with_sna:=no} \
	%{__enable_disable dri3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/lib*XvMC.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/intel-virtual-output
%attr(755,root,root) %{_libdir}/xf86-video-intel-backlight-helper
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libI810XvMC.so.1
%attr(755,root,root) %{_libdir}/libIntelXvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIntelXvMC.so.1
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/intel_drv.so
%{_mandir}/man4/intel.4*
%{_mandir}/man4/intel-virtual-output.4*
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy
