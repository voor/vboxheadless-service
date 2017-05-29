%{?systemd_requires}
# Upstream package name naturally contains an underscore
Name:           vboxheadless-service
Version:        1
Release:        1
Summary:        Unit file for running a VirtualBox Headless VM

Group:          System Environment/Base
License:        MIT
Vendor:         Robert Van Voorhees <rcvanvo@gmail.com>

Url:            https://www.virtualbox.org/wiki/VirtualBox
Requires:       VirtualBox
BuildRequires:  systemd

Source0:        vboxheadless-service.service
BuildArch:      noarch

%description
Unit file for a Headless VirtualBox VM.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/%{_unitdir}

install -p -m 644 %{SOURCE0} %{buildroot}/%{_unitdir}

%files
%attr(0644, root, root) %{_unitdir}/%{name}.service

%pre

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Mon May 29 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1-1
- Initial RPM release
