# -*- coding:utf-8 -*-

from collections import defaultdict

co_list = [u'北京', u'有限公司', u'科技', u'公司', u'发展', u'有限责任', u'技术', u'北京市']
co_list.sort(key = lambda x:len(x), reverse = True)

name_dict = defaultdict(list)
for line in open('corp_names.file', 'r').readlines():
    line = line.strip()
    if len(line) <= 0:
	continue
    line = line.decode('utf-8')
    name = line
    for co in co_list:
        name = name.replace(co, u'')
    name_dict[name].append(line)

for name in name_dict.keys():
    if len(name_dict[name]) <= 1:
        continue
    print name.encode('utf-8')
    print u', '.join(name_dict[name]).encode('utf-8')
