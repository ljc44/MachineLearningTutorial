#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 常用方法
# Created by C.L.Wang

from __future__ import absolute_import

import collections
import datetime
import os
import random
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if p not in sys.path:
    sys.path.append(p)

import glob
import json
import os
import re
import numpy as np
import operator

from itertools import izip


class ProgressBar:
    """
    进度条类
    bar = ProgressBar(total = 10)
    for i in range(10):
        bar.move()
        bar.log('We have arrived at: ' + str(i + 1))
        time.sleep(1)
    """

    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()


def remove_punctuation(line):
    """
    去除所有半角全角符号，只留字母、数字、中文
    :param line: 
    :return: 
    """
    rule = re.compile(ur"[^a-zA-Z0-9\u4e00-\u9fa5]")
    line = rule.sub('', line)
    return line


def check_punctuation(word):
    pattern = re.compile(ur"[^a-zA-Z0-9\u4e00-\u9fa5]")
    if pattern.search(word):
        return True
    else:
        return False


def clean_text(text):
    """
    text = "hello      world  nice ok    done \n\n\n hhade\t\rjdla"
    result = hello world nice ok done hhade jdla
    将多个空格换成一个
    :param text: 
    :return: 
    """
    if not text:
        return ''
    return re.sub(r"\s+", " ", text)


def merge_files(folder, merge_file):
    """
    将多个文件合并为一个文件
    :param folder: 文件夹
    :param merge_file: 合并后的文件
    :return: 
    """
    paths, _, _ = listdir_files(folder)
    with open(merge_file, 'w') as outfile:
        for file_path in paths:
            with open(file_path) as infile:
                for line in infile:
                    outfile.write(line)


def random_pick(some_list, probabilities):
    """
    根据概率随机获取元素
    :param some_list: 元素列表 
    :param probabilities: 概率列表
    :return: 当前元素
    """
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    item = some_list[0]
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def intersection_of_lists(l1, l2):
    """
    两个list的交集
    :param l1: 
    :param l2: 
    :return: 
    """
    return list(set(l1).intersection(set(l2)))


def safe_div(x, y):
    """
    安全除法
    :param x: 分子
    :param y: 分母
    :return: 除法
    """
    if y == 0:
        return 0
    return x / y


def invert_dict(d):
    """
    当字典的元素不重复时, 反转字典
    :param d: 字典
    :return: 反转后的字典
    """
    return dict((v, k) for k, v in d.iteritems())


def init_num_dict():
    """
    初始化值是int的字典
    :return: 
    """
    return collections.defaultdict(int)


def sort_dict_by_value(dict_, reverse=True):
    """
    按照values排序字典
    :param dict_: 待排序字典
    :param reverse: 默认从大到小
    :return: 排序后的字典
    """
    return sorted(dict_.items(), key=operator.itemgetter(1), reverse=reverse)


def get_current_time_str():
    """
    输入当天的日期格式, 20170718_1137
    :return: 20170718_1137
    """
    return datetime.datetime.now().strftime('%Y%m%d_%H%M')


def get_current_day_str():
    """
    输入当天的日期格式, 20170718
    :return: 20170718
    """
    return datetime.datetime.now().strftime('%Y%m%d')


def remove_line_of_file(ex_line, file_name):
    ex_line = ex_line.replace('\n', '')
    lines = read_file(file_name)

    out_file = open(file_name, "w")
    for line in lines:
        line = line.replace('\n', '')  # 确认编码格式
        if line != ex_line:
            out_file.write(line + '\n')
    out_file.close()


def map_to_ordered_list(data_dict, reverse=True):
    """
    将字段根据Key的值转换为有序列表
    :param data_dict: 字典
    :param reverse: 默认从大到小
    :return: 有序列表
    """
    return sorted(data_dict.items(), key=operator.itemgetter(1), reverse=reverse)


def map_to_index_list(data_list, all_list):
    """
    转换为one-hot形式
    :param data_list: 
    :param all_list: 
    :return: 
    """
    index_dict = {l.strip(): i for i, l in enumerate(all_list)}  # 字典
    index = index_dict[data_list.strip()]
    index_list = np.zeros(len(all_list), np.float32)
    index_list[index] = 1
    return index_list


def map_to_index(data_list, all_list):
    """
    转换为one-hot形式
    :param data_list: 
    :param all_list: 
    :return: 
    """
    index_dict = {l.strip(): i for i, l in enumerate(all_list)}  # 字典
    index = index_dict[data_list.strip()]
    return index


def n_lines_of_file(file_name):
    """
    获取文件行数
    :param file_name: 文件名
    :return: 数量
    """
    return sum(1 for line in open(file_name))


