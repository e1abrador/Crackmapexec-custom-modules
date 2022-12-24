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
        search_txt_files_cmd = 'powertxtell.exe "{}"'.format(search_txt_files_payload)
        search_txt_files_output = connection.execute(search_txt_files_cmd, True).split("\r\n")
        found = False
        for file in search_txt_files_output:
            if '.txt' in file:
                found = True
                context.log.highlight('Found .txt file: {}'.format(file))
