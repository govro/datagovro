Ansible won't work by default on Windows with Vagrant. A simpler solution is:

1. `vagrant up` and wait for the provisioning step to fail
2. `vagrant ssh` to log into the machine
3. Edit `/etc/ansible/hosts` and add `localhost ansible_connection=local` on the last line
4. `sudo apt-get install ansible`
5. Run `ansible-playbook /vagrant/provisioning/playbook.yml` in the shell.
