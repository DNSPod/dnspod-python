#!/usr/bin/env python

# ...

from distutils.core import setup

setup(name='dnspod-python',
      version='0.01',
      description='dnspod-python: DNSPod API python library',
      author='Chuangbo Li',
      author_email='im@chuangbo.li',
      url=' http://www.dnspod.com/',
      packages=['dnspod'],
      long_description="Assemble DNSPod functions with your own program. Build your own dns hosting service.",
      license="GPL 3.0",
      platforms=["any"],
     )
