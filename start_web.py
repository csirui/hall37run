#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), os.path.abspath('webmgr')))
    exec 'import main'
    exec 'main.main()'


if __name__ == '__main__':
    """
    sh ./script/nohup.sh --httpport=8877 --path  ../../source/config_test 2>&1 > ./logs/nohup.out
    """
main()
