import vim
import os
import configparser
import subprocess
from os.path import abspath, dirname, relpath


RDIRMAPPER_FILENAME = '.rdirmapper'
ROOT_DIR = '/'


def upper_directory(path):
    return os.path.split(os.path.abspath(path))[0]


def get_rdirmapper_dir():
    current_file = vim.current.buffer.name
    current_dir = os.path.abspath(os.path.dirname(current_file))
    while current_dir != ROOT_DIR:
        if RDIRMAPPER_FILENAME in os.listdir(current_dir):
            return current_dir
        current_dir = upper_directory(current_dir)
    return ''



def scp_to_host(host):
    #  print(vim.vars.keys())
    #  print(vim.vars.values())
    #  print(vim.options)
    print("Host: {}".format(host))

    if not vim.current.buffer.name:
        print("Nothing to scp. No file opened.")
        return
    rdrirmapper_dir = get_rdirmapper_dir()
    if not rdrirmapper_dir:
        print('{} file not found!'.format(RDIRMAPPER_FILENAME))
        return

    config = configparser.ConfigParser()
    config.read(os.path.join(rdrirmapper_dir, RDIRMAPPER_FILENAME))

    if host not in config:
        print('No mappings found for {}'.format(host))
        return

    for local_path in config[host]:
        print(local_path, config[host][local_path])

    current_file = vim.current.buffer.name
    current_dir = abspath(dirname(current_file))
    current_file_relative = relpath(current_file,
                                    start=rdrirmapper_dir)
    current_dir_relative = relpath(dirname(current_file),
                                    start=rdrirmapper_dir)

    path_order = [
            current_file,
            current_file_relative,
            current_dir,
            current_dir + os.path.sep,
            current_dir_relative,
            current_dir_relative + os.path.sep,
            ]

    for path in path_order:
        if path in config[host]:
            print("Path found: {}".format(path))
            dest_path = config[host][path]
            cmd = "scp {current_file} {host}:{dest_path}".format(
                    current_file=current_file,
                    host=host,
                    dest_path=dest_path)
            proc = subprocess.Popen(cmd, shell=True)
            ret = proc.wait()
            if ret != 0:
                print('Something went wrong while SCP-ing the file!')
            break
