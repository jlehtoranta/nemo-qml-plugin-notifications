# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugin-notifications-qt5

# >> macros
# << macros

Summary:    Notifications plugin for Nemo Mobile
Version:    1.0.3
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-notifications
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)

%description
%{summary}.

%package devel
Summary:    Notifications support for C++ applications
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildRequires: qt5-qttools-qthelp-devel
BuildRequires: qt5-tools
BuildRequires: qt5-plugin-platform-minimal
BuildRequires: qt5-plugin-sqldriver-sqlite

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 VERSION=%{version}

make %{?jobs:-j%jobs}
make docs

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -R doc/html/* %{buildroot}/%{_docdir}/%{name}/

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libnemonotifications-qt5.so.*
%{_libdir}/qt5/qml/org/nemomobile/notifications/libnemonotifications.so
%{_libdir}/qt5/qml/org/nemomobile/notifications/qmldir
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/libnemonotifications-qt5.so
%{_libdir}/libnemonotifications-qt5.prl
%{_includedir}/nemonotifications-qt5/*.h
%{_libdir}/pkgconfig/nemonotifications-qt5.pc
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
