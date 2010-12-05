Summary:	Mail filtering utility
Name:		imapfilter
Version:	2.2.2
Release: 	%mkrel 3
License:	MIT
Group:		Networking/Mail
URL:		http://imapfilter.hellug.gr/
Source:		http://imapfilter.hellug.gr/source/%{name}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%{name}-buildroot
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
./configure -d %{_prefix} -b %{_bindir} -s %{_datadir}/imapfilter -m %{_mandir}
%make MYCFLAGS="-Wall %{optflags}"


%install
rm -rf %buildroot
%makeinstall_std BINDIR=%{_bindir}\
	SHAREDIR=%{_datadir}/imapfilter\
	MANDIR=%{_mandir}

%clean
rm -rf %buildroot


%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README sample.config.lua sample.extend.lua
%_mandir/*/*
%_datadir/imapfilter
