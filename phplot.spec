Summary:	Dynamic plots, charts, and graphs in PHP
Name:		phplot
Version:	5.3.1
Release:	2
License:	BSD
Group:		Networking/Other
URL:		http://phplot.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/phplot/%name/%version/%name-%version.tar.gz
Requires:	php-session php-gd 
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A graph library for dynamic scientific, business, and
stock-market charts. Written in PHP and supports, PHP3,
PHP4, TTF (or no ttf), and GD versions 1.2 - latest
version. Includes Pie, Bar, Line, Area, Point and
combination plots.

%prep
%setup -q

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/phplot
install -m644 *.php %{buildroot}%{_datadir}/phplot/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt contrib
%{_datadir}/phplot


%changelog
* Wed Mar 09 2011 Stéphane Téletchéa <steletch@mandriva.org> 5.3.1-1mdv2011.0
+ Revision: 643212
- update to new version 5.3.1

* Tue Oct 05 2010 Funda Wang <fwang@mandriva.org> 5.2.0-1mdv2011.0
+ Revision: 583112
- update to new version 5.2.0

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 5.1.1-1mdv2010.1
+ Revision: 531594
- new version 5.1.1

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 5.0-0.rc2.3mdv2010.0
+ Revision: 430694
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 5.0-0.rc2.2mdv2008.1
+ Revision: 140728
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Anne Nicolas <ennael@mandriva.org> 5.0-0.rc2.2mdv2008.0
+ Revision: 63547
- Import phplot



* Mon Jun 26 2006 Oden Eriksson <oeriksson@mandriva.com> 5.0-0.rc2.2mdv2007.0
- rebuild

* Fri May 13 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0-0.rc2.1mdk
- 5.0rc2
- relocate to %%{_datadir}/phplot

* Thu Apr 01 2004 Michael Scherer <misc@mandrake.org> 4.4.6-3mdk
- build release
- clean Requires
- [DIRM]
 
* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.4.6-2mdk
- build release

* Sun Jun  2 2002 <oden.eriksson@kvikkjokk.net> 4.4.6-1mdk
- initial cooker contrib
