Summary: e-smith specific IMP configuration and templates.
%define name e-smith-imp
Name: %{name}
%define version 1.13.0
%define release 10
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Patch0: e-smith-imp-1.13.0-02.conf_php.patch
Patch1: e-smith-imp-1.13.0-03.server_php_header_txt.patch 
Patch2: e-smith-imp-1.13.0-04.prefs_php.patch
Patch3: e-smith-imp-1.13.0-05.createlinks.patch
Patch4: e-smith-imp-1.13.0-06.menuarray.patch
Patch5: e-smith-imp-1.13.0-07.imp_horde_registry_php.patch 
Patch6: e-smith-imp-1.13.0-09.imp_414.patch
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.1
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
* Wed May 9 2007 Shad L. Lords <slords@mail.com> 1.13.0-10
- Move pear module requires to e-smith-horde

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sun Mar 25 2007 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-09
- Updated imp conf.php and servers.php templates per imp 4.1.4 [SME: 2785]

* Sat Dec 09 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Oct 5 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-07
- Added imp specific horde/config/registry.php settings.  These were previously
  kept in the e-smith-horde rpm.

* Sat Sep 23 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-06
- Added an includes statement to 120Menusettings that will grab the information in 
  horde/conf.menu.apps.php.  This way each of the individual horde modules don't 
  have to repeatedly process the same template for the menu array section in conf.php.
- Added the ability to enable or disable imp menu icon from showing up on the
  main webmail screen.  To enable- config setprop imp MenuArray disabled|enabled
  enabled by default

* Tue Sep 19 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-05
- Patch to move the items in the spec file that created the template-php symlinks
  to the createlinks section.  

* Tue Sep 19 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-04
- Patch to prefs.php templates to reflect changes in imp 4.1.3

* Sat Sep 16 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-03
- Patch to servers.php templates to reflect changes in imp 4.1.3
- Patch to header.txt template that changes name to SME Server

* Sat Sep 16 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-02
- Patch to conf.php templates to reflect changes in imp 4.1.3

* Fri Sep 15 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-01
- Rolled to new dev stream to reflect work done for imp 4.1.3

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Tue Feb 14 2006 Gavin Weight <gweight@gmail.com> 1.11.2-17
- Fix issues with message viewing options. [SME: 427]

* Tue Feb 07 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.2-16
- Fix issues with configuration of receipt request. [SME: 427]

* Wed Jan 25 2006 Charlie Brady <charlieb@e-smith.com> 1.11.2-15
- Fix warning message from last change. [SME: 568]

* Fri Jan 20 2006 Charlie Brady <charlieb@e-smith.com> 1.11.2-14
- Sort domains in imp configuration with primary domain first. [SME: 521]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.2-13
- Bump release number only

* Tue Oct 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-12]
- Add missing Requires of php-ldap and php-mysql. [SF: 1337062]

* Thu Sep 22 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.2-11]
- Revert last change - the dependency should be in e-smith-horde,
  which it is [SF: 1274096]

* Thu Sep 22 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.2-10]
- Add Requires wv for attachment viewing [SF: 1266925]

* Mon Sep 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-09]
- Add Requires e-smith-ingo [SF: 1276898]

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-08]
- Add Requires headers to ensure that all php and pear stuff is
  pulled in on an upgrade.

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [1.11.2-07]
- Change requires from imp to imp-h3
- Fix Rewrite rule and Proxy Pass to be cleaner

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-06]
- Fix quoting in servers.php template [SF: 1226207]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-05]
- Add templates.metadata file for prefs.php (courtesy of Greg Swallow)
  [SF: 1220563].

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-04]
- Add templating of prefs.php. [SF: 1219234]

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-03]
- Resolve duplication of webmail default db records (moved to
  e-smith-base).
- Add domain entry in imp config for each virtual domain.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-02]
- Horde 3 update config changes, thanks to Greg Swallow.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.2-01]
- Roll to new development stream for horde 3 update - 1.11.2

* Tue Mar 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-04]
- Add missing default db entries for "imp". [MN00064130]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-03]
- Obsolete conf-imp action by using generic_template_expand action and
  default db fragments. Update e-smith-lib dependency. [MN00064130]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-02]
