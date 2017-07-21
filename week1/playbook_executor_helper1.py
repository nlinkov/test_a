#!/usr/bin/python

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook import Playbook
from ansible.executor.playbook_executor import PlaybookExecutor

Options = namedtuple('Options', ['connection',  'forks', 'become', 'become_method',
                                 'become_user', 'check', 'listhosts', 'listtasks', 'listtags', 'syntax', 'module_path'])

variable_manager = VariableManager()
loader = DataLoader()
options = Options(connection='smart', forks=5, become=False, become_method='sudo', become_user='root',
                  check=False, listhosts=None, listtasks=None, listtags=None, syntax=False, module_path="")
passwords = dict(vault_pass='secret')

inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='../../ansible-hosts')
variable_manager.set_inventory(inventory)
playbooks = ["ansible_test1.yml"]

executor = PlaybookExecutor(
    playbooks=playbooks,
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    options=options,
    passwords=passwords)

