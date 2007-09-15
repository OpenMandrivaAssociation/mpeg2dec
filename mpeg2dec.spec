%define version 0.4.1
%define release %mkrel 2
%define name mpeg2dec
%define major 0
%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandriva-release)
%if %mdkversion >= 910
%define libname %mklibname %name %major
%else
%define libname lib%name%major
%endif

Summary:	MPEG-2 Decoder
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Video
Source0:	http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.bz2
URL:		http://libmpeg2.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	libxv-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

%package -n	%{libname}
Group:		System/Libraries
Summary:	MPEG-2 Decoder

%description -n %{libname}
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

This package contains the shared libraries of mpeg2dec.

%package -n	%{libname}-devel
Summary:	MPEG-2 Decoder development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}


%description -n	%{libname}-devel
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.
MPEG-2 Decoder development files

%package -n	%{libname}-static-devel
Summary:	MPEG-2 Decoder static libraries
Group:		Development/C
Requires:	%{libname}-devel = %{version}

%description -n %{libname}-static-devel
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

MPEG-2 Decoder static libraries.

%prep
%setup -q

%build
%configure2_5x	--enable-shared \
%ifarch sparc sparcv9 sparc64
		--disable-accel-detect
%endif

%{make}

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/*
%{_bindir}/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libmpeg2*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%{_includedir}/mpeg2dec
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/lib*.pc
%files -n %libname-static-devel
%defattr(-,root,root)
%{_libdir}/lib*.a


