import mimetypes
from visitor import SearchVisitor

class SearchMimeVisitor(SearchVisitor):

    def candidate(self, fname):
        contype, encoding = mimetypes.guess_type(fname)
        return (contype and contype.split('/')[0] == 'text' and encoding == None)


V = SearchMimeVisitor('def', trace=0)
V.run(r'/home/vestenar/EDU')
