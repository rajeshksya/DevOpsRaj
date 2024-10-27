from flask import Flask, request, jsonify

@app.route('/product', methods=["POST"])
def add_product():
    title = request.json['title']
    content = request.json['content']

    new_product = Product(title, content)

    db.session.add(new_product)
    db.session.commit()

    product = PRoduct.query.get(new_product.id)

    return product_schema.jsonify(product)