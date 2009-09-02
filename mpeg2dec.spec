%define version 0.5.1
%define release %mkrel 2
%define name mpeg2dec
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name
%define oname libmpeg2

Summary:	MPEG-2 Decoder
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Video
Source0:	http://libmpeg2.sourceforge.net/files/%{oname}-%{version}.tar.gz
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

%package -n	%develname
Summary:	MPEG-2 Decoder development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %name 0

%description -n	%develname
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.
MPEG-2 Decoder development files

%package -n	%staticname
Summary:	MPEG-2 Decoder static libraries
Group:		Development/C
Requires:	%develname = %{version}-%release
Obsoletes:	%mklibname -s -d %name 0

%description -n %staticname
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

MPEG-2 Decoder static libraries.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x	--enable-shared \
%ifarch sparc sparcv9 sparc64
		--disable-accel-detect
%endif

%{make}

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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

%files -n %develname
%defattr(-,root,root)
%{_includedir}/mpeg2dec
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/lib*.pc
%files -n %staticname
%defattr(-,root,root)
%{_libdir}/lib*.a


