# Activate by default the virtualenv
. {{ ckan_path }}/bin/activate

# Run ansible provisioning script
alias provision_ansible='ansible-playbook -vvv /vagrant/provisioning/playbook.yml'
alias provision_ansible_debug='ansible-playbook -vvv /vagrant/provisioning/playbook.yml --tags "debug"'
