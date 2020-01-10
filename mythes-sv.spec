Name: mythes-sv
Summary: Swedish thesaurus
Version: 1.3
Release: 5%{?dist}
Source: http://extensions.services.openoffice.org/files/934/3/SwedishThesaurus.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/SweThes
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: MIT
BuildArch: noarch
Requires: mythes

%description
Swedish thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_sv_SE.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.dat
cp -p dictionaries/th_sv_SE.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s th_sv_SE_v2.dat "th_"$lang"_v2.dat"
        ln -s th_sv_SE_v2.idx "th_"$lang"_v2.idx"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Info-en.txt
%{_datadir}/mythes/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 10 2010 Caolán McNamara <caolanm@redhat.com> - 1.3-1
- mythes now owns /usr/share/mythes

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 1.2-3
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Caolán McNamara <caolanm@redhat.com> - 1.2-1
- latest version

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090225-1
- initial version
