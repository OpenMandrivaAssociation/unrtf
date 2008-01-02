Name:		unrtf
Version:	0.20.4
Release:	%mkrel 1
Source0:	http://ftp.gnu.org/gnu/unrtf/unrtf_%{version}.tar.gz
Source1:	http://ftp.gnu.org/gnu/unrtf/unrtf_%{version}.tar.gz.sig
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
%setup -q -n %{name}_%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-, root, root)
%doc AUTHORS README NEWS
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


