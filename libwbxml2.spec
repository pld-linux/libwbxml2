Summary:	Library and tools to parse, encode and handle WBXML documents
Name:		libwbxml2
Version:	0.9.2
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/wbxml2-%{version}+svn49synce.tar.gz
# Source0-md5:	07f659f41d529d9b89da4a86db1e0ee8
URL:		http://libwbxml.aymerick.com/
BuildRequires:	expat-devel >= 1.95.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for libwbxml2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel

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
%doc AUTHORS BUGS ChangeLog INSTALL NEWS README References THANKS TODO bootstrap
%attr(755,root,root) %{_bindir}/wbxml2xml
%attr(755,root,root) %{_bindir}/xml2wbxml
%attr(755,root,root) %{_libdir}/libwbxml2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwbxml2.la
%{_libdir}/libwbxml2.so
%{_includedir}/wbxml*.h
%{_pkgconfigdir}/libwbxml2.pc
