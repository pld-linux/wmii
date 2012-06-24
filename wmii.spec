Summary:	Window manager improved 2
Summary(pl):	Window manager improved 2 - ulepszony zarz�dca okien
Name:		wmii
Version:	2.5.1
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://wmii.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	fd2ab30ba59079a98159410d2ef6fa0b
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-9base.patch
URL:		http://wmii.de/
BuildRequires:	XFree86-devel
Requires:	9base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmii is a minimalist window manager with a small memory footprint. One
design goal is not to exceed 10.000 lines of code. Thus it has one of
the highest functionality/LOC ratios ever seen in a window manager.

%description -l pl
wmii to minimalistyczny zarz�dca okien o niewielkim zu�yciu pami�ci.
Jednym z jego cel�w jest nieprzekroczenie 10000 linii kodu, dzi�ki
czemu ma jeden z najwi�kszych wsp�czynnik�w funkcjonalno�ci do liczby
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xsessions

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
