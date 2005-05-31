Summary:	The bootable USB disk generator
Name:		makebootfat
Version:	1.4
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
URL:		-
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bootable USB disk generator.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*[!1] test
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
