from xmltodict import *
import settings


class Paper:

    def __init__(self, id):
        f = self._file_to_dict(self._file_id_to_location(id) + '.xml')
        doc = f['document']
        self.id = doc['@id']

        if keys_exist(doc, 'title', '#text'):
            self.title = doc['title']['#text']

        if keys_exist(doc, 'abstract', '#text'):
            self.abstract = doc['abstract']['#text']

        self.authors = get_authors(doc)
        self.citations = get_citations(doc)

        self.content = open(file_id + '.txt').read()

    def _file_to_dict(self, fileName):
        f = open(fileName, 'r')
        return xmltodict.parse(f.read())

    def _file_id_to_location(self, id):
        return settings.DATA_LOCATION + '/' + id.replace('.', '/') + '/'

    def _get_authors(self, doc):
        authors = list()
        if keys_exist(doc, 'authors', 'author'):
            auts = doc['authors']['author']
            auts = self._to_list_if_not(auts)
            for i in auts:
                a = Author()
                a.id = i['@id']
                a.name = i['name']['#text']
                a.order = i['order']
                authors.append(a)
        return authors

    def _get_citations(self, doc):
        citations = list()
        if keys_exist(doc, 'citations', 'citation'):
            cits = doc['citations']['citation']
            cits = self._to_list_if_not(cits)
            for i in cits:
                ct = Citation()
                ct.paperid = i['@id']
                ct.raw = i['raw']
                ctx = get_context_of_citation(i)
                if ctx != []:
                    ct.context = ctx
                citations.append(ct)
        return citations

    def _get_context_of_citation(self, citation):
        contexts = list()
        if keys_exist(citation, 'contexts', 'context'):
            ctx = citation['contexts']['context']
            contexts = self._to_list_if_not(ctx)
        return contexts

    def _keys_exist(self, doc, key1, key2):
        if key1 in doc.keys():
            if type(doc[key1]) == dict or type(doc[key1]) == OrderedDict:
                if key2 in doc[key1].keys():
                    return True
        return False

    def _to_list_if_not(self, doc):
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
