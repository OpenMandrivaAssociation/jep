%define ext_version 1.1.1

Name:		jep
Version:	2.4.1
Release:	%mkrel 3
Summary:	Java Math Expression Parser
URL:		http://sourceforge.net/projects/jep/
Source:		http://dl.sourceforge.net/sourceforge/jep/jep-%{version}-ext-%{ext_version}-gpl.zip
Patch0:		jep-build.patch
BuildRequires:	java-devel java-rpmbuild ant ant-nodeps javacc3 jama junit
Group:		Development/Java
License:	GPL+
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{_basename}-%{version}-%{release}-buildroot
%description
JEP is a Java library for parsing and evaluating mathematical expressions.
With this package you can allow your users to enter an arbitrary formula
as a string, and instantly evaluate it. JEP supports user defined
variables, constants, and functions. A number of common mathematical
functions and constants are included.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n jep-%{version}-ext-%{ext_version}-gpl
%patch0 -p1

%{_bindir}/find . -name '*.jar' -or -name '*.class' -exec rm {} \;
%{__mkdir} javacc
%{__ln_s} %{_javadir}/javacc3.jar javacc/javacc.jar

%build
export JAVACCHOME=`pwd`/javacc
%ant

%install
%{__rm} -Rf %{buildroot}
%{__install} -d %{buildroot}%{_javadir}
%{__install} -m 644 dist/ext-%{ext_version}.jar %{buildroot}%{_javadir}
%{__ln_s} ext-%{ext_version}.jar %{buildroot}%{_javadir}/ext.jar
%{__install} -m 644 dist/jep-%{version}.jar %{buildroot}%{_javadir}
%{__ln_s} jep-%{version}.jar %{buildroot}%{_javadir}/jep.jar

%{__install} -d %{buildroot}%{_javadocdir}
%{__cp} -a doc/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%doc CHANGES.txt COPYRIGHT.txt LICENSE-gpl.txt README.html doc/html
%{_javadir}/ext-%{ext_version}.jar
%{_javadir}/ext.jar
%{_javadir}/jep-%{version}.jar
%{_javadir}/jep.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
