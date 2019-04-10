#!/usr/bin/env python
# -*- coding:utf-8 -*-


from dnspod import apicn


def main():
    # please refer to:
    # https://support.dnspod.cn/Kb/showarticle/tsid/227/
    login_token = "Your TOKEN here"

    domain = "Your DOMAIN here"

    print "DomainCreate", domain
    api = apicn.DomainCreate(domain, login_token=login_token)

    domain_id = api().get("domain", {}).get("id")
    print "%s's id is %s" % (domain, domain_id)

    print "DomainList"
    api = apicn.DomainList(login_token=login_token)
    print api().get("domains")

    print "RecordType"
    api = apicn.RecordType("D_Ultra", login_token=login_token)
    print api().get("types")

    print "RecordLine"
    api = apicn.RecordLine("D_Free", login_token=login_token)
    print api().get("lines")

    print "RecordCreate"
    api = apicn.RecordCreate("www", "A", u'默认'.encode("utf8"), '1.1.1.1', 600, domain_id=domain_id, login_token=login_token)
    record = api().get("record", {})
    record_id = record.get("id")
    print "Record id", record_id

    print "RecordList"
    api = apicn.RecordList(domain_id, login_token=login_token)
    print api().get("records")

    print "DomainRemove"
    api = apicn.DomainRemove(domain_id, login_token=login_token)
    print api()


if __name__ == '__main__':
    main()
