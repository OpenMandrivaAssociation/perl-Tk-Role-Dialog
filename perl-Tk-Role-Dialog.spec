%define upstream_name    Tk-Role-Dialog
%define upstream_version 1.101390

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Moose role for enhanced tk dialogs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::JPEG)
BuildRequires: perl(Tk::PNG)
BuildRequires: perl(Tk::Sugar)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


