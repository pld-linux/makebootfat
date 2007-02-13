Summary:	The bootable USB disk generator
Summary(pl.UTF-8):	Generator bootowalnych dysków USB
Name:		makebootfat
Version:	1.4
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
# Source0-md5:	8ae9144e2bec8b8498361a25fdf76741
URL:		http://advancemame.sourceforge.net/boot-readme.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bootable USB disk generator.

%description -l pl.UTF-8
Generator bootowalnych dysków USB.

%prep
%setup -q

%build
%{__libtoolize}
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
%doc doc/*[!1] test AUTHORS README HISTORY mbrfat.asm
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
