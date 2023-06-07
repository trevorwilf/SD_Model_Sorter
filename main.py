import os
import json
import functions as fun
from model_lib import ModelInfo
import shutil
#import requests


### search directories
dir_root = "W:\SDM_testing"
dir_presort = "\presort"
dir_lycoris = "\lyCORIS"
dir_lora = "\Lora"

# extension
type_info = "civitai.info"
type_png = "preview.png"
type_safetensors = "safetensors"

dir_dict = {
    "root": dir_root,
    "presort": dir_presort,
    "LoCon": dir_lycoris,
    "LORA": dir_lora
}

ext_dict = {
    "type_info": type_info,
    "type_png": type_png,
    "type_safetensors": type_safetensors,
}


# a list of model objects
tensorlist = fun.ingest_files(dir_dict)
tensor_obj = fun.create_tensorobject(dir_dict, ext_dict, tensorlist)

# determine if it needs to move
for model in tensor_obj:
    model.presort(dir_dict)

# run sort
for model in tensor_obj:
    model.move_files(dir_dict, ext_dict)