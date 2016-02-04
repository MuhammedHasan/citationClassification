import unittest
import settings
from paper import Paper
from collections import OrderedDict


class TestPaperStaticMethods(unittest.TestCase):

    #  TODO : Write test for all of them

    def setUp(self):
        self.id = '10.1.1.582.1'
        settings.TEXT_FILES_LOCATION = 'test/test_text.tar.gz'
        settings.XML_FILES_LOCATION = 'test/test_xml.tar.gz'

    def test__file_id_to_location(self):
        location = Paper._file_id_to_location(self.id)
        self.assertEqual(location, '10/1/1/582/1/10.1.1.582.1')

    def test__xml_file_to_dict(self):
        xml_dict = Paper._xml_file_to_dict(self.id)
        self.assertEqual(type(xml_dict), OrderedDict)
        self.assertIsNotNone(xml_dict['document']['@id'])


class TestPaper(unittest.TestCase):

    def setUp(self):
        settings.TEXT_FILES_LOCATION = 'test/test_text.tar.gz'
        settings.XML_FILES_LOCATION = 'test/test_xml.tar.gz'
        self.id = '10.1.1.582.1'
        self.paper = Paper(self.id)

    def test_init(self):
        self.assertIsNotNone(self.paper.id)
        self.assertEqual(self.id,self.paper.id)

if __name__ == '__main__':
    unittest.main()
