#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by C.L.Wang


HADOOP_SUBMIT_NODE = 'hive_server'
HADOOP_HIVE_SERVER_PORT = 10000
# 需要与/etc/hive/conf/hive-site.xml中的配置hive.server2.authentication保持一致
AUTH_MECHANISM = 'NOSASL'
DEFAULT_HIVE_FIELD_SEPARATOR = u'\t'  # 默认字段分隔符


def pre_process_hql(hql):
    """
    预处理,去掉最后的';'
    :param hql:
    :return:
    """
    hql = hql.strip()
    return hql[:-1] if hql[-1] == ';' else hql


def execute_hql(hql, raise_exception=True):
    """
    执行hql
    :param hql:
    :param raise_exception:
    :return: result, error_msg
    """
    # 放内部调是为了测试用例不报import error
    import pyhs2
    from pyhs2.error import Pyhs2Exception

    hql = pre_process_hql(hql)
    print 'HQL:\n  ', hql
    try:
        with pyhs2.connect(host=HADOOP_SUBMIT_NODE,
                           port=HADOOP_HIVE_SERVER_PORT,
                           authMechanism=AUTH_MECHANISM,
                           database='default') as conn:
            with conn.cursor() as cur:
                # Execute query
                cur.execute(hql)
                # Fetch table results
                result = cur.fetchall()
                return result, ''
    except Exception as e:
        if raise_exception:
            raise e
        msg = e.errorMessage if isinstance(e, Pyhs2Exception) else '%s' % e.message
        return None, '%s\nException: %s' % (hql, msg)


print execute_hql("describe orc_elapsed_log")
