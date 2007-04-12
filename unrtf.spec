Name:		unrtf
Version: 0.19.3
Release:	%mkrel 3
Source0:	http://www.gnu.org/software/unrtf/unrtf-%{version}.tar.bz2
URL:		http://www.gnu.org/software/unrtf/unrtf.html
License:	GPL
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Summary:	RTF to other formats converter
Group:		Text tools

%description
UnRTF is a moderately complicated converter from RTF to other
formats, including HTML, LaTeX, text, and PostScript. Converting
to HTML, it supports tables, fonts, colors, embedded images, 
hyperlinks, paragraph alignment among other things. All other
conversions are "alpha"--just begun.

%prep
%setup -q

%build
%make CFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%defattr(-, root, root)
%doc README CHANGES doc/unrtf.html
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


