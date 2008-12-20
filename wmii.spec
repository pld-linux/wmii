Summary:	Window manager improved 2
Summary(pl.UTF-8):	Window manager improved 2 - ulepszony zarządca okien
Name:		wmii
Version:	2.5.2
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://code.suckless.org/dl/wmii/%{name}-%{version}.tar.gz
# Source0-md5:	61677e625be99732860e423b7074127f
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-9base.patch
URL:		http://www.suckless.org/wmii/
BuildRequires:	xorg-lib-libX11-devel
Requires:	9base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmii is a minimalist window manager with a small memory footprint. One
design goal is not to exceed 10.000 lines of code. Thus it has one of
the highest functionality/LOC ratios ever seen in a window manager.

%description -l pl.UTF-8
wmii to minimalistyczny zarządca okien o niewielkim zużyciu pamięci.
Jednym z jego celów jest nieprzekroczenie 10000 linii kodu, dzięki
czemu ma jeden z największych współczynników funkcjonalności do liczby
linii kodu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	OPTLDFLAGS="%{rpmldflags}" \
	LIB="%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%dir %{_sysconfdir}/X11/%{name}-2.5
%attr(755,root,root) %{_sysconfdir}/X11/%{name}-2.5/*
%attr(755,root,root) %{_bindir}/wmii*
%{_mandir}/man1/wmii*.1*
%{_datadir}/xsessions/%{name}.desktop
