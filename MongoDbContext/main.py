from scraper import *

for i in xrange(1, 10000):
    xml_to_mongo("10/1/1/582/" + str(i) + "/" + '10.1.1.582.' + str(i))
