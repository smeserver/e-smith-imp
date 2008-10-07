# $Id: e-smith-imp.spec,v 1.5 2008/10/07 18:30:47 slords Exp $

Summary: e-smith specific IMP configuration and templates.
%define name e-smith-imp
Name: %{name}
%define version 5.0.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.2
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: e-smith-ingo
Requires: php
Requires: php-ldap
Requires: php-mysql
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: dcb-e-smith-imp
Obsoletes: smeserver-imp-menuarray

%changelog
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 5.0.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Mon Jun 23 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2-1
- Initial build
- Jump in package name to reflect new version of imp

%description
This package adds necessary templates and configuration items
so that IMP will work properly on SME Server

%prep
%setup

%build
mkdir -p root/home/httpd/html/horde/imp/SSLonly
 
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
