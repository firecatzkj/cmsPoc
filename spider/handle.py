# -*- coding: utf-8 -*-
from urllib.parse import urlparse
for i in open("url.txt", "r+").readlines():
    res = urlparse(i)
    print(res[0],res[1])
    with open("url_clear.txt", "a+") as f2:
        clear_url = res[0] + "://" + res[1] + "/index.php"
        f2.write(clear_url + "\n")
