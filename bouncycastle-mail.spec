%global ver  1.46
%global archivever  jdk16-%(echo %{ver}|sed 's|\\\.||')

Summary:          Bouncy Castle Mail Package for Java
Name:             bouncycastle-mail
Version:          1.46
Release:          1%{?dist}
Group:            System Environment/Libraries
License:          MIT
URL:              http://www.bouncycastle.org/
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# Use original sources from here on out.
Source0:          http://www.bouncycastle.org/download/bcmail-%{archivever}.tar.gz
Source1:          http://www.bouncycastle.org/download/bcmail-%{archivever}.jar

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel >= 1.6
BuildRequires:    junit4
BuildRequires:    bouncycastle
BuildRequires:    javamail

Requires:         jpackage-utils
Requires:         java >= 1.6
Requires:         bouncycastle == %{version}

Provides:         bcmail = %{version}-%{release}

%description
Bouncy Castle consists of a lightweight cryptography API and is a provider 
for the Java Cryptography Extension and the Java Cryptography Architecture.
This library package offers additional classes, in particuar 
generators/processors for S/MIME and CMS, for Bouncy Castle.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcmail-%{archivever}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_javadir}/bcmail-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf bcmail-%{version}.jar bcmail.jar
popd

#javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.html
%{_javadir}/bcmail.jar
%{_javadir}/bcmail-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Tue Nov 13 2012 Andrea Ceccanti <andrea.ceccanti@cnaf.infn.it> - 1.46-1
- Initial packaging
