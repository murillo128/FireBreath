Name: log4cplus
Version: 1.1.0
Release: 1

Summary: log4cplus, C++ logging library
License: Apache
Group: Development/Libraries
Vendor: log4cplus project 
Packager: Yusuke SATO <y-sato@y-sa.to>
Url: http://log4cplus.sourceforge.net/

Source: %name-%version.tar.gz

Prefix: %_prefix
BuildRoot: %_tmppath/%name-%version-root

%description
log4cplus is a simple to use C++ logging API providing thread-safe, 
flexible, and arbitrarily granular control over log management and 
configuration. It is modeled after the Java log4j API.

%package devel
Summary: log4cplus headers, static libraries
Group: Development/Libraries
Requires: %name = %version

%description devel
log4cplus is a simple to use C++ logging API providing thread-safe, 
flexible, and arbitrarily granular control over log management and 
configuration. It is modeled after the Java log4j API.

%prep
rm -rf $RPM_BUILD_ROOT

%setup
./configure --prefix=%{prefix} --with-working-locale CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install
mkdir -p $RPM_BUILD_ROOT%{prefix}/include/
cp -rp include/log4cplus $RPM_BUILD_ROOT%{prefix}/include/
rm -f $RPM_BUILD_ROOT%{prefix}/include/log4cplus/config/stamp-*
rm -f $RPM_BUILD_ROOT%{prefix}/include/log4cplus/config/*.in
rm -f $RPM_BUILD_ROOT%{prefix}/include/log4cplus/stamp-*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%attr(755,root,root) %prefix/lib/lib*.so*
%attr(644,root,root) %prefix/lib/*.la

%files devel
%defattr(-,root,root,755)
%prefix/include/log4cplus/*.h
%prefix/include/log4cplus/helpers/*.h
%prefix/include/log4cplus/spi/*.h
%attr(644,root,root) %prefix/lib/*.a
