import vim
import os
import configparser

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



def say_it_works():
    rdrirmapper_dir = get_rdirmapper_dir()
    if not rdrirmapper_dir:
        print('{} file not found!'.format(RDIRMAPPER_FILENAME))
        return

    print(rdrirmapper_dir)

    config = configparser.ConfigParser()
    config.read(os.path.join(rdrirmapper_dir, RDIRMAPPER_FILENAME))
    print(config.sections())


    #  print("It works!")
    #  print(os.getcwd())
    # vim.current.line
    #  print(vim.current.buffer.name)
    #  print(vim.vars.keys())
    #  print(vim.vars.values())
    #  print(vim.options)

def scp_to_host(filename, hostname):
    pass
