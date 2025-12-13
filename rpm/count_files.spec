Name:		count-files
Version:	1.0
Release:	1%{?dist}
Summary:	Script for calculating files in /etc directory
License:	MIT
BuildArch:	noarch
Requires:	bash findutils coreutils
Source0:	count_files.sh

%description
This package provide file count_files.sh that calculate the number of files in /etc directory

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/count_files

%files
/usr/bin/count_files

%changelog
* Sat Dec 13 2025 Illya Moskat <moskat.illya17@gmail.com> - 1.0-1
- Initial build
