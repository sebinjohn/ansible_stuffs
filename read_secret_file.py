from ansible.parsing.vault import VaultEditor
from ansible.parsing.dataloader import DataLoader
from ansible.cli import CLI
import yaml
import os

loader = DataLoader()
vault_password_file = os.environ.get('ANSIBLE_VAULT_PASSWORD_FILE')
secret_file = os.environ.get('SECRET_FILE')
if vault_password_file and secret_file:
    password = CLI.read_vault_password_file(vault_password_file, loader)
    editor = VaultEditor(password)
    secrets = yaml.load(editor.plaintext(secret_file))
    print secrets
    for k, v in secrets.iteritems():
        print k, v
else:
    print """
        Specify the following
        ANSIBLE_VAULT_PASSWORD_FILE
        SECRET_FILE
        """

