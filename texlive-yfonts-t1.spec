Name:		texlive-yfonts-t1
Version:	36013
Release:	2
Summary:	Old German-style fonts, in Adobe type 1 format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yfonts-t1
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts-t1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts-t1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package comprises type 1 versions of the Gothic,
Schwabacher and Fraktur fonts of Yannis Haralambous' set of old
German fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/public/yfonts-t1
%{_texmfdistdir}/fonts/map/dvips/yfonts-t1
%{_texmfdistdir}/fonts/afm/public/yfonts-t1
%{_texmfdistdir}/dvips/yfonts-t1
%doc %{_texmfdistdir}/doc/fonts/yfonts-t1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
