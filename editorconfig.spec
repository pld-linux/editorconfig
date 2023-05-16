Summary:	EditorConfig core library and tool
Summary(pl.UTF-8):	Podstawowa biblioteka i narzędzie EditorConfig
Name:		editorconfig
Version:	0.12.6
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/editorconfig/editorconfig-core-c/releases
Source0:	https://github.com/editorconfig/editorconfig-core-c/archive/v%{version}/editorconfig-core-c-%{version}.tar.gz
# Source0-md5:	548f661d514b8a6b2161801212387a3c
URL:		https://editorconfig.org/
BuildRequires:	cmake >= 3.5.1
BuildRequires:	doxygen
BuildRequires:	pcre2-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different
projects. The EditorConfig project maintains a file format and plugins
for various text editors which allow this file format to be read and
used by those editors.

%description -l pl.UTF-8
EditorConfig ułatwia utrzymywanie właściwego stylu kodowania przy
przełączaniu się między różnymi edytorami tekstu oraz różnymi
projektami. Projekt EditorConfig utrzymuje format pliku oraz wtyczki
do różnych edytorów tekstu, pozwalające na wczytanie i używanie tego
formatu pliku przez obsługiwane edytory.

%package libs
Summary:	Library handling EditorConfig files
Summary(pl.UTF-8):	Biblioteka obsługująca pliki EditorConfig
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description libs
Library handling EditorConfig files, a file format defining coding
styles in projects.

%description libs -l pl.UTF-8
Biblioteka obsługująca pliki EditorConfig - format plików
definiujących styl kodowania w projektach.

%package devel
Summary:	Header files for EditorConfig library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki EditorConfig
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for EditorConfig library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki EditorConfig.

%package static
Summary:	Static EditorConfig library
Summary(pl.UTF-8):	Statyczna biblioteka EditorConfig
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EditorConfig library.

%description static -l pl.UTF-8
Statyczna biblioteka EditorConfig.

%package apidocs
Summary:	API documentation for EditorConfig library
Summary(pl.UTF-8):	Dokumentacja API biblioteki EditorConfig
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for EditorConfig library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki EditorConfig.

%prep
%setup -q -n editorconfig-core-c-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CONTRIBUTORS LICENSE README.md
%attr(755,root,root) %{_bindir}/editorconfig
%attr(755,root,root) %{_bindir}/editorconfig-%{version}
%{_mandir}/man1/editorconfig.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeditorconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeditorconfig.so.0
%{_mandir}/man5/editorconfig-format.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeditorconfig.so
%{_includedir}/editorconfig
%{_pkgconfigdir}/editorconfig.pc
%{_libdir}/cmake/EditorConfig
%{_mandir}/man3/editorconfig.h.3*
%{_mandir}/man3/editorconfig_handle.h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libeditorconfig_static.a

%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/{search,*.css,*.html,*.js,*.png}
