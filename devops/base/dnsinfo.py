#coding:utf-8
#!/usr/bin/env python
import dns.resolver
domain = raw_input('Please input an domain: ')
A = dns.resolver.query(domain,'A')
for i in A.response.answer:
    print i
    for j in i.items:
        print j.address
