Name: tpm2-tools
Version: 4.1.1
Release: 5%{?dist}
Summary: A TPM2.0 testing tool build upon TPM2.0-TSS

License: BSD
URL:     https://github.com/tpm2-software/tpm2-tools
Source0: https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:  0001-tpm2_hierarchycontrol-Fixed-bug-where-hierarchycontr.patch
Patch1:  0001-tpm2_nvdefine.c-Fixed-error-reporting-message.patch
Patch2:  0001-tpm2_policyor-Silent-failure-bug-fix-for-invalid-uns.patch
Patch3:  0001-tpm2_alg_util.c-fix-a-bug-where-the-string-rsa3072-w.patch
Patch4:  0001-Fix-ESYS_TR-hierarchy-transition.patch
Patch5:  0001-Refactor-fix_esys_hierarchies.patch
Patch6:  0001-tpm2_create.c-Fix-an-issue-where-userwithauth-attr-c.patch
Patch7:  0001-tpm2_getekcertificate-add-default-web-address.patch
Patch8:  0001-lib-files-fix-an-error-message-in-files_load_-name.patch
Patch9:  0001-tpm2_policy.c-restrict-policy-digest-size.patch
Patch10: 0001-tpm2_policycountertimer-Fix-an-issue-where-operandB-.patch
Patch11: 0001-tools-tpm2_nvcertify.c-Fix-incompatible-pointer-cast.patch
Patch12: 0001-tools-tpm2_nvreadpublic-Fix-resource-leak.patch
Patch13: 0001-lib-files.c-Fix-an-issue-where-execution-could-not-r.patch
Patch14: 0001-tpm2_import-fix-fixed-AES-key-CVE-2021-3565.patch

BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: pandoc
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl)
# tpm2-tss-devel provides tss2-mu/sys/esys package config
BuildRequires: pkgconfig(tss2-mu)
BuildRequires: pkgconfig(tss2-sys)
BuildRequires: pkgconfig(tss2-esys)

# tpm2-tools is heavily depending on TPM2.0-TSS project, matched tss is required
Requires: tpm2-tss%{?_isa} >= 2.3.2-1%{?dist}

# tpm2-tools project changed the install path for binaries and man page section
Obsoletes: tpm2-tools <= 2.1.1-2

%description
tpm2-tools is a batch of testing tools for tpm2.0. It is based on tpm2-tss.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure --prefix=/usr --disable-static --disable-silent-rules
%make_build

%install
%make_install

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/tpm2_*
%{_datadir}/bash-completion/completions/tpm2*
%{_mandir}/man1/tpm2_*.1.gz

%changelog
* Mon Aug 09 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 4.1.1-5
- Bump nvr to trigger osci.
resolves: rhbz#1965981

* Tue Jun 01 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 4.1.1-4
- Fix CVE-2021-3565
resolves: rhbz#1965981

* Fri May 14 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 4.1.1-3
- Fix resource leak.
- Fix to restrict policy digest size.
- Fix incompatible pointer cast.
- Fix error message in files_load_##name
- Fix issue where execution couldn't reach function return.
resolves: rhbz#1920821

* Mon Nov 16 2020 Jerry Snitselaar <jsnitsel@redhat.com> - 4.1.1-2
- Fix ESYS_TR hierarchy transition.
- Refactor fix_esys_hierarchies to return actual TSS2_RC return code.
- tpm2_alg_util.c: fix a bug where the string rsa3072 wasn't being parsed.
- tpm2_create.c: Fix an issue where userwithauth attr cleared if policy specified.
- tpm2_hierarchycontrol: Fix bug where hierarchycontrol operation failed silently.
- tpm2_nvdefine.c: Fix error reporting message.
- tpm2_policyor: Fix silent failure for invalid/unspecified policy digest alg.
resolves: rhbz#1854774

* Wed Apr 29 2020 Jerry Snitselaar <jsnitsel@redhat.com> - 4.1.1-1
- Update to 4.1.1 release
resolves: rhbz#1789682

* Tue Oct 22 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.2.1-1
- Update to 3.2.1 release
resolves: rhbz#1725714

* Tue May 28 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.4-5
- Another dependency needed for CI gating
resolves: rhbz#1682417

* Tue May 28 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.4-4
- Fix CI dependency
resolves: rhbz#1682417

* Tue May 28 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.4-3
- Add CI gating test
resolves: rhbz#1682417

* Tue May 14 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.4-2
- Add initial CI gating support
resolves: rhbz#1682417

* Tue Apr 30 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.4-1
- Rebase to 3.1.4 release.
resolves: rhbz#1664498

