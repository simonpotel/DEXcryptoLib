from datetime import *
from .json import *
import os 
import json 

class Log(object):
    def __init__(self, folder, default_config):
        self.folder = folder 
        self.config_path = folder + "/config.json" 
        self.config = get_json_content(self.config_path)
        if not os.path.exists(folder): os.makedirs(folder, exist_ok=True)
        if self.config == -1:
            with open(self.config_path, 'w') as file_handle:
                json.dump(default_config, file_handle, indent=2)
                print(f"{self.config_path} has been created.")
                exit()
    def writelog(self, folder, to_log):
        if not (folder in self.config): # Security to not crash "Keyerror"
            self.config[folder] = "True"
            write_json(self.config_path, self.config) 
            return self.writelog(folder, to_log) 
        if self.config[folder] != "True": return 0
        file = str(date.today())
        path_folder = self.folder + "/" + folder
        timestamp = str(datetime.now())
        if not os.path.exists(path_folder):
            os.makedirs(path_folder, exist_ok=True)
        with open(path_folder + "/" + file + ".txt", "a") as file_handle:
            file_handle.write(f'{timestamp} | {to_log}\n')
        print(timestamp + " " + folder + " " + file + " " + to_log)

default_config = {'debug': 'True', 'routers': 'True', 'web3': 'True'}
logobj = Log("Logs", default_config)
def log(folder, to_log):
    logobj.writelog(folder, to_log)
for section in logobj.config:
    log(section, "*** Library has been started ***")
