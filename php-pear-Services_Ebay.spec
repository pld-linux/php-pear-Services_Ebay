%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Ebay
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - interface to eBay's XML-API
Summary(pl):	%{_pearname} - interfejs do API XML eBay
Name:		php-pear-%{_pearname}
Version:	0.12.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f06197217dece26606f08360771cf6b3
URL:		http://pear.php.net/package/Services_Ebay/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:5.0.0
Requires:	php-curl
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.3.2
Requires:	php-pear-XML_Serializer >= 0.16.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is interface to eBay's XML-API. It provides objects that are able
to communicate with eBay as well as models that help you working with
the return values like User or Item models.

The Services_Ebay class provides a unified method to use all objects.

In PEAR status of this package is: %{_status}.

%description -l pl
Jest to interfejs do API XML-owego eBay. Udostêpnia obiekty do
komunikacji z eBay jak równie¿ modele u³atwiaj±ce pracê ze zwracanymi
warto¶ciami takimi jak modele U¿ytkownika czy Przedmiotów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
