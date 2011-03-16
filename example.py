#!/usr/bin/env python
#-*- coding:utf-8 -*-

from dnspod.apicn import *

def main():
    email = "Your Email Here"
    password = "Your Password Here"
    
    import random
    domain = "test%d.com" % random.randint(1000, 100000)
    
    print "DomainCreate", domain
    api = DomainCreate(domain, email=email, password=password)
    
    domain_id = api().get("domain", {}).get("id")
    print "%s's id is %s" % (domain, domain_id)
    
    print "DomainList"
    api = DomainList(email=email, password=password)
    print api().get("domains")
    
    print "RecordType"
    api = RecordType("D_Ultra", email=email, password=password)
    print api().get("types")
    
    print "RecordLine"
    api = RecordLine("D_Free", email=email, password=password)
    print api().get("lines")
    
    print "RecordCreate"
    api = RecordCreate("www", "A", u'默认'.encode("utf8"), '1.1.1.1', 600, domain_id=domain_id, email=email, password=password)
    record = api().get("record", {})
    record_id = record.get("id")
    print "Record id", record_id
    
    print "RecordList"
    api = RecordList(domain_id, email=email, password=password)
    print api().get("records")
    
    print "DomainRemove"
    api = DomainRemove(domain_id, email=email, password=password)
    print api()
    
if __name__ == '__main__':
    main()