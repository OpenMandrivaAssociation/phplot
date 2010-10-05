Summary:	Dynamic plots, charts, and graphs in PHP
Name:		phplot
Version:	5.2.0
Release:	%mkrel 1
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
