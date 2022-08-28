from flask import current_app as app, request, jsonify

from . import models, db


# Создаем вьюшки для User на получение, добавление

@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        user_data = request.json
        new_user = models.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200


# Создаем вьюшки для User на получение, обновление и удаление данных

@app.route('/users/<int:idx>', methods=['GET', 'PUT', 'DELETE'])
def user_functions(idx):
    if request.method == 'GET':
        user = models.User.query.get(idx)
        return jsonify(user.to_dict()), 200
    if request.method == 'PUT':
        user_data = request.json
        user = models.User.query.det(idx)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(idx)
        return jsonify(user.to_dict())

    if request.method == 'DELETE':
        user = models.User.query.get(idx)
        db.session.delete(user)
        db.session.commit()

        return '', 200


# Создаем вьюшки для Offer на получение, добавдение

@app.route('/offers/', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        offer_data = request.json
        new_offer = models.Offer(**offer_data)

        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result), 200


# Создаем вьюшки для Offer на получение, обновление и удаление данных

@app.route('/offers/<int:idx>', methods=['GET', 'PUT', 'DELETE'])
def offer_functions(idx):
    if request.method == 'GET':
        offer = models.Offer.query.get(idx)
        return jsonify(offer.to_dict()), 200
    if request.method == 'PUT':
        offer_data = request.json
        offer = models.Offer.query.det(idx)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = models.Offer.query.get(idx)
        return jsonify(offer.to_dict())

    if request.method == 'DELETE':
        offer = models.Offer.query.get(idx)
        db.session.delete(offer)
        db.session.commit()

        return '', 200


# Создаем вьюшки для Order на получение, добавдение

@app.route('/orders/', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        order_data = request.json
        new_order = models.User(**order_data)

        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200


# Создаем вьюшки для Order на получение, обновление и удаление данных

@app.route('/orders/<int:idx>', methods=['GET', 'PUT', 'DELETE'])
def order_functions(idx):
    if request.method == 'GET':
        order = models.Order.query.get(idx)
        return jsonify(order.to_dict()), 200
    if request.method == 'PUT':
        order_data = request.json
        order = models.Order.query.det(idx)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']

        db.session.add(order)
        db.session.commit()

        order = models.User.query.get(idx)
        return jsonify(order.to_dict())

    if request.method == 'DELETE':
        order = models.Order.query.get(idx)
        db.session.delete(order)
        db.session.commit()

        return '', 200
