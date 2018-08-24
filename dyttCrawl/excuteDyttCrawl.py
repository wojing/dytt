from scrapy import cmdline
import platform

if platform.system() == "Windowns":
    cmdline.execute("scrapy crawl dytt -s JOBDIR=/log".split())
else:
    cmdline.execute("scrapy crawl dytt -s JOBDIR=./log".split())
