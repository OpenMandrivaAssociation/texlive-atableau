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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/atableau
%dir %{_datadir}/texmf-dist/tex/latex/atableau
%doc %{_datadir}/texmf-dist/doc/latex/atableau/CHANGES.md
%doc %{_datadir}/texmf-dist/doc/latex/atableau/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/atableau/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/atableau/README.md
%doc %{_datadir}/texmf-dist/doc/latex/atableau/TODO.md
%doc %{_datadir}/texmf-dist/doc/latex/atableau/atableau.pdf
%doc %{_datadir}/texmf-dist/doc/latex/atableau/atableau.tex
%doc %{_datadir}/texmf-dist/doc/latex/atableau/atableau_beamer.pdf
%doc %{_datadir}/texmf-dist/doc/latex/atableau/atableau_beamer.tex
%doc %{_datadir}/texmf-dist/doc/latex/atableau/atableau_readme.webp
%{_datadir}/texmf-dist/tex/latex/atableau/atableau.ini
%{_datadir}/texmf-dist/tex/latex/atableau/atableau.sty
