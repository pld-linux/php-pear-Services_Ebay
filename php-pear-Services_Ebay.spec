%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Ebay
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - interface to eBay's XML-API
Summary(pl):	%{_pearname} - interfejs do API XML eBay
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cd6239e562c02aba2d3580b409371673
URL:		http://pear.php.net/package/Services_Ebay/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Call,Model,Transport}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Call/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Call
install %{_pearname}-%{version}/%{_subclass}/Model/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Model
install %{_pearname}-%{version}/%{_subclass}/Transport/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Transport

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,examples}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
