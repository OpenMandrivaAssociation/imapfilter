Summary:	Mail filtering utility
Name:		imapfilter
Version:	2.5.1
Release:	1
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
