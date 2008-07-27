Summary:	WindowMaker docklet with box in Matrix style
Summary(pl.UTF-8):	Aplet dla WindowMakera wyświetlający spadające znaczki
Name:		wmMatrix
Version:	0.2
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	4e9f0c94e78ad65ea9a564fba5f7a187
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	xscreensaver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A DockApp thats runs a slightly modified version of Jamie Zawinski's
xmatrix screenhack.

%description -l pl.UTF-8
Dokowalny aplet dla WindowMakera wyświetlający spadające znaczki,
znane z filmu Matrix.

%prep
%setup -q

%build
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/*
