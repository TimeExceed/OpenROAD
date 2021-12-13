#!/usr/bin/python3
import subprocess as sp

cmd = [
    'apt', 'install', '-y',
    'libreadline-dev', 'tcl', 'tcl-dev',
    'swig3.0', 'libspdlog1', 'libspdlog-dev',
    'bison', 'flex', 'libeigen3-dev',
    'liblemon-dev', 'liblemon-utils',
]
sp.check_call(cmd)
sp.check_call(['apt', 'clean'])
