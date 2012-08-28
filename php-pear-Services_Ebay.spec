%define		status		alpha
%define		pearname	Services_Ebay
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - interface to eBay's XML-API
Summary(pl.UTF-8):	%{pearname} - interfejs do API XML eBay
Name:		php-pear-%{pearname}
Version:	0.13.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	6616ef0ac457b97f586c3290fe338082
URL:		http://pear.php.net/package/Services_Ebay/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 5.0.0
Requires:	php(curl)
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Jest to interfejs do API XML-owego eBay. Udostępnia obiekty do
komunikacji z eBay jak również modele ułatwiające pracę ze zwracanymi
wartościami takimi jak modele Użytkownika czy Przedmiotów.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Services_Ebay/README .
mv .%{php_pear_dir}/data/Services_Ebay/progress .
# wtf: https://pear.php.net/bugs/bug.php?id=19591
rm .%{php_pear_dir}/data/Services_Ebay/Services_Ebay-0.13.0.tgz

mv docs/%{pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log progress
%doc docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/*.php
%{php_pear_dir}/Services/Ebay
%{_examplesdir}/%{name}-%{version}
