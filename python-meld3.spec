%global srcname meld3
%global sum HTML/XML templating system for Python

Summary: %{sum}
Name: python-%{srcname}
Version: 1.0.2
Release: 2%{?dist}

License: BSD
Group: Development/Languages
URL: https://github.com/Supervisor/%{srcname}
Source0: https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires: python2-devel python3-devel
BuildArch: noarch

%description
%{srcname} is an HTML/XML templating system for Python which keeps template
markup and dynamic rendering logic separate from one another.

This package contains common files for both Python 2 and Python 3 modules.

%package -n python2-%{srcname}
Summary:  %{sum}
Obsoletes: %{name} < 1.0.0
Conflicts: %{name} < 1.0.0
Conflicts: python < 2.5
Conflicts: python2 < 2.5
Requires: %{name} = %{version}-%{release}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{srcname} is an HTML/XML templating system for Python 2.5+ which keeps
template markup and dynamic rendering logic separate from one another.


%package -n python3-%{srcname}
Summary:  %{sum}
Requires: %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{srcname} is an HTML/XML templating system for Python 3.2+ which keeps
template markup and dynamic rendering logic separate from one another.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%clean
rm -rf %{buildroot}

%files
%doc README.txt CHANGES.txt
%license COPYRIGHT.txt LICENSE.txt

%files -n python2-%{srcname}
%{python2_sitelib}/*

%files -n python3-%{srcname}
%{python3_sitelib}/*

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Wed Apr 20 2016 Nils Philippsen <nils@redhat.com> - 1.0.2-1
- version 1.0.2
- change license to BSD
- package is noarch now
- ship Python 3 package (#1309618)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.6.7-5
- rebuild for gcc 4.7

* Tue Apr 05 2011 Nils Philippsen - 0.6.7-4
- patch in missing cmeld3.c file instead of indiscriminately (over-)writing it
- don't use macros for system executables (except python)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.7-1
- Update to solve a crasher bug on python-2.7:
  https://bugzilla.redhat.com/show_bug.cgi?id=652890
- Fix missing cmeld3.c file in the upstream tarball (upstream was notified).

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 Nils Philippsen <nils@redhat.com> - 0.6.5-1
- version 0.6.5
- drop obsolete etree patch

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.4-2
- Rebuild for Python 2.6

* Tue Feb 28 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.6.4-1
- Update to 0.6.4.
- Fix python-2.5 elementtree problem.

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 0.6.3-3
- Rebuild for gcc43

* Mon Jan 7 2008 Toshio Kuratomi <a.badger@gmail.com> 0.6.3-2
- Fix include egginfo when created.

* Wed Oct 17 2007 Toshio Kuratomi <a.badger@gmail.com> 0.6.3-1
- Update to 0.6.3 (Fix memory leaks).
- Update license tag.

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-3
- Release bump for rebuild

* Thu Apr 26 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-2.1
- Fix requires on python-elementtree for python-2.5.  (elementtree is included
  in python-2.5)

* Sun Apr 22 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-2
- Patch suggested in #153247

* Fri Apr 20 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-1
- Initial packaging

