#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fdupes
Version  : 1.6.1
Release  : 3
URL      : https://github.com/adrianlopezroche/fdupes/archive/v1.6.1.tar.gz
Source0  : https://github.com/adrianlopezroche/fdupes/archive/v1.6.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: fdupes-bin = %{version}-%{release}
Requires: fdupes-man = %{version}-%{release}

%description
Introduction
--------------------------------------------------------------------
FDUPES is a program for identifying duplicate files residing
within specified directories.

%package bin
Summary: bin components for the fdupes package.
Group: Binaries

%description bin
bin components for the fdupes package.


%package man
Summary: man components for the fdupes package.
Group: Default

%description man
man components for the fdupes package.


%prep
%setup -q -n fdupes-1.6.1
cd %{_builddir}/fdupes-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604358574
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604358574
rm -rf %{buildroot}
%make_install
## install_append content
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man1
install fdupes %{buildroot}/usr/bin/
install fdupes.1 %{buildroot}/usr/share/man/man1
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fdupes

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fdupes.1
