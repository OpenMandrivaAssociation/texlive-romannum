# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/romannum
# catalog-date 2009-09-03 13:00:14 +0200
# catalog-license lppl
# catalog-version 1.0b
Name:		texlive-romannum
Version:	1.0b
Release:	2
Summary:	Generate roman numerals instead of arabic digits
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/romannum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The romannum package changes LaTeX generated numbers to be
printed with roman numerals instead of arabic digits. It
requires the stdclsdv package. Users of the bookhands fonts may
find this package useful.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/romannum/romannum.sty
%doc %{_texmfdistdir}/doc/latex/romannum/README
%doc %{_texmfdistdir}/doc/latex/romannum/romannum.pdf
#- source
%doc %{_texmfdistdir}/source/latex/romannum/romannum.dtx
%doc %{_texmfdistdir}/source/latex/romannum/romannum.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-2
+ Revision: 755723
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-1
+ Revision: 719461
- texlive-romannum
- texlive-romannum
- texlive-romannum
- texlive-romannum

