%define name	libopendaap
%define version	0.4.0
%define release  %mkrel 5

%define major	0
%define libname %mklibname opendaap %major

Name: 	 	%{name}
Summary: 	Library to interface with iTunes® music
Version: 	%{version}
Release: 	%{release}

Source:		http://crazney.net/programs/itunes/files/%{name}-%{version}.tar.bz2
URL:		http://crazney.net/programs/itunes/libopendaap.html
License:	BSD
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This library enables applications to discover, and connect to, iTunes® music
shares.  Unlike all other daap implementations, this library is able to
connect to recent iTunes shares which require a special authentication
algorithm.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	libopendaap-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

