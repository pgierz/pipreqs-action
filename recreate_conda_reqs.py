#!/usr/bin/env python3
"""
Reads pip requirements.txt and creates conda requirements
"""
import os

import yaml

def read_requirements(rpath="requirements.txt"):
    with open(rpath, "r", encoding="utf-8") as requirements:
        return requirements.readlines()

def read_old_conda(cfile="ci/..."):
    with open(cfile, "r", encoding="utf-8") as conda_reqs:
        return yaml.safe_load(conda_reqs.read())


def replace_requirements(old_reqs, new_reqs):
    del old_reqs["dependencies"]
    old_reqs["dependencies"] = new_reqs
    return old_reqs

def write_new_conda(cfile, reqs):
    with open(cfile, "w", encoding="utf-8") as cfile:
        yaml.dump(reqs, cfile)


def main():
    pip_reqs = read_requirements()
    old_conda = read_old_conda()
    new_reqs = replace_requirements(old_conda, pip_reqs)
    path = os.environ.get("CONDA_REQS", "environment.yml")
    write_new_conda(new_reqs, path)





