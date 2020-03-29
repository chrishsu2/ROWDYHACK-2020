# -*- coding: utf-8 -*-
# @Author: Christopher Hsu
# @Date:   2020-03-28 12:39:59
# @Last Modified by:   Christopher Hsu
# @Last Modified time: 2020-03-28 12:40:08
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
