from flask import Flask, request, jsonify
from flask_cors import CORS
from file_reader import search, get_docs

app = Flask(__name__)
CORS(app)


@app.route('/')
def query():
    q = request.args.get('q')
    docs = get_docs(search(q))
    results = [{
        'publish_date': doc.publish_date,
        'title': doc.title,
        'url': doc.url,
        'summary': doc.summary,
        'meta_tags': doc.meta_tags,
        'content': doc.content,
        # 'thumbnail': doc.thumbnail,
    } for doc in docs]
    print("<span style='font-weight: bold'>{0}</span>".format("The Text"))
    print(len(results), "results found")
    return jsonify({
        "q": q,
        "result": results
    })


if __name__ == '__main__':
    app.run()