- Modify config for compatibility with apache 2. [charlieb MN00051144]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-01]
- New development stream version - 1.11.1

* Wed May 26 2004 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-03]
- Only catch ..../horde/... with slash after horde. This fixes
  an issue which stopped network installs of the server _from_
  the server when webmail was enabled for HTTPS access only.
  [gordonr MN00034938]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-02]
- Removed "RewriteEngine on" directive, since it will be on already in new
  e-smith-apache version. [msoulier MN00020885]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- rolling to dev - 1.11.0

* Fri Jul 11 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-02]
- Add 'allow_resume_all_in_drafts' user option in conf.php template.
  [charlieb 9410]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-10]
- Add imp|installed property so Mail button shows in the
  address book [gordonr 9041]

* Mon Jun  2 2003 Tony Clayton <apc@e-smith.com>
- [1.9.0-09]
- Use mod_rewrite for webmail SSL redirect [tonyc 5835]

* Mon Apr 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-08]
- Backout of last change. It belongs in e-smith-horde. [msoulier 8160]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-07]
- Restrict further directories from IMP access [gordonr 8160]

* Fri Mar 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-06]
- Fold back changes submitted by Dan Brown in 1.9.0-06db - hide option to change root
  folder, and allow choice about whether to include quoted message in
  reply. [charlieb 7694]

* Fri Mar 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Fix imap port/protocol specification. [charlieb 7893]
- Change Copyright => License in header. [charlieb]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-04]
- Deleted empty template-end files
- Deleted template-begin files, modified %build [lijied 3295]
- Deleted template-end files, modifed %build [lijied 3295]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-03]
- And delete dangling Alias directive [gordonr 5835]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-02]
- Remove IMP SSLonly page - do it as an Apache redirect [gordonr 5835]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-01]
- dev stream to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Rolling stable version number to 1.8.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-06]
- Fix path error for index.shtml, and reposition brace. [charlieb 4782].

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-05]
- Do template expansion of imp config files unconditionally in conf-imp.
  Set required GID and PERMS parameters. Only do conf-imp in
  bootstrap-console-save and email-update, and only do db initialisation
  at bootstrap-console-save time. [charlieb 4782]

* Mon Sep  9 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-04]
- Block non-SSL access via "backdoor" URLs when SSL-only mode is on [markk
  4646]

* Fri Aug 30 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-03]
- Remove Mail folder prefix which is now implicit in imapd. [charlieb 4412]

* Fri Aug 30 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-02]
- Remove "folder prefix" prompt [markk 4095]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Force STARTTLS to be ignored when logging on to IMAP [charlieb 4589]

* Mon Jul 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Create bootstrap-console-save conf-imp symlink. [charlieb 1939]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to development stream number to 1.7.0

* Thu May 30 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.9-01]
- Remove the version number from X-Sent-Via header [charlieb 3230]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.8-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.7-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Thu Apr 25 2002 Mark Knox <markk@e-smith.com>
- [1.6.6-01]
- Fixed conf-imp test logic that was causing script failures on a clean install
  [markk]

* Tue Apr 23 2002 Mark Knox <markk@e-smith.com>
- [1.6.5-01]
- Minor fix: Changed '\t' to a real tab in 410addressbook [markk 3230]

* Tue Apr 23 2002 Mark Knox <markk@e-smith.com>
- [1.6.4-01]
- Templated header.txt, trailer.txt, and prefs.php. Incorporated changes
  from Rich to activate "Expand Addresses" feature and include SME Server
  tagline in header. [markk 3230]

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [1.6.3-01]
- Make SSLonly directory so that templates will expand [markk]

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [1.6.2-01]
- Updated to handle IMP 3.0, using Dan Brown's contributed packages 
  [markk 2825]
- Updated conf-imp to process IMP 3.0 templates, converted to new DB APIs
  [markk 2825]
- Moved 30WebmailAliases fragment from e-smith-base [markk]

