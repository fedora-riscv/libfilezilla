Name: libfilezilla
Version: 0.17.1
Release: 1%{?dist}
URL: http://lib.filezilla-project.org/
Summary: C++ Library for FileZilla
License: GPLv2+
Source0: http://download.sourceforge.net/sourceforge/filezilla/%{name}-%{version}.tar.bz2
BuildRequires: gcc-c++ nettle-devel gnutls-devel gettext

%package devel
Summary: Development files for C++ Library for FileZilla
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

%description devel
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

This package contains files needed to compile code using libfilezilla.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libfilezilla.pc

%changelog
* Thu Jun 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.17.1-1
- 0.17.1

* Tue Apr 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.16.0-1
- 0.16.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15.1-1
- 0.15.1

* Fri Oct 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15.0-1
- 0.15.0

* Fri Oct 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.14.0-1
- 0.14.0

* Fri Sep 21 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.2-1
- 0.13.2.

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.1-1
- Latest upstream.

* Tue Jul 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.0-1
- Latest upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.3-1
- Latest upstream.

* Mon May 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.2-1
- Latest upstream.

* Fri Feb 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.1-1
- Latest upstream.

* Tue Feb 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.0-1
- Latest upstream.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.11.2-1
- Latest upstream.

* Wed Nov 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.1-1
- Latest upstream.

* Fri Sep 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.0-1
- Latest upstream.

* Mon Aug 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.10.1-1
- Latest upstream.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.10.0-1
- Latest upstream.

* Fri Jun 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.9.2-2
- Patch for filezilla build issue, from upstream.

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.9.2-1
- Latest upstream.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Feb 23 2017 Jon Ciesla <limburgher@gmail.com> - 0.9.1-1
- Latest upstream.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.0-1
- Latest upstream.

* Wed Oct 26 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.0-1
- Latest upstream.

* Mon Oct 03 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.1-1
- Latest upstream.

* Mon Sep 26 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- Latest upstream.

* Thu Jul 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.1-1
- Latest upstream.

* Thu Jul 21 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- Latest upstream.

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.3-1
- Latest upstream.

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.2-1
- Latest upstream.

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.0-1
- Latest upstream.

* Mon Apr 04 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.0.1-2
- Dropped buildroot, Group, buildroot scrup, and added --disable-static and
- isa-specific Requires.

* Tue Mar 15 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.0.1-1
- Initial package creation.
