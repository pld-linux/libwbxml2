# TODO:
# - rename to synce-wbxml2 (contains synce modifications)
# - kill unecessary -lnsl etc.
# - lib is linked with -lexpat, but .pc specifies libxml2
Summary:	Library and tools to parse, encode and handle WBXML documents
Summary(pl.UTF-8):	Biblioteka i narzędzia do analizy, kodowania i obsługi dokumentów WBXML
Name:		libwbxml2
Version:	0.9.2
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/wbxml2-%{version}+svn49synce.tar.gz
# Source0-md5:	07f659f41d529d9b89da4a86db1e0ee8
URL:		http://libwbxml.aymerick.com/
BuildRequires:	expat-devel >= 1.95.8
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library and tools to parse, encode and handle WBXML documents.

%description -l pl.UTF-8
Biblioteka i narzędzia do analizy, kodowania i obsługi dokumentów
WBXML.

%package devel
Summary:	Header files for wbxml2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wbxml2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# CHECKME
Requires:	expat-devel
Requires:	popt-devel
Requires:	zlib-devel

%description devel
Header files for wbxml2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wbxml2.

%prep
%setup -q -n wbxml2-%{version}+svn49synce

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/wbxml2-%{version}*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README References THANKS TODO
%attr(755,root,root) %{_bindir}/wbxml2xml
%attr(755,root,root) %{_bindir}/xml2wbxml
%attr(755,root,root) %{_libdir}/libwbxml2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwbxml2.so
%{_libdir}/libwbxml2.la
%{_includedir}/wbxml*.h
%{_pkgconfigdir}/libwbxml2.pc
