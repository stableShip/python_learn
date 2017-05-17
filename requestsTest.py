#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

# requests api参照: https://github.com/kennethreitz/requests

url = "http://www.baidu.com"
data = requests.get(url)
print "请求返回状态码: %s, 返回内容: %s" % (data.status_code, data.content)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')
assert "百度" in browser.title
print browser.title


browser.quit()