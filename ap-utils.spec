%define prerelease pre3

Summary: Configure and monitor Wireless Access Points
Name: ap-utils
Version: 1.5.1
Release: 0.%{prerelease}.5
License: GPL
Group: Networking/Other
URL: https://ap-utils.polesye.net/
Source: http://prdownloads.sourceforge.net/ap-utils/%{name}-%{version}%{prerelease}.tar.bz2
BuildRequires: pkgconfig(ncurses)

%description
Wireless Access Point Utilities for Unix is a set of utilities
to configure and monitor Wireless Access Points under Unix.

%prep
%setup -q -n %{name}-%{version}%{prerelease}

%build
%define Werror_cflags %nil
%configure2_5x
%make

%install
%makeinstall_std

# remove french translation, it is prevent correct usage of ap-config
rm %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/ap-utils.mo

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS INSTALL NEWS COPYING README TODO ChangeLog
%doc Documentation/FAQ Documentation/*.html
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/*

