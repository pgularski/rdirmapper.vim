# rdirmapper.vim
Map remote files and/or directories to local ones. SCP at will.

# Run
```
:scpto example-server
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
local/path/with/.ridmapper-containg/dir/as/root = /remote/path
relative/directory/path/file.name = /remote/directory/path
/absolute/directory/path = /remote/directory/path
/absolute/directory/path/with/a/slash/ = /remote/directory/path
relative/directory/path = /remote/directory/path
```

