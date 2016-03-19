%define oname mpeg2
%define major 0
%define libname %mklibname %{oname}_ %{major}
%define libconvert %mklibname %{oname}convert %{major}
%define devname %mklibname -d %{oname}

Summary:	MPEG-2 Decoder
Name:		mpeg2dec
Version:	0.5.1
Release:	25
License:	GPLv2+
Group:		Video
Url:		http://libmpeg2.sourceforge.net/
Source0:	http://libmpeg2.sourceforge.net/files/lib%{oname}-%{version}.tar.gz
Patch0:		libmpeg2-0.5.1-gcc4.6.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xv)

%description
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

%package -n	%{libname}
Summary:	MPEG-2 Decoder
Group:		System/Libraries
Obsoletes:	%{_lib}mpeg2dec0 < 0.5.1-12

%description -n %{libname}
This package contains a shared library of mpeg2dec.

%package -n	%{libconvert}
Summary:	MPEG-2 Decoder
Group:		System/Libraries
Obsoletes:	%{_lib}mpeg2dec0 < 0.5.1-12

%description -n %{libconvert}
This package contains a shared library of mpeg2dec.

%package -n	%{devname}
Summary:	MPEG-2 Decoder development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libconvert} = %{version}-%{release}
Provides:	lib%{oname}-devel = %{version}-%{release}
Obsoletes:	%{_lib}mpeg2dec0 < 0.5.1-12

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn lib%{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-shared

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/*
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libmpeg2.so.%{major}*

%files -n %{libconvert}
%{_libdir}/libmpeg2convert.so.%{major}*

%files -n %{devname}
%{_includedir}/mpeg2dec
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/lib*.pc

