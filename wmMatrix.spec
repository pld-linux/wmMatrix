Summary:	WindowMaker docklet with box in Matrix style
Summary(pl):	Aplet dla WindowMakera wy¶wietlaj±cy spadaj±ce znaczki
Name:		wmMatrix
Version:	0.2
Release:	1
License:	GPL
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	4e9f0c94e78ad65ea9a564fba5f7a187
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Group:		X11/Window Managers/Tools
BuildRequires:	XFree86-devel
Requires:	xscreensaver	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A DockApp thats runs a slightly modified version of Jamie Zawinski's
xmatrix screenhack.

%description -l pl
Dokowalny aplet dla WindowMakera wy¶wietlaj±cy spadaj±ce znaczki,
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}       $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
