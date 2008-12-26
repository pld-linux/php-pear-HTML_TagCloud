%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	TagCloud
%define		_status		beta
%define		_pearname	HTML_TagCloud
Summary:	%{_pearname} - generate a "tag cloud" in HTML
Summary(pl.UTF-8):	%{_pearname} - generowanie "chmury tagów" w HTML
Name:		php-pear-%{_pearname}
Version:	0.2.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e0aaca38d8bfe21eee160093baf76dfb
URL:		http://pear.php.net/package/HTML_TagCloud/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML_TagCloud enables you to generate a "tag cloud" in HTML.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTML_TagCloud pozwala na generowanie chmury tagów w HTML.

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
%doc install.log docs/HTML_TagCloud/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/TagCloud.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
