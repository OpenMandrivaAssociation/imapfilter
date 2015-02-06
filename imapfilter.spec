Summary:	Mail filtering utility
Name:		imapfilter
Version:	2.5.2
Release:	2
License:	MIT
Group:		Networking/Mail
URL:		http://imapfilter.hellug.gr/
Source0:	http://imapfilter.hellug.gr/source/%{name}-%{version}.tar.gz
Buildrequires:	openssl-devel  pcre-devel
Buildrequires:	lua-devel

%description
IMAPFilter is a mail filtering utility. It connects to remote mail servers
using the Internet Message Access Protocol (IMAP). Based on the user defined
filters it checks messages residing on a remote IMAP mailbox and processes
them in various ways.

One can execute imapfilter before:
  * fetching of mail locally
  * accessing a mailbox using one of the available Mail User Agents (MUA)
  * browsing a mailbox via the Web
...in order to "clear" a mailbox and avoid downloading/seeing some specific
mails, copy and/or move messages between folders, etc.


%prep
%setup -q

%build
%make

%install
%makeinstall_std BINDIR=%{_bindir}\
	SHAREDIR=%{_datadir}/imapfilter\
	MANDIR=%{_mandir}

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README
%_mandir/*/*
%_datadir/imapfilter


%changelog
* Thu Mar 01 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.2-1
+ Revision: 781542
- version update 2.5.2

* Tue Feb 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.1-1
+ Revision: 781266
- version update 2.5.1

* Fri Feb 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5-1
+ Revision: 780116
- version update 2.5

* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-2
+ Revision: 772994
- relink against libpcre.so.1

* Fri Jan 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.4.2-1
+ Revision: 762986
- version update 2.4.2

* Fri Dec 09 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.4.1-1
+ Revision: 740007
- version update 2.4.1

* Wed Dec 07 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.4-1
+ Revision: 738571
- package update 2.4

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-3mdv2011.0
+ Revision: 611180
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 2.2.2-2mdv2010.1
+ Revision: 537366
- rebuild

* Sat Jan 23 2010 Frederik Himpe <fhimpe@mandriva.org> 2.2.2-1mdv2010.1
+ Revision: 495305
- update to new version 2.2.2

* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 494630
- update to new version 2.2.1

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 2.2-2mdv2010.1
+ Revision: 494378
- Fix BuildRequires
- Update to new version 2.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3-4mdv2009.0
+ Revision: 247213
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3-2mdv2008.1
+ Revision: 170896
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 27 2007 Michael Scherer <misc@mandriva.org> 2.0.3-1mdv2008.0
+ Revision: 56342
- upgrade to 2.0.3
- Import imapfilter

