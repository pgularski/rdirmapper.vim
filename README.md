# rdirmapper.vim
Vim plugin - map local and remote paths. SCP at will.

Instead of running `scp path/to/recently/edited/file.js example-host:/var/www/myapp/public/common/scipts/` every time you save a file, you can do `:ScpTo example-host` directly from vim. Hours saved.

# Run
```
:ScpTo example-host
```
It'll find a mapping for the currently open file and scp it to the remote server.

# Installation
With Vundle:
```
Plugin 'pgularski/rdirmapper.vim'
```

# Sample config
Place the `.rdirmapper` file in the project's directory:
```
[example-host]
/local/file/path/file.name = /remote/file/path/file.name
directory/path/ = /remote/directory/path

[example-host.settings]
username = root
```
The `section-name.settings` is NOT required

# SSH config
Make sure you have your public ssh keys deployed to the target hosts.

The plugin uses the system's `scp` command so the `~/.ssh/config` file is used.

Ideally you want to match the host from the `~/.ssh/config` to a `.rdirmapper` section:

~/.ssh/config:
```
Host example-host
    Hostname example.com
    User someuser
    Port 2222
```

.rdirmapper:
```
[example-host]
/local/file/path/file.name = /remote/file/path/file.name
local/path/with/.ridmapper/path/ = /remote/path
```

# Requirements
Your vim has to be compiled with Python3 support.
Run `vim --version` to see if `+python3` is there.
