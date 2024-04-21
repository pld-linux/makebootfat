Summary:	The bootable USB disk generator
Summary(pl.UTF-8):	Generator bootowalnych dysków USB
Name:		makebootfat
Version:	1.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
# Source0-md5:	8ae9144e2bec8b8498361a25fdf76741
URL:		http://www.advancemame.it/boot-readme.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bootable USB disk generator.

%description -l pl.UTF-8
Generator bootowalnych dysków USB.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install mbrfat.bin $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{authors,history,readme}.html AUTHORS README HISTORY
%attr(755,root,root) %{_bindir}/makebootfat
%{_datadir}/%{name}
%{_mandir}/man1/makebootfat.1*
