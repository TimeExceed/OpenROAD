#!/usr/bin/python3
from pathlib import Path
import subprocess as sp

IMAGE_NAME = 'ord-build'

def build_docker(pwd):
    cmd = ['docker', 'build', '-t', IMAGE_NAME, '.']
    sp.run(cmd, cwd=pwd).check_returncode()

if __name__ == '__main__':
    pwd = Path.cwd()
    build_docker(pwd)

