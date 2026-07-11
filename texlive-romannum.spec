%global tl_name romannum
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0b
Release:	%{tl_revision}.1
Summary:	Generate roman numerals instead of arabic digits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/romannum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romannum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The romannum package changes LaTeX generated numbers to be printed with
roman numerals instead of arabic digits. It requires the stdclsdv
package. Users of the bookhands fonts may find this package useful.

