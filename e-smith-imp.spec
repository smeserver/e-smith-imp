# $Id: e-smith-imp.spec,v 1.11 2010/01/24 03:19:28 mrjhb3 Exp $

Summary: e-smith specific IMP configuration and templates.
%define name e-smith-imp
Name: %{name}
%define version 5.0.0
%define release 7
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-imp_imp-4.3.patch
Patch2: e-smith-imp_imp-4.3.4.patch
Patch3: e-smith-imp-4.3.5.patch
Patch4: e-smith-imp-4.3.6.patch  
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.3
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: e-smith-ingo
Requires: php
Requires: php-ldap
Requires: php-mysql
Requires: php-pear-HTTP-Request
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: dcb-e-smith-imp
Obsoletes: smeserver-imp-menuarray

%changelog
* Sat Jan 23 2010 John H. Bennett III <bennettj@johnbennettservices.com> 5.0.0-7
- Updated templates to reflect changes in imp 4.3.6 [SME: 5722]

* Tue Oct 13 2009 John H. Bennett III <bennettj@johnbennettservices.com> 5.0.0-6
- Updated templates to reflect changes in imp 4.3.5 [SME: 5510]

* Sat Jun 20 2009 John H. Bennett III <bennettj@johnbennettservices.com> 5.0.0-5
- Updated templates to reflect changes in imp 4.3.4 [SME: 5371]

* Sun Dec 28 2008 Gavin Weight <gweight@gmail.com> 5.0.0-4
- Bump version to accept previous requires entry. [SME: 4821]

* Sun Dec 21 2008 John H. Bennett III <bennettj@johnbennettservices.com> 5.0.0-3
- Updated spec file to require php-pear-HTTP-Request to accomodate HTML composition [SME: 4821]

* Sat Dec 06 2008 John H. Bennett III <bennettj@johnbennettservices.com> 5.0.0-2       
- Updated templates to reflect changes in imp 4.3 [SME: 4832]

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

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
