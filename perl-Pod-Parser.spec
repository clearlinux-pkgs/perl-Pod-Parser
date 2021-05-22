#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Parser
Version  : 1.63
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-1.63.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-1.63.tar.gz
Summary  : Modules for parsing/translating POD format documents
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Pod-Parser-bin = %{version}-%{release}
Requires: perl-Pod-Parser-man = %{version}-%{release}
Requires: perl-Pod-Parser-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
WHAT IS THIS?
=============
This software distribution contains the following packages for using
Perl5 "pod" (Plain Old Documentation).  See the "perlpod" and "perlsyn"
manual pages from your Perl5 distribution for more information about pod.

%package bin
Summary: bin components for the perl-Pod-Parser package.
Group: Binaries

%description bin
bin components for the perl-Pod-Parser package.


%package dev
Summary: dev components for the perl-Pod-Parser package.
Group: Development
Requires: perl-Pod-Parser-bin = %{version}-%{release}
Provides: perl-Pod-Parser-devel = %{version}-%{release}
Requires: perl-Pod-Parser = %{version}-%{release}

%description dev
dev components for the perl-Pod-Parser package.


%package man
Summary: man components for the perl-Pod-Parser package.
Group: Default

%description man
man components for the perl-Pod-Parser package.


%package perl
Summary: perl components for the perl-Pod-Parser package.
Group: Default
Requires: perl-Pod-Parser = %{version}-%{release}

%description perl
perl components for the perl-Pod-Parser package.


%prep
%setup -q -n Pod-Parser-1.63
cd %{_builddir}/Pod-Parser-1.63

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/podselect

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Find.3
/usr/share/man/man3/Pod::InputObjects.3
/usr/share/man/man3/Pod::ParseUtils.3
/usr/share/man/man3/Pod::Parser.3
/usr/share/man/man3/Pod::PlainText.3
/usr/share/man/man3/Pod::Select.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/podselect.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Pod/Find.pm
/usr/lib/perl5/vendor_perl/5.34.0/Pod/InputObjects.pm
/usr/lib/perl5/vendor_perl/5.34.0/Pod/ParseUtils.pm
/usr/lib/perl5/vendor_perl/5.34.0/Pod/Parser.pm
/usr/lib/perl5/vendor_perl/5.34.0/Pod/PlainText.pm
/usr/lib/perl5/vendor_perl/5.34.0/Pod/Select.pm
