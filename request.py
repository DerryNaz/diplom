import configuration
import data
import requests


# Создание заказа
def post_orders_track():
    orders_track = requests.post(configuration.URL_SERVICE + configuration.ORDERS_NEW,  # подставляем полный url
                                 json=data.user_body)  # Тут тело
    track_number = orders_track.json()["track"]  # Трек нового заказа в переменной
    get_orders = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_AN_ORDER + "?t=" + str(
        track_number))  # Получения заказа по треку
    return get_orders.status_code  # Статус ответа
