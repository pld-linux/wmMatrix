Summary:	WindowMaker docklet with box in Matrix style
Summary(pl):	Aplet dla WindowMakera wyswietlajacy spadajace znaczki
Name:		wmMatrix
Version:	0.2
Release:	1
License:	GPL
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Group:		X11/Window Managers/Tools
Requires:	xscreensaver	
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A DockApp thats runs a slightly modified version of Jamie Zawinski's
xmatrix screenhack.

%description -l pl
Dokowalny aplet dla WindowMakera wyswietlajacy spadajace znaczki,
znane z filmu Matrix.

%prep
%setup -q

%build
#%{__make} CC=%{__cc}
%{__make} clean
%{__make}
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}       $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
