import os
import pathlib
import sys
from directree.constants import PIPE, TEE, PIPE_PREFIX,SPACE_PREFIX,ELBOW

class DirecTree:
    def __init__(self,root_dir,dirs_only=False):
        self._generator = TreeGenerator(root_dir,dirs_only=dirs_only)


    def generate(self):
        tree= self._generator.build_tree()
        for entry in tree:
            print(entry)


class TreeGenerator:
    def __init__(self,root_dir,dirs_only=False):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only=dirs_only
        self._tree = []
    
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
    
    def _prepearte_entries(self,directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries
    
    def _tree_body(self,directory,prefix=''):
        entries=self._prepearte_entries(directory)
        entries = sorted(entries,key=lambda x:x.is_file())
        entries_count=len(entries)

        for index,entry in enumerate(entries):
            connector=ELBOW if index==entries_count -1 else TEE
            if entry.is_dir():
                self._add_directory(entry,index,entries_count,prefix,connector)
            else:
                self._add_file(entry,prefix,connector)

    def _add_directory(self,directory,index,entries_count,prefix,connector):
        self._tree.append(f"{prefix}{connector}{directory.name}{os.sep}")
        if index!=entries_count-1:
            prefix+=PIPE_PREFIX
        else:
            prefix+=SPACE_PREFIX
        self._tree_body(directory,prefix)
        self._tree.append(prefix.rstrip())

    def _add_file(self,file,prefix,connector):
        self._tree.append(f"{prefix}{connector}{file.name}")


