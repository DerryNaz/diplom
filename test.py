import request

# Проверка кода ответа
def test_track():

    track_id = request.get_orders()
    assert track_id.status_code == 200

# Трубавина Дарья, 5-я когорта, финальный проект, инженер по тестированию плюс