* Mon Apr 8 2002 Mark Knox <markk@e-smith.com>
- [1.6.1-01]
- rollRPM: Rolled version number to 1.6.1-01. Includes patches up to 1.6.0-04.

* Fri Jan 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-04]
- Remove %post and %postun events. They contain an incorrect path for "cut"
  and don't do anything. They aren't required either.

* Fri Jan 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.0-03]
- Adjusted Copyright notice on SSLonly html page

* Thu Jan  3 2002 Adrian Chung <adrianc@e-smith.com>
- [1.6.0-02]
- Remove 86ImpAlias fragment that generates global aliases.  We do this on
  a per VirtualHost basis now instead.
- Cleanup fragment code in 85ImpAccess and fix path:
  /home/e-smith/files/primary/html -> /home/httpd/html/horde/imp

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-02.

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-02]
- Provided empty template-begin to be HTML friendly
- Referenced new server-manager.jpg
- Changed text to be less technical

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches up to 1.4.2-01.

* Thu Nov 15 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.2-01]
- Rolled version number to 1.4.2-01. Includes patches up to 1.4.1-03.

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-03]
- Final branding cleanup

* Fri Aug 17 2001 gordonr
- [1.4.1-02]
- Autorebuild by rebuildRPM

* Fri Aug 17 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-01]
- Rolled version number to 1.4.1-01. Includes patches upto 1.4.0-03.

* Fri Aug 17 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Removed redundant event

* Tue Aug 14 2001 Adrian Chung <adrianc@e-smith.com>
- [1.4.0-02]
- Minor touch ups to the SSLonly index.html template.
- Make banner span width of browser window, remove
  excessive whitespace from left side of text.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-03.

* Wed Aug 8 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-03]
- Rebranding of the SSLonly index.shtml page

* Tue May 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-02]
- New optional property imp|....|SendmailPath which defaults to
  /usr/sbin/sendmail

* Tue May 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-05.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-05]
- Rolling release number for GPG signing.

* Mon Jan 29 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-04]
- move dependency check in conf-imp action inside of check to
  see if imp is enabled.

* Mon Jan 29 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- moved imp/SSLonly/index.html -> index.shtml so as to preserve
  URL that was used to access the page, and so it can be used in
  the "click here" link.
- modified conf-imp to expand index.shtml instead of index.html

* Fri Jan 26 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- changed dependency check in conf-imp so that the database
  entry is always initialized before checking dependencies 
  and expanding templates.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-14.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-14]
- changed action to 60 instead of 55.  Must happen after
  php and subsequently, horde.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-13]
- added dependency in conf-imp on both PHP and horde.

* Wed Jan 17 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-12]
- remove binaries that aren't installed from defaults.php
  includes: wvHtml, xlHtml, zipinfo
- add RPM mime type and path to RPM.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-11]
- properly template the index.html file in SSLonly.
- it no longer reads "www.tonez.cqa". :)

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-10]
- create directory SSLonly in spec file.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-9]
- added template index.html to html/horde/imp/SSLonly
- conf-imp expands it.

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-8]
- added email-update event link

* Tue Jan  9 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-7]
- fix typo in conf-imp

* Tue Jan  9 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-6]
- reserve 'webmail' in accounts database => conf-imp

* Mon Jan  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-5]
- clean up conf-imp script
- run conf-imp script from %post if in runlevel 7

* Thu Jan  4 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-4]
- conditionally expand 85ImpAccess and 86ImpAlias fragments dependant
  on service being enabled.
- default to disabled instead of enabled in conf-imp.

* Thu Jan  4 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-3]
- changed default.php3 template to save copies of sent mail in
  ~/Mail/sent-mail.

* Thu Dec 14 2000 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-2]
- updated 445userUseAddressBook to true

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-1]
- Rolled version to 1.1.0-1. Includes patches to 0.1-2

* Tue Nov 21 2000 Adrian Chung <adrianc@e-smith.com>
- Added /horde alias to httpd.conf template as well so that
  all graphics and libraries can be located.

* Tue Nov 14 2000 Adrian Chung <adrianc@e-smith.com>
- initial release

%description
This package adds necessary templates and configuration items
so that IMP will work properly.

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)