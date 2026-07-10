%global tl_name atableau
%global tl_revision 79517

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.2
Release:	%{tl_revision}.1
Summary:	A LaTeX package for symmetric group combinatorics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/atableau
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atableau.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atableau.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(l3kernel)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for symmetric group combinatorics, with commands for
Young diagrams, tableaux, tabloids, skew tableaux, shifted tableaux,
ribbon tableaux, multitableaux, abacuses. These commands are intended to
be easy to use and easy to customise. In particular, TikZ styling can be
added to the components of these diagrams and common conventions and
idioms are supported using a key-value interface. All diagrams can be
used as standalone commands or as part of tikzpicture environments.

