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



%changelog
* Thu Aug 25 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.21.2-1mdv2012.0
+ Revision: 697108
- update to new version 0.21.2

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.21.1-8
+ Revision: 640488
- rebuild to obsolete old packages

* Sun Jan 30 2011 Tomas Kindl <supp@mandriva.org> 0.21.1-7
+ Revision: 634022
- finally fix #62270 and #54232, update license info

* Sat Jan 22 2011 Tomas Kindl <supp@mandriva.org> 0.21.1-6
+ Revision: 632276
- move files from libdir to datadir where they belong, fixing #62270, #54232

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.21.1-5mdv2011.0
+ Revision: 615361
- the mass rebuild of 2010.1 packages

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 0.21.1-4mdv2010.1
+ Revision: 501572
- really fix bug#54232

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 0.21.1-3mdv2010.1
+ Revision: 501559
- fix bug#54232 (wrong config dir)

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 0.21.1-2mdv2010.1
+ Revision: 501558
- rebuild

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.21.1-1mdv2010.1
+ Revision: 493335
- update to new version 0.21.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.21.0-2mdv2010.0
+ Revision: 427481
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.21.0-1mdv2009.1
+ Revision: 332938
- New upstream release

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.20.2-3mdv2009.0
+ Revision: 225902
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.20.2-2mdv2008.1
+ Revision: 178878
- rebuild
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Emmanuel Andry <eandry@mandriva.org>
    - New version

* Sat May 19 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.20.2-1mdv2008.0
+ Revision: 28389
- Updated to 0.20.2.


* Fri Jan 12 2007 Pixel <pixel@mandriva.com> 0.19.3-3mdv2007.0
+ Revision: 108014
- use mkrel
- rebuild
- Import unrtf

* Fri Oct 14 2005 Pixel <pixel@mandriva.com> 0.19.3-2mdk
- rebuild

* Mon May 24 2004 Michael Scherer <misc@mandrake.org> 0.19.3-1mdk
- New release 0.19.3

