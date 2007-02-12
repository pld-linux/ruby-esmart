Summary:	Ruby binding to the esmart library
Summary(pl.UTF-8):	Dowiązania języka ruby do biblioteki esmart
Name:		ruby-esmart
Version:	0
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	%{name}.tar.gz
# Source0-md5:	6cfc22dba679839fc2b6ab88314b9647
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	esmart-devel
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the esmart library.

%description -l pl.UTF-8
Dowiązania języka ruby do biblioteki esmart.

%prep
%setup -q -n %{name}

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

DESTDIR=$RPM_BUILD_ROOT RUBYARCHDIR=%{ruby_archdir} rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/*.so
