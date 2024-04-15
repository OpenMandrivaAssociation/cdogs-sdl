Name:           cdogs-sdl
Version:        2.1.0
Release:        1
Summary:        Open source, classic overhead run-and-gun game
Group:          Games/Arcade
License:        GPLv2 and BSD and CC0 and CC-BY and CC-BY-SA
URL:            https://cxong.github.io/cdogs-sdl
Source0:        https://github.com/cxong/cdogs-sdl/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         cdogs-sdl-disable-werror.patch
Patch1:         fix-build.patch
# https://github.com/cxong/cdogs-sdl/issues/729
#Patch2:         fix-source-file-directory.patch

BuildRequires:  cmake
BuildRequires:  ccache
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  python3dist(protobuf)

Provides:       bundled(yajl) == 2.1.0

%description
C-Dogs SDL is a classic overhead run-and-gun game, supporting up to
4 players in co-op and deathmatch modes. Customize your player, choose
from up to 11 weapons, and try over 100 user-created campaigns. Have fun!

%prep
%autosetup -p1

rm -rf src/cdogs/enet

%build
%cmake \
  -DCDOGS_BIN_DIR=%{_gamesbindir} \
  -DCDOGS_DATA_DIR=%{_gamesdatadir}/%{name}/ \
  -DOpenGL_GL_PREFERENCE=GLVND \
  -DUSE_SHARED_ENET=ON
%make_build

%install
%make_install -C build

%files
%doc README.md doc/AUTHORS doc/README_DATA.md doc/original_readme.txt
%{_datadir}/applications/io.github.cxong.%{name}.desktop
%{_datadir}/metainfo/io.github.cxong.%{name}.appdata.xml
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-editor
%{_gamesdatadir}/%{name}/
%{_iconsdir}/hicolor/*/apps/io.github.cxong.%{name}.png
