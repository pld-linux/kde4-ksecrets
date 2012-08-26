#
# ksecrets removed from kde-4.9 (due to early development state)
# http://mail.kde.org/pipermail/release-team/2012-May/005668.html
#
%define		_state		stable
%define		orgname		ksecrets
%define		qtver		4.8.0

Summary:	K Desktop Environment - secrets management infrastructure
Name:		kde4-ksecrets
Version:	4.8.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	61533859da11b808214b4bc0478e31ad
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qca-devel
Requires:	kde4-kdebase-workspace >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secrets management infrastructure for KDE.

%package devel
Summary:	ksecrets development files
Summary(pl.UTF-8):	Pliki dla programistów ksecrets
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
ksecrets development files.

%description devel -l pl.UTF-8
Pliki dla programistów ksecrets.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksecrets
%attr(755,root,root) %{_bindir}/ksecretsserviced
%attr(755,root,root) %{_bindir}/ksecretsync
%attr(755,root,root) %{_bindir}/kwl2kss
%attr(755,root,root) %{_libdir}/kde4/kcm_ksecretsync.so
%attr(755,root,root) %{_libdir}/kde4/kio_ksecretsservice.so
%attr(755,root,root) %{_libdir}/libksecretsservice.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libksecretsservice.so.?
%{_desktopdir}/kde4/ksecrets.desktop
%{_datadir}/apps/ksecretsync
%{_datadir}/config.kcfg/kcm_ksecretsync.kcfg
%{_datadir}/dbus-1/services/org.kde.ksecretsserviced.service
%{_datadir}/kde4/services/kcm_ksecretsync.desktop
%{_datadir}/kde4/services/ksecretsserviced.desktop
%{_datadir}/kde4/services/secrets.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/ksecretsservice
%attr(755,root,root) %{_libdir}/libksecretsservice.so