def remove_file(file_name):
    """
    删除文件
    :param file_name: 文件名
    :return: 删除文件
    """
    if os.path.exists(file_name):
        os.remove(file_name)


def find_sub_in_str(string, sub_str):
    """
    子字符串的起始位置
    :param string: 字符串
    :param sub_str: 子字符串
    :return: 当前字符串
    """
    return [m.start() for m in re.finditer(sub_str, string)]


def list_has_sub_str(string_list, sub_str):
    """
    字符串是否在子字符串中
    :param string_list: 字符串列表
    :param sub_str: 子字符串列表
    :return: 是否在其中
    """
    for string in string_list:
        if sub_str in string:
            return True
    return False


def list_has_index(index_list, sub_index):
    """
    判断sub_index是否在索引列表中
    :param index_list: 索引列表(start_index, end_index)
    :param sub_index: 索引
    :return: 是否在其中
    """
    for start_index, end_index in grouped(index_list, 2):
        if start_index <= sub_index <= end_index:
            return True
    return False


def remove_last_char(str_value, num):
    """
    删除最后的字符串
    :param str_value: 字符串 
    :param num: 删除位置
    :return: 新的字符串
    """
    str_list = list(str_value)
    return "".join(str_list[:(-1 * num)])


def read_file(data_file, mode='more'):
    """
    读文件, 原文件和数据文件
    :return: 单行或数组
    """
    try:
        with open(data_file, 'r') as f:
            if mode == 'one':
                output = f.read()
                return output
            elif mode == 'more':
                output = f.readlines()
                return map(str.strip, output)
            else:
                return list()
    except IOError:
        return list()


def find_word_position(original, word):
    """
    查询字符串的位置
    :param original: 原始字符串
    :param word: 单词
    :return: [起始位置, 终止位置]
    """
    u_original = original.decode('utf-8')
    u_word = word.decode('utf-8')
    start_indexes = find_sub_in_str(u_original, u_word)
    end_indexes = [x + len(u_word) - 1 for x in start_indexes]
    return zip(start_indexes, end_indexes)


def write_list_to_file(file_name, data_list):
    """
    将列表写入文件
    :param file_name: 文件名
    :param data_list: 数据列表
    :return: None
    """
    for data in data_list:
        write_line(file_name, data)


def write_line(file_name, line):
    """
    将行数据写入文件
    :param file_name: 文件名 
    :param line: 行数据
    :return: None
    """
    if file_name == "":
        return
    with open(file_name, "a+") as fs:
        if type(line) is (tuple or list):
            fs.write("%s\n" % ", ".join(line))
        else:
            fs.write("%s\n" % line)


def show_set(data_set):
    """
    显示集合数据
    :param data_set: 数据集
    :return: None
    """
    data_list = list(data_set)
    show_string(data_list)


def show_string(obj):
    """
    用于显示UTF-8字符串, 尤其是含有中文的.
    :param obj: 输入对象, 可以是列表或字典
    :return: None
    """
    print list_2_utf8(obj)


def list_2_utf8(obj):
    """
    用于显示list汉字
    :param obj: 
    :return: 
    """
    return json.dumps(obj, encoding="UTF-8", ensure_ascii=False)


def grouped(iterable, n):
    """
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    例子:
    for x, y in grouped(l, 2):
        print "%d + %d = %d" % (x, y, x + y)
        
    :param iterable: 迭代器
    :param n: 间隔
    :return: 组合
    """
    return izip(*[iter(iterable)] * n)


def listdir_no_hidden(root_dir):
    """
    显示顶层文件夹
    :param root_dir: 根目录
    :return: 文件夹列表
    """
    return glob.glob(os.path.join(root_dir, '*'))


def listdir_files(root_dir, ext=None):
    """
    列出文件夹中的文件
    :param root_dir: 根目录
    :param ext: 类型
    :return: [文件路径(相对路径), 文件夹名称, 文件名称]
    """
    names_list = []
    paths_list = []
    dirs_list = []
    for parent, dirNames, fileNames in os.walk(root_dir):
        for name in fileNames:
            if ext:
                if name.endswith(tuple(ext)):
                    names_list.append(name)
                    paths_list.append(os.path.join(parent, name))
            else:
                names_list.append(name)
                paths_list.append(os.path.join(parent, name))
        for name in dirNames:
            dirs_list.append(name)
    return paths_list, dirs_list, names_list


def time_elapsed(start, end):
    """
    输出时间
    :param start: 开始
    :param end: 结束
    :return: 
    """
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)


def batch(iterable, n=1):
    """
    批次迭代器
    :param iterable: 迭代器
    :param n: 次数
    :return: 
    """
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]
