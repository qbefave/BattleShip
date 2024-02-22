error_message1 = 'Диапазон значений координат [1,6]'
error_message2 = 'Ячейка уже поражена'

class BaseExeption(Exception):
    pass
class OutOfFieldExeption(BaseExeption):
    def __str__(self):
        return error_message1
class HittedFieldExeption(BaseExeption):
    def __str__(self):
        return error_message2
class ShipExeption(BaseExeption):
    pass