%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}
%define staticname %mklibname -s -d %{name}
%define oname libmpeg2

Summary:	MPEG-2 Decoder
Name:		mpeg2dec
Version:	0.5.1
Release:	11
License:	GPLv2+
Group:		Video
URL:		http://libmpeg2.sourceforge.net/
Source0:	http://libmpeg2.sourceforge.net/files/%{oname}-%{version}.tar.gz
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

%package -n	%{develname}
Summary:	MPEG-2 Decoder development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
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
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
mpeg2dec is an mpeg-1 and mpeg-2 video decoder. It is purposely kept
simple : it does not include features like reading files from a DVD,
CSS, fullscreen output, navigation, etc... The main purpose of
mpeg2dec is to have a simple test bed for libmpeg2. mpeg2dec also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams, and
output routines for a variety of different interfaces.

MPEG-2 Decoder static libraries.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build
%configure2_5x	--enable-shared \
%ifarch sparc sparcv9 sparc64
		--disable-accel-detect
%endif

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/*
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libmpeg2*.so.%{major}*

%files -n %{develname}
%{_includedir}/mpeg2dec
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/lib*.pc

%files -n %{staticname}
%{_libdir}/lib*.a

%changelog
* Mon May 14 2012 Götz Waschk <waschk@mandriva.org> 0.5.1-8mdv2012.0
+ Revision: 798719
- spec cleanup
- remove libtool archive
- yearly rebuild

* Fri May 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5.1-7
+ Revision: 674312
- Better correction to crash in SSE code with gcc 4.6.0-compiled mpeg2dec (#63279)

* Thu May 12 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5.1-6
+ Revision: 673986
- Correct crash in SSE code with gcc 4.6.0-compiled mpeg2dec (#63279)

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-5
+ Revision: 666488
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-4mdv2011.0
+ Revision: 606660
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-3mdv2010.1
+ Revision: 523384
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.1-2mdv2010.0
+ Revision: 426167
- rebuild

* Fri Jul 25 2008 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2009.0
+ Revision: 248835
- new version
- new devel names
- update license

* Tue Jul 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-6mdv2009.0
+ Revision: 232818
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-4mdv2008.1
+ Revision: 153256
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jun 06 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.4.1-2mdv2008.0
+ Revision: 36105
- Rebuild with libslang2.


* Sun Dec 17 2006 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2007.0
+ Revision: 98302
- Import mpeg2dec

* Sun Dec 17 2006 G�tz Waschk <waschk@mandriva.org> 0.4.1-1mdv2007.1
- fix buildrequires
- drop all patches
- New version 0.4.1

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.4.0b-5mdk
- Rebuild

* Mon Feb 14 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4.0b-4mdk
- libtool & x86_64 fixes

* Mon Dec 13 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.0b-3mdk
- --disable-accel-detect on sparc
- libtoolize
- spec cosmetics

* Fri May 14 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.4.0b-2mdk
- amd64 fixes, i.e. enforce check for -prefer-non-pic flags

* Mon May 03 2004 Stefan van der Eijk <stefan@mandrake,org> 0.4.0b-1mdk
- 0.4.0b

* Thu Feb 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-2mdk
- support mandrake 9.0

* Sun Jan 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- don't libtoolize
- new version

* Mon Dec 22 2003 Stefan van der Eijk <stefan@eijk.nu> 0.3.1-5mdk
- rebuild for new pkgconfig Requires
- removed redundant BuildRequires

