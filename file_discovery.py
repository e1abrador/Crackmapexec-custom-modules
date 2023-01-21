from csv import reader

class CMEModule:
    """
        Search for interesting files in a specified directory

        Module by Eric Labrador 
    """

    name = 'file_discovery'
    description = "Search for .sql files in a specified directory."
    supported_protocols = ['smb']
    opsec_safe = True   # only legitimate commands are executed on the remote host (search process and files)
    multiple_hosts = True

    def __init__(self):
        self.search_path = ''

    def options(self, context, module_options):
        """
        SEARCH_PATH     Remote location where to search for .sql files (you must add single quotes around the path if it includes spaces)
                        Required option
        """

        if 'SEARCH_PATH' in module_options:
            self.search_path = module_options['SEARCH_PATH']
        else:
            context.log.error('SEARCH_PATH is a required option')

    def on_admin_login(self, context, connection):
        # search for .sql files
        search_sql_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.sql -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_sql_files_cmd = 'powershell.exe "{}"'.format(search_sql_files_payload)
        search_sql_files_output = connection.execute(search_sql_files_cmd, True).split("\r\n")
        found = False
        for file in search_sql_files_output:
            if '.sql' in file:
                found = True
                context.log.highlight('Found .sql file: {}'.format(file))

        # search for .kdbx files
        search_kdbx_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.kdbx -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_kdbx_files_cmd = 'powershell.exe "{}"'.format(search_kdbx_files_payload)
        search_kdbx_files_output = connection.execute(search_kdbx_files_cmd, True).split("\r\n")
        found = False
        for file in search_kdbx_files_output:
            if '.kdbx' in file:
                found = True
                context.log.highlight('Found .kdbx file: {}'.format(file))

        # search for .txt files
        search_txt_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.txt -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_txt_files_cmd = 'powershell.exe "{}"'.format(search_txt_files_payload)
        search_txt_files_output = connection.execute(search_txt_files_cmd, True).split("\r\n")
        found = False
        for file in search_txt_files_output:
            if '.txt' in file:
                found = True
                context.log.highlight('Found .txt file: {}'.format(file))

        # search for .bak files
        search_bak_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.bak -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_bak_files_cmd = 'powershell.exe "{}"'.format(search_bak_files_payload)
        search_bak_files_output = connection.execute(search_bak_files_cmd, True).split("\r\n")
        found = False
        for file in search_bak_files_output:
            if '.bak' in file:
                found = True
                context.log.highlight('Found .bak file: {}'.format(file))

        # search for .env files
        search_env_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.env -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_env_files_cmd = 'powershell.exe "{}"'.format(search_env_files_payload)
        search_env_files_output = connection.execute(search_env_files_cmd, True).split("\r\n")
        found = False
        for file in search_env_files_output:
            if '.env' in file:
                found = True
                context.log.highlight('Found .env file: {}'.format(file))

        # search for .yml files
        search_yml_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.yml -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_yml_files_cmd = 'powershell.exe "{}"'.format(search_yml_files_payload)
        search_yml_files_output = connection.execute(search_yml_files_cmd, True).split("\r\n")
        found = False
        for file in search_yml_files_output:
            if '.yml' in file:
                found = True
                context.log.highlight('Found .yml file: {}'.format(file))
                
        # search for .yaml files
        search_yaml_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.yaml -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_yaml_files_cmd = 'powershell.exe "{}"'.format(search_yaml_files_payload)
        search_yaml_files_output = connection.execute(search_yaml_files_cmd, True).split("\r\n")
        found = False
        for file in search_yaml_files_output:
            if '.yaml' in file:
                found = True
                context.log.highlight('Found .yaml file: {}'.format(file))                

        # search for .properties files
        search_properties_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.properties -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_properties_files_cmd = 'powershell.exe "{}"'.format(search_properties_files_payload)
        search_properties_files_output = connection.execute(search_properties_files_cmd, True).split("\r\n")
        found = False
        for file in search_properties_files_output:
            if '.properties' in file:
                found = True
                context.log.highlight('Found .properties file: {}'.format(file))                

        # search for .ini files
        search_ini_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.ini -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_ini_files_cmd = 'powershell.exe "{}"'.format(search_ini_files_payload)
        search_ini_files_output = connection.execute(search_ini_files_cmd, True).split("\r\n")
        found = False
        for file in search_ini_files_output:
            if '.ini' in file:
                found = True
                context.log.highlight('Found .ini file: {}'.format(file))    

        # search for .config files
        search_config_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.config -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_config_files_cmd = 'powershell.exe "{}"'.format(search_config_files_payload)
        search_config_files_output = connection.execute(search_config_files_cmd, True).split("\r\n")
        found = False
        for file in search_config_files_output:
            if '.config' in file:
                found = True
                context.log.highlight('Found .config file: {}'.format(file)) 

        # search for .cfg files
        search_cfg_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.cfg -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_cfg_files_cmd = 'powershell.exe "{}"'.format(search_cfg_files_payload)
        search_cfg_files_output = connection.execute(search_cfg_files_cmd, True).split("\r\n")
        found = False
        for file in search_cfg_files_output:
            if '.cfg' in file:
                found = True
                context.log.highlight('Found .cfg file: {}'.format(file))    

                
        # search for .conf files
        search_conf_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.conf -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_conf_files_cmd = 'powershell.exe "{}"'.format(search_conf_files_payload)
        search_conf_files_output = connection.execute(search_conf_files_cmd, True).split("\r\n")
        found = False
        for file in search_conf_files_output:
            if '.conf' in file:
                found = True
                context.log.highlight('Found .conf file: {}'.format(file))    
                
        # search for .cnf files
        search_cnf_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.cnf -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_cnf_files_cmd = 'powershell.exe "{}"'.format(search_cnf_files_payload)
        search_cnf_files_output = connection.execute(search_cnf_files_cmd, True).split("\r\n")
        found = False
        for file in search_cnf_files_output:
            if '.cnf' in file:
                found = True
                context.log.highlight('Found .cnf file: {}'.format(file))   
                
        # search for .plist files
        search_plist_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.plist -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_plist_files_cmd = 'powershell.exe "{}"'.format(search_plist_files_payload)
        search_plist_files_output = connection.execute(search_plist_files_cmd, True).split("\r\n")
        found = False
        for file in search_plist_files_output:
            if '.plist' in file:
                found = True
                context.log.highlight('Found .plist file: {}'.format(file))   
                
                
        # search for .key files
        search_key_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.key -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_key_files_cmd = 'powershell.exe "{}"'.format(search_key_files_payload)
        search_key_files_output = connection.execute(search_key_files_cmd, True).split("\r\n")
        found = False
        for file in search_key_files_output:
            if '.key' in file:
                found = True
                context.log.highlight('Found .key file: {}'.format(file))   
                
        # search for .netrc files
        search_netrc_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.netrc -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_netrc_files_cmd = 'powershell.exe "{}"'.format(search_netrc_files_payload)
        search_netrc_files_output = connection.execute(search_netrc_files_cmd, True).split("\r\n")
        found = False
        for file in search_netrc_files_output:
            if '.netrc' in file:
                found = True
                context.log.highlight('Found .netrc file: {}'.format(file)) 
                
                
        # search for .php files
        search_php_files_payload = "Get-ChildItem -Path {} -Recurse -Force -Include *.php -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName".format(self.search_path)
        search_php_files_cmd = 'powershell.exe "{}"'.format(search_php_files_payload)
        search_php_files_output = connection.execute(search_php_files_cmd, True).split("\r\n")
        found = False
        for file in search_php_files_output:
            if '.php' in file:
                found = True
                context.log.highlight('Found .php file: {}'.format(file)) 
                
