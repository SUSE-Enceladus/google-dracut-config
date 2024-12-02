#
# spec file for package google-dracut-config
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           google-dracut-config
Version:        0.0.1
Release:        0
Summary:        Google Dracut config overlay files
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/google-dracut-config
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch

%description

%prep
%autosetup -p1

%build

%install
install -D -m 644 etc/dracut.conf.d/07-aws-type-switch.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/07-aws-type-switch.conf
install -D -m 644 etc/dracut.conf.d/07-dracut-nvme.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/07-dracut-nvme.conf
install -D -m 644 etc/dracut.conf.d/07-ext4.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/07-ext4.conf
install -D -m 644 etc/dracut.conf.d/07-virtio.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/07-virtio.conf
install -D -m 644 etc/dracut.conf.d/07-xfs.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/07-xfs.conf
install -D -m 644 etc/dracut.conf.d/11-resume.conf \
    %{buildroot}%{_sysconfdir}/dracut.conf.d/11-resume.conf

%check

%files
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/dracut.conf.d/
%config %{_sysconfdir}/dracut.conf.d/07-aws-type-switch.conf
%config %{_sysconfdir}/dracut.conf.d/07-dracut-nvme.conf
%config %{_sysconfdir}/dracut.conf.d/07-ext4.conf
%config %{_sysconfdir}/dracut.conf.d/07-virtio.conf
%config %{_sysconfdir}/dracut.conf.d/07-xfs.conf
%config %{_sysconfdir}/dracut.conf.d/11-resume.conf

%changelog

