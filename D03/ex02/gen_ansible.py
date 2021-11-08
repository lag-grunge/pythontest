#! /bin/python3
import os
import re

import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from os import path

filepath = path.realpath(__file__)
dirname = Path(filepath).parent.parent
q1 = dirname / "todo.yml"
q2 = dirname / "deploy.yml"
e1 = dirname / "ex00" / "exploit.py"
e2 = dirname / "ex01" / "consumer.py"

if __name__=="__main__":
	todo_text = None
	with q1.open("r") as fp:
		todo_text = fp.read()
		fp.close()
	if todo_text is None:
		print("no such file or empty file or read error")
		exit(1)
	yml = yaml.load(todo_text, Loader=SafeLoader)
	todo = yml["server"]
	server_operations = []

	install = dict({})
	install["name"] = "Install"
	install["ansible.builtin.package"] = dict({})
	install["ansible.builtin.package"]["name"] = []
	for p in todo["install_packages"]:
		install["name"] += " " + p
		install["ansible.builtin.package"]["name"].append(p)
	install["ansible.builtin.package"]["state"] = "present"
	server_operations.append(install)

	for e in todo["exploit_files"]:
		copy = dict({})
		copy["name"] = "Copy exploit file " + e
		copy["ansible.builtin.copy"] = dict({})
		if e == e1.name:
			copy["ansible.builtin.copy"]["src"] = e1.as_posix()
		elif e == e2.name:
			copy["ansible.builtin.copy"]["src"] = e2.as_posix()
		copy["ansible.builtin.copy"]["dest"] = "/"
		copy["ansible.builtin.copy"]["owner"] = "root"
		copy["ansible.builtin.copy"]["group"] = "root"
		copy["ansible.builtin.copy"]["mode"] = "u = rwx, g = rx, o = rx"
		server_operations.append(copy)

	for e in todo["exploit_files"]:
		run = dict({})
		run["name"] = "Run exploit " + e
		run["ansible.builtin.command"] = dict({})
		if e == 'exploit.py':
			run["ansible.builtin.command"]["command"] = "/bin/python3 " + "/" + e1.name
		elif e == 'consumer.py':
			run["ansible.builtin.command"]["command"] = "/bin/python3 " + "/" + e2.name
			run["ansible.builtin.command"]["args"] = ["-e"] + yml["bad_guys"]
		server_operations.append(run)

	with q2.open("w") as wf:
		yaml.dump(server_operations, wf, sort_keys=False)
		wf.close()
