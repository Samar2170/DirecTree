from directree.constants import VALID_FILE_FORMATS
from directree.lookup_dicts import LOOKUP_FILE_FORMAT_DICT
import pathlib
import os

class Accountant:
    def __init__(self, root_dir,grouped=True):
        self._root_dir = pathlib.Path(root_dir)
        self.grouped=grouped
        self.__init__files_dict()

    def __init__files_dict(self):
        self._files_dict = {}
        if self.grouped==True:
            for k in VALID_FILE_FORMATS.keys():
                self._files_dict[k] = {}
                self._files_dict[k]['file_count'] = 0
                self._files_dict[k]['memory'] = 0

    def build_cfm(self):
        self.analyze(self._root_dir)
        files_dict_copy = self._files_dict.copy()
        for k in files_dict_copy.keys():
            if files_dict_copy[k]['file_count'] == 0:
                del self._files_dict[k]
        
        print("{:<8} {:<15} {:<5} ".format('Type','Files','Size'))
        for k, v in self._files_dict.items():
            print("{:<8} {:<15} {:<10} Kb ".format(k, v['file_count'], v['memory']))

    def analyze(self, directory):
        objects = [o for o in directory.iterdir()]
        for obj in objects:
            if obj.is_dir():
                self.analyze(obj)
            else:
                self.analyze_file(obj)
    
    def analyze_file(self, file):
        if "." in file.name:
            file_format = file.name.split(".")[-1]
        else:
            file_format = "other"
        if file_format != "other":
            file_group = LOOKUP_FILE_FORMAT_DICT.get(file_format, "other")
        else:
            file_group = "other"
        self._files_dict[file_group]['file_count'] += 1
        self._files_dict[file_group]['memory'] += os.path.getsize(file)/1024
        # print(file_group, os.path.getsize(file))