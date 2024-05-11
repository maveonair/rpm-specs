Name:           coredns
Version:        1.11.1
Release:        1%{?dist}
Summary:        CoreDNS is a DNS server that chains plugins
License:        Apache-2.0
URL:            https://github.com/coredns/%{name}

Source0:        https://github.com/coredns/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        Corefile
Source2:        %{name}.service


BuildRequires:  golang
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
CoreDNS is a DNS server that chains plugins

%global debug_package %{nil}

%prep
%autosetup

%build
make all

%pre
getent passwd %{name} >/dev/null || \
  useradd \
      --system --user-group --shell /sbin/nologin \
      --create-home --home-dir /var/lib/%{name} \
      --comment "CoreDNS is a DNS server that chains plugins" %{name}
exit 0

%install
# Binary
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# Configuration
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/Corefile

# systemd service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%check
go test -v ./...

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
/usr/sbin/userdel %{name}

%files
# Binary
%{_bindir}/%{name}

# Configuration
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/Corefile

# systemd
%{_unitdir}/%{name}.service

%changelog
* Sat May 11 2024 Fabian Mettler <dev@maveonair.com>
- Initial package creation of version 1.11.1
