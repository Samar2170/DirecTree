import pathlib
from directree.constants import VALID_FORMATS
from directree.lookup_dicts import LOOKUP_FORMAT_DICT

class Director:
    def __init__(self,root_dir):
        self._root_dir=pathlib.Path(root_dir)
        self.__init__lc_dict()

    def __init__lc_dict(self):
        self._files_lc = {}
        for k in VALID_FORMATS.keys():
            self._files_lc[k]={}
            self._files_lc[k]['line_count']=0
            self._files_lc[k]['file_count']=0
    
    def build_cloc(self):
        self.analyze(self._root_dir)
        files_lc_copy=self._files_lc.copy()
        for k in files_lc_copy.keys():
            if files_lc_copy[k]['file_count']==0:
                del self._files_lc[k]
        print("-------------------------------------------------------")
        print ("{:<8} {:<15} {:<10} ".format('Lang','Files','LOCs'))
        for k,v in self._files_lc.items():
            print("{:<8} {:<15} {:<10} ".format(k,v['file_count'],v['line_count']))


    def analyze(self,directory):
        objects =[o for o in directory.iterdir()]
        for obj in objects:
            if obj.is_dir():
                self.analyze(obj)
            else:
                self.analyze_file(obj)
    
    def analyze_file(self,file):
        if "." in file.name:
            file_format = file.name.split(".")[-1]
        else:
            file_format = "other"
        if file_format !="other":
            file_group=LOOKUP_FORMAT_DICT.get(file_format,"other")
        else:
            file_group="other"

        try:
            with file.open() as f:
                lines=f.readlines()
                line_count=len(lines)
        except:
            line_count=0
        self._files_lc[file_group]['line_count']+=line_count
        self._files_lc[file_group]['file_count']+=1
    