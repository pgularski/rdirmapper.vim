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
[example-server]
; Use ~/.ssh/config by default
host = example-server
; user = root
; pass = xyz
; port = 22
; cmd = scp -P {port}{user}@{host}:{local} {remote}

[example-server.paths]
/local/file/path = /remote/file/path
/local/directory/path = /remote/directory/path
./local/path/with/.ridmapper-containg/dir/as/root = /remote/path
```

