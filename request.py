import configuration
import data
import requests

# Создание заказа
def post_orders_track():
    response = requests.post(configuration.URL_SERVICE + configuration.ORDERS_NEW,  # подставляем полный url
                          json=data.user_body)
    return response.json()["track"]


# Получение заказа
def get_orders():
    return requests.get(configuration.URL_SERVICE + "?t=" + str(configuration.RECEIVE_AN_ORDER))


def track_id():
 return track_id.json()["track"]