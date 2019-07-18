let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
import vim
from os.path import normpath, join
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'src'))
sys.path.insert(0, python_root_dir)
import rdirmapper
EOF

