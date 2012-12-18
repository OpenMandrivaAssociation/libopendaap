%define major	0
%define libname %mklibname opendaap %{major}
%define devname %mklibname opendaap -d

Name: 	 	libopendaap
Summary: 	Library to interface with iTunes® music
Version: 	0.4.0
Release: 	7
License:	BSD
Group:		System/Libraries
URL:		http://crazney.net/programs/itunes/libopendaap.html
Source0:	http://crazney.net/programs/itunes/files/%{name}-%{version}.tar.bz2

%description
This library enables applications to discover, and connect to, iTunes® music
shares.  Unlike all other daap implementations, this library is able to
connect to recent iTunes shares which require a special authentication
algorithm.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{devname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make
										
%install
%makeinstall

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

