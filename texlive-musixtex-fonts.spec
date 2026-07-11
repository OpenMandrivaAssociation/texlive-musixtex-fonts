%global tl_name musixtex-fonts
%global tl_revision 65517

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts used by MusixTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/musixtex-fonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These are fonts for use with MusixTeX; they are provided both as
original Metafont source, and as converted Adobe Type 1. The bundle
renders the older (Type 1 fonts only) bundle musixtex-t1fonts obsolete.

