%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	HTML_TagCloud
Summary:	%{_pearname} - generate a "tag cloud" in HTML
Summary(pl.UTF-8):	%{_pearname} - generowanie "chmury tagów" w HTML
Name:		php-pear-%{_pearname}
Version:	0.2.4
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	03644cb805cb3ba48fea52755a1b0744
URL:		http://pear.php.net/package/HTML_TagCloud/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-date
Requires:	php-pear
Suggests:	php-pear-Image_Color
Obsoletes:	php-pear-HTML_TagCloud-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Image/Color.*)

%description
HTML_TagCloud enables you to generate a "tag cloud" in HTML.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTML_TagCloud pozwala na generowanie chmury tagów w HTML.

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
%doc install.log docs/HTML_TagCloud/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/TagCloud.php
