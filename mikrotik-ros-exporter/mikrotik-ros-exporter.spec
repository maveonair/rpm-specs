Name:           mikrotik-ros-exporter
Version:        0.3.0
Release:        1%{?dist}
Summary:        A simple Prometheus exporter for Mikrotik RouterOS devices
License:        MIT
URL:            https://github.com/eatplanted/%{name}

Source0:        https://github.com/eatplanted/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        config.yml
Source2:        %{name}.service


BuildRequires:  git
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
A simple Prometheus exporter for Mikrotik RouterOS devices

%global debug_package %{nil}

%prep
%autosetup

%build
go build -v -o ./dist/%{name} cmd/%{name}/main.go

%pre
getent passwd %{name} >/dev/null || \
  useradd \
      --system --user-group --shell /sbin/nologin \
      --home-dir /var/lib/%{name} \
      --comment "Mikrotik RouterOS Exporter" %{name}
exit 0

%install
# Binary
install -Dpm 0755 dist/%{name} %{buildroot}%{_bindir}/%{name}

# Configuration
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/config.yml

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
%config(noreplace) %{_sysconfdir}/%{name}/config.yml

# systemd
%{_unitdir}/%{name}.service

%changelog
* Sat Oct 21 2023 Fabian Mettler <dev@maveonair.com>
- Initial package creation of version 0.3.0
