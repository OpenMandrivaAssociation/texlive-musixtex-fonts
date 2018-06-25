Name:		texlive-musixtex-fonts
Version:	20180303
Release:	1
Summary:	Fonts used by MusixTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/musixtex-fonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex-fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex-fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These are fonts for use with MusixTeX; they are provided both
as original Metafont source, and as converted Adobe Type 1. The
bundle renders the older (Type 1 fonts only) bundle musixtex-
t1fonts obsolete.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/musixtex-fonts
%{_texmfdistdir}/fonts/source/public/musixtex-fonts
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
