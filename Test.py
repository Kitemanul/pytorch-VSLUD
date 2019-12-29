import h5py
import os
import numpy as np

dir_base = "datasets"
dataset_name_list = ["summe", "tvsum", "youtube", "ovp"]
f=h5py.File("{}/eccv16_dataset_{}_google_pool5.h5".format(dir_base,dataset_name_list[0]),'r')


for group in f.keys():

    print(f[group]['features'])
    n = f[group]['features']
    data = np.array(n)
    print(data)
    print(f[group]['n_frame_per_seg'])
    n=f[group]['n_frames']
    data = np.array(n)
    print(data)
    #print(f[group]['n_frames'])

pass

# import os
# import torch
#
# # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# # print(device)
# # pass
#
# import torch.nn as nn
# label = torch.full((1,), 1)
# output=torch.tensor(0.6731)
# result=nn.BCELoss()
# d=result(output,label)
# print()
# pass