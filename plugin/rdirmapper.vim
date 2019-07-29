if !has("python3")
    echo "vim has to be compiled with +python3 to load rdirmapper plugin"
    finish
endif

if exists('g:rdirmapper_plugin_loaded')
    finish
endif

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

function! ScpToHost(host)
    python3 rdirmapper.scp_to_host(vim.eval('a:host'))
endfunction

command! -nargs=* ScpToHost call ScpToHost(<f-args>)


let g:rdirmapper_plugin_loaded = 1
