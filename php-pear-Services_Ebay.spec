%define		_class		Services
%define		_subclass	Ebay
%define		_status		alpha
%define		_pearname	Services_Ebay
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - interface to eBay's XML-API
Summary(pl.UTF-8):	%{_pearname} - interfejs do API XML eBay
Name:		php-pear-%{_pearname}
Version:	0.12.0
Release:	7
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f06197217dece26606f08360771cf6b3
URL:		http://pear.php.net/package/Services_Ebay/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(curl)
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.2
Requires:	php-pear-XML_Serializer >= 0.16.0
Obsoletes:	php-pear-Services_Ebay-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is interface to eBay's XML-API. It provides objects that are able
to communicate with eBay as well as models that help you working with
the return values like User or Item models.

The Services_Ebay class provides a unified method to use all objects.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Jest to interfejs do API XML-owego eBay. Udostępnia obiekty do
komunikacji z eBay jak również modele ułatwiające pracę ze zwracanymi
wartościami takimi jak modele Użytkownika czy Przedmiotów.

Ta klasa ma w PEAR status: %{_status}.

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
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/*.php
%{php_pear_dir}/Services/Ebay
