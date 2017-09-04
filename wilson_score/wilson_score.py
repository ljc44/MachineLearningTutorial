#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by C.L.Wang

import numpy as np


def wilson_score(pos, total, p_z=2.):
    """
    威尔逊得分计算函数
    参考：https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    :param pos: 正例数
    :param total: 总数
    :param p_z: 正太分布的分位数
    :return: 威尔逊得分
    """
    if total <= 0. or pos < 0.:
        return 0.
    pos_rat = float(pos) / float(total)  # 正例比率
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score


# 假设医生A有100个评价，1个差评99个好评。医生B有2个评价，都是好评，那哪个应该排前面？
print 'score: %s' % wilson_score(99, 99 + 1)
print 'score: %s' % wilson_score(2, 2 + 0)
