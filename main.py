from DbContext import Paper
from DbContext import settings
import tarfile
#
# p = Paper('10.1.1.1.1519')
#
# print 'number of citation =>', len(p.citations)
# print '-' * 10
#
# for i in p.citations:
#     print i.raw
#     print i.context
#     print '-' * 8, '\n'

t = tarfile.open(settings.XML_FILES_LOCATION, "r:gz")
print t.getmember(Paper._file_id_to_location('10.1.1.1.1519') + '.xml')
# print t.gettarinfo(Paper._file_id_to_location('10.1.1.1.1519') + '.xml')
