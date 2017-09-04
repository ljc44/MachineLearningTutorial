#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by C.L.Wang

from tensorflow.python.client import device_lib


def get_available_gpus():
    """
    查看GPU的命令：nvidia-smi
    :return: GPU个数
    """
    local_device_protos = device_lib.list_local_devices()
    print [x.name for x in local_device_protos]
    gpu_names = [x.name for x in local_device_protos if x.device_type == 'GPU']
    return gpu_names


print get_available_gpus()
