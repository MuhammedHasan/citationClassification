import xmltodict
import pprint
from publication import *
from collections import OrderedDict


def xml_to_mongo(file_id):
    connect('Publication')
    pub = Publication()
    f = file_to_dict(file_id + '.xml')
    doc = f['document']
    print doc['@id']

    pub.dataid = doc['@id'].replace('.', '')

    if keys_exist(doc, 'title', '#text'):
        pub.title = doc['title']['#text']

    if keys_exist(doc, 'abstract', '#text'):
        pub.abstract = doc['abstract']['#text']

    authors = get_authors(doc)
    if len(authors) != 0:
        pub.authors = authors

    citations = get_citations(doc)
    if len(citations) != 0:
        pub.citations = get_citations(doc)

    pub.content = open(file_id + '.txt').read()
    pub.save()


def file_to_dict(fileName):
    f = open(fileName, 'r')
    return xmltodict.parse(f.read())


def get_authors(doc):
    authors = list()
    if keys_exist(doc, 'authors', 'author'):
        auts = doc['authors']['author']
        auts = to_list_if_not(auts)
        for i in auts:
            a = Author()
            a.dataid = i['@id']
            a.name = i['name']['#text']
            a.order = i['order']
            authors.append(a)
    return authors


def get_citations(doc):
    citations = list()
    if keys_exist(doc, 'citations', 'citation'):
        cits = doc['citations']['citation']
        cits = to_list_if_not(cits)
        for i in cits:
            ct = Citation()
            ct.publicationid = i['@id']
            ct.raw = i['raw']
            ctx = get_context_of_citation(i)
            if ctx != []:
                ct.context = ctx
            citations.append(ct)
    return citations


def get_context_of_citation(citation):
    contexts = list()
    if keys_exist(citation, 'contexts', 'context'):
        ctx = citation['contexts']['context']
        contexts = to_list_if_not(ctx)
    return contexts


def keys_exist(doc, key1, key2):
    if key1 in doc.keys():
        if type(doc[key1]) == dict or type(doc[key1]) == OrderedDict:
            if key2 in doc[key1].keys():
                return True
    return False


def to_list_if_not(doc):
    if type(doc) != list:
        doc = [doc]
    return doc
