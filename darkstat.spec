Summary:	darkstat - a network traffic analyzer
Summary(pl):	darkstat - sieciowy analizator ruchu
Name:		darkstat
Version:	2.6
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dmr.ath.cx/net/darkstat/%{name}-%{version}.tar.gz
# Source0-md5:	0a1a407acb6f9b35a46d64885c30d08d
URL:		http://purl.org/net/darkstat/
Requires:	libpcap >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
darkstat is a network traffic analyzer. It's basically a packet
sniffer which runs as a background process on a cable/DSL router and
gathers all sorts of useless but interesting statistics.

%description -l pl
darkstat jest sieciowym analizatorem ruchu. Jest prostym po³±czeniem
sniffera pakietów który uruchamia siê w tle na routerze i zbiera je
wszytstkie w bezu¿yteczne ale interesuj±ce statystyki.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
