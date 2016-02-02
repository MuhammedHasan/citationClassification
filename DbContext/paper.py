import xmltodict
import settings
import tarfile
from collections import OrderedDict


class Paper:

    def __init__(self, id):
        f = Paper._xml_file_to_dict(id)
        doc = f['document']
        self.id = doc['@id']

        if Paper._keys_exist(doc, 'title', '#text'):
            self.title = doc['title']['#text']

        if Paper._keys_exist(doc, 'abstract', '#text'):
            self.abstract = doc['abstract']['#text']

        self.authors = Paper._get_authors(doc)
        self.citations = Paper._get_citations(doc)

    #    self.content = open(file_id + '.txt').read()

    @staticmethod
    def _xml_file_to_dict(id):
        t = tarfile.open(settings.XML_FILES_LOCATION, 'r')
        f = t.extractfile(Paper._file_id_to_location(id) + '.xml')
        return xmltodict.parse(f.read())

    @staticmethod
    def _file_id_to_location(id):
        return id.replace('.', '/') + '/' + id

    @staticmethod
    def _get_authors(doc):
        authors = list()
        if Paper._keys_exist(doc, 'authors', 'author'):
            auts = doc['authors']['author']
            auts = Paper._to_list_if_not(auts)
            for i in auts:
                a = Author(i['@id'], i['name']['#text'], i['order'])
                authors.append(a)
        return authors

    @staticmethod
    def _get_citations(doc):
        citations = list()
        if Paper._keys_exist(doc, 'citations', 'citation'):
            cits = doc['citations']['citation']
            cits = Paper._to_list_if_not(cits)
            for i in cits:
                ct = Citation(i['@id'], i['raw'],)
                ctx = Paper._get_context_of_citation(i)
                if ctx != []:
                    ct.context = ctx
                citations.append(ct)
        return citations

    @staticmethod
    def _get_context_of_citation(citation):
        contexts = list()
        if Paper._keys_exist(citation, 'contexts', 'context'):
            ctx = citation['contexts']['context']
            contexts = Paper._to_list_if_not(ctx)
        return contexts

    @staticmethod
    def _keys_exist(doc, key1, key2):
        if key1 in doc.keys():
            if type(doc[key1]) == dict or type(doc[key1]) == OrderedDict:
                if key2 in doc[key1].keys():
                    return True
        return False

    @staticmethod
    def _to_list_if_not(doc):
        if type(doc) != list:
            doc = [doc]
        return doc


class Author:

    def __init__(self, id, name, order):
        self.id = id
        self.name = name
        self.order = order


class Citation:

    def __init__(self, id, raw, context=str()):
        self.paperid = id
        self.raw = raw
        self.context = context
