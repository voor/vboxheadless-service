%{?systemd_requires}
Name:           vboxheadless-service
Version:        1.0.4
Release:        1
Summary:        Unit file for running a VirtualBox Headless VM

Group:          System Environment/Base
License:        MIT
Vendor:         Robert Van Voorhees <rcvanvo@gmail.com>

Url:            https://www.virtualbox.org/wiki/VirtualBox
Requires:       VirtualBox
Requires(pre):  shadow-utils
BuildRequires:  systemd

Source0:        vboxheadless-service@.service
BuildArch:      noarch

%description
Unit file for a Headless VirtualBox VM.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/var/lib/vboxheadless/

install -p -m 644 %{SOURCE0} %{buildroot}/%{_unitdir}

%files
%attr(0644, root, root) %{_unitdir}/%{name}@.service
%attr(0755, vboxheadless, vboxusers) /var/lib/vboxheadless/

%pre
getent group vboxusers >/dev/null || groupadd -r vboxusers
getent passwd vboxheadless >/dev/null || \
    useradd -r -g vboxusers -d /var/lib/vboxheadless/ -s /sbin/nologin \
    -c "Service account for running Virtual Box instances" vboxheadless
exit 0

%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service

%changelog
* Mon May 29 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1.0.4-1
- Create the home directory

* Mon May 29 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1.0.2-1
- Create service user because nobody cannot create config files.

* Mon May 29 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1.0.1-1
- Forgot to add @ for user units.

* Mon May 29 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1-1
- Initial RPM release
