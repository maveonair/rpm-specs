%global forgeurl    https://github.com/JetBrains/JetBrainsMono
Version:            3.1.1

Release: 1%{?dist}
URL:     https://github.com/ryanoasis/nerd-fonts/

%global foundry           JetBrains
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.md
%global common_description %{expand:
Nerd Fonts patches developer targeted fonts with a high number of glyphs (icons).
Specifically to add a high number of extra glyphs from popular ‘iconic fonts’ such
as Font Awesome, Devicons, Octicons, and others.}

%global fontfamily0       JetBrainsMono Nerd Font
%global fontsummary0      A mono-space font family of the JetBrains Mono font with Nerd Font glyphs added
%global fonts0            JetBrainsMonoNerdFont*.ttf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}
This is a package of the JetBrains Mono font with Nerd Font glyphs added.}

%global fontfamily1       JetBrainsMonoNL Nerd Font
%global fontsummary1      A mono-space font family of the JetBrains Mono font with Nerd Font glyphs added
%global fonts1            JetBrainsMonoNLNerdFont*.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
This is a package of the JetBrains mono font without coding ligatures and with additional Nerd Font glyphs.}

Source0:  https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.zip
Source10: 60-%{fontpkgname0}.xml
Source11: 58-%{fontpkgname1}.xml

%fontpkg -a

%prep
%setup -c -n %{fontpkgname0}-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Wed Dec 13 2023 Fabian Mettler <dev@maveonair.com>
- Initial packaging
