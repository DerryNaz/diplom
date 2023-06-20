import request


# Проверка кода ответа
def test_track():
    status_code = request.post_orders_track()  # Сохраняем полученный статус
    assert status_code == 200  # Проверяем статус ответа

# Трубавина Дарья, 5-я когорта, финальный проект, инженер по тестированию плюс