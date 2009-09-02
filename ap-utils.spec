%define prerelease pre3

Summary:	Configure and monitor Wireless Access Points 
Name:		ap-utils
Version:	1.5.1
Release:	%mkrel 0.%{prerelease}.4

Source:		http://prdownloads.sourceforge.net/ap-utils/%name-%{version}%{prerelease}.tar.bz2

License:	GPL
Group:		Networking/Other
URL:		http://ap-utils.polesye.net/
Buildrequires:	libncurses-devel
Buildroot:	%_tmppath/%name-buildroot

%description
Wireless Access Point Utilities for Unix is a set of utilities 
to configure and monitor Wireless Access Points under Unix.

%prep

%setup -q -n %name-%{version}%{prerelease}

%build

%configure2_5x

%make

%install
rm -Rf $RPM_BUILD_ROOT

%makeinstall

# remove french translation, it is prevent correct usage of ap-config
rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/ap-utils.mo

%find_lang %name

%clean
rm -Rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README TODO ChangeLog
%doc Documentation/FAQ Documentation/*.html 
%_bindir/*
%_sbindir/*
%_mandir/man8/*


