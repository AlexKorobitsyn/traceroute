import requests
import re
import json
from icmplib import traceroute


name = input("Напишите адрес до которого надо найти маршрут: ")
tracert_hops = traceroute(name)
arr_res = []

for hop in tracert_hops:
    arr_res.append(hop.address)
# reg_name = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
max_indent_AS = 40
max_indent_country = 20
max_indent_ip = len(max(arr_res, key=len)) + 2
print("IP:", (max_indent_ip-4)*" ",  "AS:", (max_indent_AS-4)*" ",
      "Country:", (max_indent_country-4)*" ", "ISP:", '\n')
for ip in arr_res:
    url = 'http://ip-api.com/json/' + ip
    data = json.loads(requests.get(url).text)
    if data['status'] == 'fail':
        str_as = "That local ip"
        country = "World"
        isp = "-"
    else:
        str_as = data['as']
        country = data['country']
        isp = data['isp']
    if len(ip) < max_indent_ip:
        ip += " " * (max_indent_ip-len(ip))
    if len(str_as) < max_indent_AS:
        str_as += " " * (max_indent_AS-len(str_as))
    if len(country) < max_indent_country:
        country += " " * (max_indent_country-len(country))
    print(ip, str_as, country, isp)
