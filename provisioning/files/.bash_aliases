# Activate by default the virtualenv
. {{ ckan_path }}/bin/activate

# Run ansible provisioning script
alias provision_ansible="ansible-playbook playbook.yml -vvv /vagrant/provisioning/playbook.yml"
