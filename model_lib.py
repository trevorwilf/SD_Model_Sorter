import shutil
import os



class ModelInfo:

    def __init__(self, id, name, type, currentDir):
        self.modelId = id
        self.name = name
        self.type = type
        self.currentDir = currentDir
        self.targetDir = ''
        self.needsmove = False


    def move_files(self, dir_dict, ext_dict):
        # move files if necessary
        if self.needsmove and len(self.targetDir) > 3:
            for ext in ext_dict:
                if os.path.isfile(self.currentDir + "\\" + self.name + "." + ext_dict[ext]):
                    cur_sor = self.currentDir + "\\" + self.name + "." + ext_dict[ext]
                    cur_tar = self.targetDir + "\\" + self.name + "." + ext_dict[ext]
                    shutil.move(cur_sor, cur_tar)
                    self.needsmove = False
                    print(f"moving  . . . {cur_sor} to {cur_tar}")

    def presort(self, dir_dict):
        # determine if the file needs to move and where
        if (self.type in dir_dict):
            self.targetDir = dir_dict["root"] + dir_dict[self.type]
            if (self.targetDir != self.currentDir):
                self.needsmove = True


