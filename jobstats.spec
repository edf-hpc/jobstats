Name:           jobstats
Version:        1.0.0
Release:        1
Summary:        HPC job monitoring designed for CPU and GPU

License:        GPL-2.0
URL:            https://github.com/edf-hpc/jobstats
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3
Requires:       python3

%description
Jobstats is a free and open-source job monitoring platform designed for CPU and GPU clusters that use the Slurm workload manager.

%prep
%autosetup -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{python3_sitelib}/jobstats

install -m 0644 jobstats.py \
    %{buildroot}%{python3_sitelib}/jobstats/jobstats.py

install -m 0644 store_jobstats.py \
    %{buildroot}%{python3_sitelib}/jobstats/store_jobstats.py

install -m 0644 output_formatters.py \
    %{buildroot}%{python3_sitelib}/jobstats/output_formatters.py

install -m 0644 db_handler.py \
    %{buildroot}%{python3_sitelib}/jobstats/db_handler.py

cat <<'EOF' > %{buildroot}%{python3_sitelib}/jobstats/__init__.py
from .jobstats import c, Jobstats
from .output_formatters import ClassicOutput
from .db_handler import JobstatsDBHandler

__all__ = ["c", "Jobstats", "ClassicOutput", "JobstatsDBHandler"]
EOF

install -d %{buildroot}%{_bindir}
install -Dp jobstats %{buildroot}%{_bindir}

install -d %{buildroot}%{_sysconfdir}/jobstats
install -m 0644 config.py %{buildroot}%{_sysconfdir}/jobstats/config.py

%files
%license LICENSE.md
%doc README.md

%{_bindir}/jobstats

%dir %{python3_sitelib}/jobstats
%pycached %{python3_sitelib}/jobstats/__init__.py
%pycached %{python3_sitelib}/jobstats/jobstats.py
%pycached %{python3_sitelib}/jobstats/store_jobstats.py
%pycached %{python3_sitelib}/jobstats/output_formatters.py
%pycached %{python3_sitelib}/jobstats/db_handler.py

%dir %{_sysconfdir}/jobstats
%config(noreplace) %{_sysconfdir}/jobstats/config.py

%changelog
* Wed Feb 11 2026 Kwame Amedodji <kwame-externe.amedodji@edf.fr> - 1.0.0-1
- first rpm package
