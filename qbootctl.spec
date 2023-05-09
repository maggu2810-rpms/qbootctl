%global _vpath_srcdir %{name}-%{version}-0

Name:           qbootctl
Version:        0.1.2
Release:        1%{?dist}
Summary:        A port of the Qualcomm Android bootctrl HAL for musl/glibc userspace

License:        gpl
URL:            https://gitlab.com/sdm845-mainline/qbootctl
Source:         https://gitlab.com/maggu2810/%{name}/-/archive/%{version}-0/%{name}-%{version}-0.tar.gz

BuildRequires:  meson
BuildRequires:  g++
BuildRequires:  zlib-devel
BuildRequires:  systemd-rpm-macros

%description
qbootctl package description

%prep
%autosetup -c

%build
%meson
%meson_build
cat > %{name}-mark-boot-successful.service <<EOF
[Unit]
Description=Mark all boot slots as successful via qbootctl
After=multi-user.target

[Service]
ExecStart=%{_bindir}/%{name} -m

[Install]
WantedBy=multi-user.target
EOF

%install
%meson_install
%{__install} -p -m 0755 -d %{buildroot}%{_unitdir}
%{__install} -p -m 0644 %{name}-mark-boot-successful.service %{buildroot}%{_unitdir}/%{name}-mark-boot-successful.service

%check
%meson_test

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}-mark-boot-successful.service

%changelog
* Tue May 02 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial RPM

