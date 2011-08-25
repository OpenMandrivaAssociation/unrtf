Name:		unrtf
Version:	0.21.2
Release:	%mkrel 1
Source0:	http://ftp.gnu.org/gnu/unrtf/unrtf-%{version}.tar.gz
Source1:	http://ftp.gnu.org/gnu/unrtf/unrtf-%{version}.tar.gz.sig
URL:		http://www.gnu.org/software/unrtf/unrtf.html
License:	GPLv3
Buildroot:	%{_tmppath}/%{name}-%{version}
Summary:	RTF to other formats converter
Group:		Text tools

%description
UnRTF is a moderately complicated converter from RTF to other
formats, including HTML, LaTeX, text, and PostScript. Converting
to HTML, it supports tables, fonts, colors, embedded images,
hyperlinks, paragraph alignment among other things. All other
conversions are "alpha"--just begun.

%prep
%setup -q -n %{name}-%{version}
sed -i -e 's#/usr/local/lib/unrtf/#%{_datadir}/unrtf/#' src/main.h
sed -i -e 's#/usr/local/lib/unrtf/#%{_datadir}/unrtf/#' src/path.h
sed -i -e 's#/usr/local/lib/unrtf/#%{_datadir}/unrtf/#' src/my_iconv.h

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}/%{_libdir}/%{name} %{buildroot}/%{_datadir}/

%files
%defattr(-, root, root)
%doc AUTHORS README NEWS
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%clean
rm -rf %{buildroot}

