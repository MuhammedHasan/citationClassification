from DbContext import Paper
from DbContext import settings
import tarfile
from tarfile import TarInfo
# p = Paper('10.1.1.1.1519')
#
# print 'number of citation =>', len(p.citations)
# print '-' * 10
#
# for i in p.citations:
#     print i.raw
#     print i.context
#     print '-' * 8, '\n'

tr = tarfile.open(settings.TEXT_FILES_LOCATION, 'r|gz')
filename = './10/1/1/582/9667/10.1.1.582.9667.txt'
for t in tr:
    if filename in t.name:
        tr.extractfile(t).read()
