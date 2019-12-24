import math
from flask import Flask, request, jsonify
from flask_cors import CORS
from reader import FileReader, Bolder

app = Flask(__name__)
CORS(app)
reader = FileReader('./data/IR-F19-Project01-Input.xlsx', './matches.json', './exceptions.txt')
bolder = Bolder()


@app.route('/')
def query():
    q = request.args.get('q')
    print("Query:", q)
    docs, query_tokens = reader.search(q)
    docs, query_tokens = list(docs), list(query_tokens)
    print("Results:", len(docs))
    items = int(request.args.get('items', 10))
    print("Items:", items)
    pages = math.ceil(len(docs) / items)
    print("Pages:", pages)
    page = int(request.args.get('page', 0))
    print("Page:", page)
    start = min(page * items, len(docs))
    print("Start:", start)
    end = min((page + 1) * items, len(docs))
    print("End:", end)
    articles = [{
        'publish_date': doc.publish_date,
        'title': str(doc.title),
        'url': doc.url,
        'summary': bolder.bold(str(doc.summary), query_tokens),
        'meta_tags': doc.meta_tags,
        'content': bolder.bold(str(doc.content), query_tokens),
        'thumbnail': str(doc.thumbnail),
    } for doc in docs[start:end]]
    return jsonify({
        "query": q,
        "items": items,
        "pages": pages,
        "page": page,
        "articles": articles,
    })


if __name__ == '__main__':
    app.run()
