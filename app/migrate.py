import json
from . import models, db


# Получаем данные и преобразуем их из JSON
def load_data(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)

    return json_data

def load_users(filename):
    users = load_data(filename)

    for user in users:
        '''Делаем распаковку'''
        new_user = models.User(**user)
        db.session.add(new_user)

    db.session.commit()

def load_offers(filename):
    offers = load_data(filename)

    for offer in offers:
        '''Делаем распаковку'''
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)

    db.session.commit()

def load_orders(filename):
    orders = load_data(filename)

    for order in orders:
        '''Делаем распаковку'''
        new_order = models.Order(**order)
        db.session.add(new_order)

    db.session.commit()
    #print(models.User.query.get(1).to_dict())

