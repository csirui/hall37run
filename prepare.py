#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from optparse import Values

from webmgr.action.actthread import thread_run_action


def main():
    options = Values()
    options.httpport = 8877
    options.logfile = os.path.abspath('logs/webmagr.log')
    options.logpath = os.path.abspath('logs')
    options.pokerpath = os.path.abspath('conf/ide')
    options.workpath = os.path.abspath('webmgr')
    params = {
        "action": "prepare",
        "params": {},
        "uuid": "20170306_180155_0001",
        "time": "20170306_180155",
        "user": "zqh"
    }
    thread_run_action(options, params)


if __name__ == '__main__':
    main()
