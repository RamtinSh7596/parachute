from flask import Flask, request, jsonify
from flask_cors import CORS
from reader import FileReader

app = Flask(__name__)
CORS(app)
reader = FileReader('./data/IR-F19-Project01-Input.xlsx', './matches.json')


@app.route('/')
def query():
    q = request.args.get('q')
    docs = reader.search(q)
    results = [{
        'publish_date': doc.publish_date,
        'title': doc.title,
        'url': doc.url,
        'summary': doc.summary,
        'meta_tags': doc.meta_tags,
        'content': doc.content,
        # 'thumbnail': doc.thumbnail,
    } for doc in docs]
    print(len(results), "results found")
    return jsonify({
        "query": q,
        "result": results,
    })


if __name__ == '__main__':
    app.run()
