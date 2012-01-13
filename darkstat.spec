Summary:	darkstat - a network traffic analyzer
Summary(pl.UTF-8):	darkstat - sieciowy analizator ruchu
Name:		darkstat
Version:	3.0.714
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dmr.ath.cx/net/darkstat/%{name}-%{version}.tar.bz2
# Source0-md5:	eef385fadc8dbb611d3d4c4d8fa94817
URL:		http://purl.org/net/darkstat
BuildRequires:	libpcap-devel >= 0.8.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
darkstat is a network traffic analyzer. It's basically a packet
sniffer which runs as a background process on a cable/DSL router and
gathers all sorts of useless but interesting statistics.

%description -l pl.UTF-8
darkstat jest sieciowym analizatorem ruchu. Jest prostym połączeniem
sniffera pakietów który uruchamia się w tle na routerze i zbiera je
wszystkie w bezużyteczne ale interesujące statystyki.

%prep
%setup -q

%build
%configure \
	--with-chroot-dir=/usr/share/empty
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README export-format.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
