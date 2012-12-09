# revision 24517
# category Package
# catalog-ctan /fonts/musixtex-fonts
# catalog-date 2011-10-27 10:28:55 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-musixtex-fonts
Version:	20111027
Release:	2
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
%{_texmfdistdir}/fonts/map/dvips/musixtex-fonts/musix.map
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musexgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix25.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musix29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musixgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musixsps.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/musixspx.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/mxsk.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xdrawsl.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xdrawzl.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg25.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreg29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xgreggen.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsld29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsldd20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xsldu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslgend.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslgenu.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhd29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhu29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhz-o.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhz.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhz20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslhz20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu11.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu13.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu16.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu24.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu29.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslu29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslud20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslup20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslz.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslz20.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xslz20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex-fonts/xtie20.mf
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix25.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musix29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musixsps.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/musixspx.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/mxsk.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xgreg29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsld29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsldd20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xsldu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhd29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu20m.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhu29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhz20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslhz20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslu29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslud20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslup20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslz20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xslz20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex-fonts/xtie20.tfm
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musix29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musixsps.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/musixspx.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/mxsk.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xgreg29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsld29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsldd20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xsldu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhd29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhu29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhz20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslhz20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslu29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslud20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslup20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslz20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xslz20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex-fonts/xtie20.pfb
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/CHANGES.psfonts
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/README
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/README.psfonts
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/gpl.txt
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/musixtex-fonts-install.pdf
%doc %{_texmfdistdir}/doc/fonts/musixtex-fonts/musixtex-fonts-install.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111027-2
+ Revision: 754237
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111027-1
+ Revision: 729689
- texlive-musixtex-fonts
- texlive-musixtex-fonts

