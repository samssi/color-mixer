#!/usr/bin/env bash

ansible-playbook -i inventory-prod playbook.yml --user=pi --private-key=~/.ssh/pi_rsa --ask-become-pass --become