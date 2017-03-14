%{?scl:%scl_package nodejs-npm-package-arg}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-npm-package-arg

%global npm_name npm-package-arg
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           %{?scl_prefix}nodejs-npm-package-arg
Version:        4.2.0
Release:        1%{?dist}
Summary:        Parse the things that can be arguments to `npm install`
Url:            https://github.com/npm/npm-package-arg
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        ISC
BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(tap)
%endif

BuildRequires: %{?scl_prefix}npm(hosted-git-info)
BuildRequires: %{?scl_prefix}npm(semver)

Requires: %{?scl_prefix}npm(hosted-git-info)
Requires: %{?scl_prefix}npm(semver)

%description
Parse the things that can be arguments to `npm install`

%prep
%setup -q -n package

#%{nodejs_fixdep} semver

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json npa.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md
%doc LICENSE

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.2.0-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.0-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 4.1.0-1
- New upstream release

* Thu Nov 26 2015 Tomas Hrcka <thrcka@redhat.com> - 4.0.1-3
- Enable scl macros

* Wed Jun 17 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.1-1
- New upstream version

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.0-1
- Initial build
