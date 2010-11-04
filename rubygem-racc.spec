%define oname racc

Summary:    Racc is a LALR(1) parser generator
Name:       rubygem-%{oname}
Version:    1.4.6
Release:    %mkrel 1
Group:      Development/Ruby
License:    LGPLv2
URL:        http://racc.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
Provides:   rubygem(%{oname}) = %{version}

%description
Racc is a LALR(1) parser generator. It is written in Ruby itself, and
generates Ruby program.


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext

# Move arch dependent files to sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/racc/cparse/cparse.so %{buildroot}%{ruby_sitearchdir}
rmdir %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/racc/cparse

# Move executables to bindir
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ -name ".git*" -exec rm {} \;
perl -pi -e 's!/usr/local/bin/ruby!/usr/bin/env ruby!' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin/*

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/racc
%{_bindir}/racc2y
%{_bindir}/y2racc
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/fastcache/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/misc/
%{ruby_gemdir}/gems/%{oname}-%{version}/sample/
%{ruby_gemdir}/gems/%{oname}-%{version}/tasks/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/web/
%{ruby_gemdir}/gems/%{oname}-%{version}/.require_paths
%{ruby_gemdir}/gems/%{oname}-%{version}/setup.rb
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/doc/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/DEPENDS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README*.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/TODO
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so
