%define upstream_name    Linux-Distribution
%define upstream_version 0.20

Summary:	Mudule for Linux distribution
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LINUX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl extension to guess on which Linux distribution we are running.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Linux
%{_mandir}/man3/*


%changelog
* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 612366
- new version

* Fri Jan 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.140_100-1mdv2011.0
+ Revision: 484901
- disable tests because they fails on chroot
- import perl-Linux-Distribution


