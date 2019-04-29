from whoosh import *
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from whoosh.fields import *
import wikipedia

index_path = r"C:\Users\Abhi\Downloads\Index"
ix = open_dir(index_path)
mparser = MultifieldParser(["title", "content"], schema=ix.schema)

def search():
    query=input("Hi How can I help you")
    q = mparser.parse(str(query))
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=20)
        for result in results:
            print(result['content'])
            print(wikipedia.summary(result['title'],sentences=2))



if __name__ == '__main__':
    search()

    '''if len(result) != 0:
        return render_template("search.html", results=result)
    else:
        return render_template("NotFound.html")'''