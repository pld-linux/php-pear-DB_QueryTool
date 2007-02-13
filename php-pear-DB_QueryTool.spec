%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	QueryTool
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an OO-interface for easily retrieving and modifying data in a DB
Summary(pl.UTF-8):	%{_pearname} - obiektowy interfejs do odczytywania i modyfikowania danych w DB
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6b93afe58f4e5bdd2f198b2b6d7acefa
URL:		http://pear.php.net/package/DB_QueryTool/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB
Requires:	php-pear-Log >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is an OO-abstraction to the SQL-Query language, it
provides methods such as setWhere, setOrder, setGroup, setJoin, etc.
to easily build queries. It also provides an easy to learn interface
that interacts nicely with HTML-forms using arrays that contain the
column data, that shall be updated/added in a DB. This package bases
on an SQL-Builder which lets you easily build SQL-Statements and
execute them.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet to obiektowo zorientowana abstrakcja dla języka zapytań
SQL, udostępniająca metody takie jak setWhere, setOrder, setGroup,
setJoin itp. do łatwego tworzenia zapytań. Udostępnia on także łatwy
do nauczenia się interfejs współpracujący z HTML-forms przy użyciu
tablic zawierających dane z kolumn, które mają być uaktualnione/dodane
do bazy. Ten pakiet bazuje na SQL-Builderze, który pozwala na łatwe
tworzenie i wykonywanie instrukcji SQL.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