* Thu Nov 08 2018 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1.1-4
- lib/tpm2_options: restore TCTI configuration environment variables
- tpm2_getcap: restore tool output to print properties with TPM_PT prefix
resolves: rhbz#1648001

* Sat Jul 14 2018 Javier Martinez Canillas <javierm@redhat.com> - - 3.1.1-3
- Revert backward incompatible change that removes default object attributes

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Yunying Sun <yunying.sun@intel.com> - 3.1.1-1
- Update to 3.1.1 release

* Thu Jul 5 2018 Yunying Sun <yunying.sun@intel.com> - 3.1.0-1
- Update Requires version of tpm2-tss to 2.0.0
- Remove BuildRequires for tcti-abrmd since it is optional
- Remove BuildRequires for tcti-{device,mssim} as it is now dynamically loaded
- Update to 3.1.0 release

* Mon Apr 30 2018 Javier Martinez Canillas <javierm@redhat.com> - 3.0.4-1
- Update URLs to point to the new project location
- Update to 3.0.4 release

* Wed Feb 21 2018 Javier Martinez Canillas <javierm@redhat.com> - 3.0.3-3
- Remove ExclusiveArch: x86_64 directive

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Javier Martinez Canillas <javierm@redhat.com> - 3.0.3-1
- Update to 3.0.3 release

* Mon Dec 18 2017 Javier Martinez Canillas <javierm@redhat.com> - 3.0.2-1
- Update to 3.0.2 release

* Tue Dec 12 2017 Javier Martinez Canillas <javierm@redhat.com> - 3.0.1-1
- Update to 3.0.1 release (RHBZ#1512743)
- Download the generated tarball provided instead of the source code tarball

* Fri Dec 08 2017 Javier Martinez Canillas <javierm@redhat.com> - 3.0-1
- Update to 3.0 release

* Wed Nov 29 2017 Javier Martinez Canillas <javierm@redhat.com> - 3.0-0.1.rc1
- Update to 3.0 release candidate 1
- Update URLs to point to the new project location
- Make the package to obsolete version 2.1.1

* Wed Nov 01 2017 Javier Martinez Canillas <javierm@redhat.com> - 2.1.1-1
- Rename remaining tpm2.0-tools prefixes to tpm2-tools
- Remove global pkg_prefix since now the upstream repo and package names match
- Remove downstream patches since now these are in the latest upstream release
- Update to 2.1.1 release (RHBZ#1504438)

* Thu Oct 19 2017 Jerry Snitselaar <jsnitsel@redhat.com> - 2.1.0-7
- Clean up potential memleak (RHBZ#1503959)

* Thu Oct 05 2017 Javier Martinez Canillas <javierm@redhat.com> - 2.1.0-6
- Add tpm2-abrmd-devel BuildRequires so tools have abrmd support (RHBZ#1498909)

* Fri Aug 18 2017 Javier Martinez Canillas <javierm@redhat.com> - 2.1.0-5
- Remove unneeded source tarballs (RHBZ#1482830)

* Tue Aug 15 2017 Sun Yunying <yunying.sun@intel.com> - 2.1.0-4
- Add patch to fix build error when openssl-devel is installed(RHBZ#1481236)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Sun Yunying <yunying.sun@intel.com> - 2.1.0-2
- Add patch to fix gcc7 complaining about implicit-fallthrough cases

* Fri Jul 28 2017 Sun Yunying <yunying.sun@intel.com> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Fri Jul 28 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-9
- Update Requires dependency so that tpm2-tss update won't break tpm2-tools

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-7
- Only update release version to make fedpkg build works for f26

* Wed Mar 1 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-6
- Update tpm2-tss version to 1.0-3 to fix broken dependency on f26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-4
- Dependency check failed for Requires again, here to fix this
- Update release version and changelog

* Thu Jan 19 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-3
- Change spec file permission to 644 to avoid rpmlint complain
- Update Requires to fix dependency check error reported in Bodhi
- Remove tpm2-tss-devel version in BuildRequires comment
- Update release version and changelog

* Wed Dec 21 2016 Sun Yunying <yunying.sun@intel.com> - 1.1.0-2
- Remove pkg_version to avoid dupliate use of version
- Remove redundant BuildRequires for autoconf/automake/pkgconfig
- Add comments for BuildRequires of sapi/tcti-device/tcti-socket
- Use ExclusiveArch instead of ExcludeArch
- Requires tpm2-tss version updated to 1.0-2
- Updated release version and changelog

* Fri Dec 2 2016 Sun Yunying <yunying.sun@intel.com> - 1.1.0-1
- Initial version of the package
