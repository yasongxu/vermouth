# -*- coding: utf-8 -*-
import json

'''判断是否可以json化'''


def is_json(j):
    try:
        data = json.loads(j)
    except ValueError:
        return False
    return data