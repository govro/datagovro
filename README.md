# data.gov.ro

[data.gov.ro](http://data.gov.ro) is the Romanian national portal for open data.

![homepage](https://cloud.githubusercontent.com/assets/772220/7836915/ba2043b0-048c-11e5-9c06-25368d95cba0.png)

## Setup

### Vagrant

1. Install [Vagrant](https://www.vagrantup.com/).
2. Clone this repo.
2. `cd datagovro && vagrant up` will provision the machine using Ansible, with a CKAN
[installation](http://docs.ckan.org/en/ckan-2.3/maintaining/installing/install-from-source.html)
from source.
3. `vagrant ssh` to log into the machine.
4. `sudo supervisorctl status` should show a running process.
5. On [localhost:8080](http://localhost:8080) should be the website.

### Dev Server

1. `sudo apt-get install git ansible`
2. `git clone https://github.com/govro/datagovro.git`
3. `cd datagovro/provisioning`
4. `ansible-playbook -i "localhost," -c local playbook.yml`

## Folder hierarchy

- `docs/`
- `provisioning/playbook.yml` - provisioning Ansible script
- `provisioning/files` - configs

Logs are in `/var/log/supervisor`.

## Monitoring

[Uptime](http://uptime.statuscake.com/?TestID=8pM4VcMsBu) on the last 30 days.

<a href="http://uptime.statuscake.com/?TestID=8pM4VcMsBu" title="Website Uptime Monitoring"><img src="https://www.statuscake.com/App/button/index.php?Track=FPupDABBg2&Days=30&Design=2" /></a>
