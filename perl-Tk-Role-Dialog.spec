%define upstream_name    Tk-Role-Dialog
%define upstream_version 1.101480

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Moose role for enhanced tk dialogs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tk)
BuildRequires:	perl(Tk::JPEG)
BuildRequires:	perl(Tk::PNG)
BuildRequires:	perl(Tk::Sugar)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

%description
the Tk::Role::Dialog manpage is meant to be used as a the Moose manpage
role to be composed for easy the Tk manpage dialogs creation.

It will create a new toplevel with a title, and possibly a header as well
as some buttons.

The attributes (see below) can be either defined as defaults using the
'_build_attr()' methods, or passed arguments to the constructor call. The
only mandatory attribute is 'parent', but you'd better provide some other
attributes if you want your dialog to be somehow usable! :-)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.101.480-2mdv2011.0
+ Revision: 658555
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.480-1mdv2011.0
+ Revision: 551925
- adding missing buildrequires:
- update to 1.101480
- import perl-Tk-Role-Dialog


* Wed May 19 2010 cpan2dist 1.101381-1mdv
- initial mdv release, generated with cpan2dist
