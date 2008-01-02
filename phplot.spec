Summary:	Dynamic plots, charts, and graphs in PHP
Name:		phplot
Version:	5.0
Release:	%mkrel 0.rc2.2
License:	BSD
Group:		Networking/Other
URL:		http://www.phplot.com/
Source0:	%{name}-%{version}rc2.tar.bz2
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

%setup -q -n %{name}

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
install -m644 examples/*.ttf %{buildroot}%{_datadir}/phplot/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt doc examples
%{_datadir}/phplot
