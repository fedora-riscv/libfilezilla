Name: libfilezilla
Version: 0.11.2
Release: 1%{?dist}
URL: http://lib.filezilla-project.org/
Summary: C++ Library for FileZilla
License: GPLv2+
Source0: http://download.sourceforge.net/sourceforge/filezilla/%{name}-%{version}.tar.bz2

%package devel
Summary: Development files for C++ Library for FileZilla
Group: Development/Libraries
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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libfilezilla.pc

%changelog
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
