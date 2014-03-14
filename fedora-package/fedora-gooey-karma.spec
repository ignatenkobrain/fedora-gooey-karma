%global commit 1e27c830f1a49b37d92855bd75f3a50911539b9d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fedora-gooey-karma
Version:        0.1
Release:        3%{?dist}
Summary:        GUI tool for sending feedback about installed Test Update packages

Group:          Development/Tools
License:        GPLv3+
URL:            https://fedoraproject.org/wiki/Fedora_Gooey_Karma

Source0:        https://github.com/blaskovic/fedora-gooey-karma/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
BuildRequires:  asciidoc
BuildRequires:  libxslt

Requires:       python-fedora
Requires:       fedora-cert
Requires:       yum
Requires:       yum-utils
Requires:       bodhi-client
Requires:       python-pyside
Requires:       python-keyring
Requires:       koji
Requires:       hicolor-icon-theme

%description
Fedora-gooey-karma helps you to easily and fast provide feedback for all testing
updates that you have currently installed and browse the available ones. It is
similar tool to fedora-easy-karma but with graphical front-end.

%prep
%setup -q -n %{name}-%{commit}

%build
a2x -d manpage -f manpage man/fedora-gooey-karma.1.asciidoc

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%install
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} DATADIR=%{_datadir}
desktop-file-validate %{buildroot}/%{_datadir}/applications/fedora-gooey-karma.desktop
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/fedora-gooey-karma.1 %{buildroot}/%{_mandir}/man1/

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/fedora-gooey-karma.1*

%changelog
* Fri Mar 14 2014 Branislav Blaskovic <branislav@blaskovic.sk> - 0.1-3
- Fixed UnicodeEncodeError issue #28
- Require for hicolor-icon-theme added
- Man page added

* Mon Dec 9 2013 Branislav Blaskovic <branislav@blaskovic.sk> - 0.1-2
- python2-devel added as build requires
- removed deletion of buildroot dir

* Fri Oct 18 2013 Branislav Blaskovic <branislav@blaskovic.sk> - 0.1-1
- Initial spec file
