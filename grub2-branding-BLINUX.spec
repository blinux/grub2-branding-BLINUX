#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		grub2-branding-BLINUX
Version:        2.0
Release:        0
License:        BSD-2-Clause
Summary:	GRUB2 branding for BLINUX
Group:          System Environment/Base

Requires:	grub2
Conflicts:	otherproviders(grub2-branding)
Supplements:	packageand(grub2:branding-BLINUX)
Provides:       grub2-branding = %{version}

BuildArch:      noarch
BuildRequires:	grub2
Source0:        grub

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr
Vendor:		Blinux

%description
GRUB2 branding and config for BLINUX

%prep

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/default/
install -D -m 644 %{SOURCE0} %{buildroot}/%{_sysconfdir}/default/

%post
if [ -f %{_sysconfdir}/sysconfig/bootloader ]; then
  . %{_sysconfdir}/sysconfig/bootloader
fi
/sbin/update-bootloader --reinit 2>&1 | grep -q 'Unknown option: reinit' &&
/sbin/update-bootloader --refresh || true

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/default/grub

%changelog
* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Bump to 2.0

* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.1-0
- Bump to 1.1

* Sat Mar 29 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- package creation
