import json
import os
from model_lib import ModelInfo

def ingest_files(dir_dict):
    '''
    Reads in the sort directory, and puts the newly created object into a list
    :param dir_dict:
    :return:
    '''

    tensorlist = []
    for file in os.listdir(dir_dict["root"] + dir_dict["presort"]):
        # only use specific files
        if file.endswith('.safetensors'):
            tensorlist.append(file)

    return(tensorlist)

def create_tensorobject(dir_dict, ext_dict, tensorlist):

    tensorobject_list = []

    for cur_tn in tensorlist:
        # find file name stub
        cur_tn_name_sub = os.path.splitext(dir_dict["root"] + dir_dict["presort"] + "\\" + cur_tn )[0]

        # move forward only if civtia file exists
        if os.path.isfile(cur_tn_name_sub + "." +ext_dict["type_info"]):
            #read in json file
            cur_obj = ''
            #print(f'current model: {cur_tn_name_sub}')

            f = open(cur_tn_name_sub + "." +ext_dict["type_info"])
            cur_json = json.load(f)

            if ("id" in cur_json):
                try:
                    cur_obj = ModelInfo(id = cur_json["id"],
                                        name = os.path.splitext(cur_tn)[0],
                                        type = cur_json["model"]["type"],
                                        currentDir = dir_dict["root"] + dir_dict["presort"])
                except:
                    print(f'current model: {cur_tn_name_sub}')

                try:
                    tensorobject_list.append(cur_obj)
                except:
                    print(f'current model: {cur_tn_name_sub}')

    return tensorobject_list
