Summary:	GNOME 2 visual diff and merge tool
Name:		meld
Version:	3.16.1
Release:	1
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
License:	GPLv2+
URL:		http://meld.sourceforge.net/
Group:		File tools
BuildRequires:	scrollkeeper
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:desktop-file-utils
Requires:	pygtk2.0
Requires:	python-gtksourceview
Requires:	python-gobject
Requires:	patch
BuildArch:	noarch
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3


%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges.
The margins show location of changes for easy navigation, and it also
features a tabbed interface that allows you to open many diffs at once.

%prep
%setup -q

%build
%make prefix=%_prefix libdir=%_datadir

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std prefix=%_prefix libdir=%_datadir

%find_lang %name --with-gnome

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


rm -rf %buildroot/usr/var/lib/scrollkeeper

%files -f %name.lang
%doc  NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%_datadir/icons/hicolor/*/apps/meld.*
%{_datadir}/icons/HighContrast/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/appdata/meld.appdata.xml
