import subprocess

class CMEModule:
    name = "xfreerdp"
    description = "Remotely check if RDP connection is possible using xfreerdp"
    supported_protocols = ["smb"]
    opsec_safe= True
    multiple_hosts = True

    def options(self, context, module_options):
        """
        """

    def on_admin_login(self, context, connection):

        domain = connection.domain
        username = connection.username
        host = connection.host
        password = getattr(connection, "password", "")
        nthash = getattr(connection, "nthash", "")
        hostname = connection.hostname


        if password == "":
            command = f'xfreerdp /v:{host} +auth-only /d:{domain} /u:{username} /pth:{nthash} /cert-ignore'
            showcommand = f'xfreerdp /v:{host} /d:{domain} /u:{username} /p:{nthash} /cert-ignore'
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                success_login_yes_rdp = "Authentication only, exit status 0"
                if success_login_yes_rdp in output.decode('utf-8'):
                     context.log.success(f"Connection successfuly in RDP using provided credentials.")
                     context.log.success(showcommand)
                else:
                    None
                    #context.log.error("Authentication error using xfreerdp")
            except subprocess.CalledProcessError as e:
               None
               #context.log.error("Authentication error using xfreerdp.")

        else:
            command = f'xfreerdp /v:{host} +auth-only /d:{domain} /u:{username} /p:{password} /cert-ignore'
            showcommand = f'xfreerdp /v:{host} /d:{domain} /u:{username} /p:{password} /cert-ignore'
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                success_login_yes_rdp = "Authentication only, exit status 0"
                if success_login_yes_rdp in output.decode('utf-8'):
                     context.log.success(f"Connection successfuly in RDP using provided credentials.")
                     context.log.success(showcommand)
                else:
                    None
                    #context.log.error("Authentication error using xfreerdp")
            except subprocess.CalledProcessError as e:
                #context.log.error("Authentication error using xfreerdp.")
                None

