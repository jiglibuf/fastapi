from fastapi import HTTPException, status

class BookingException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail='Пользователь уже существует'


class IncorrectEmailOrPasswordException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail= 'Неверная почта или пароль',

class TokenExpiredException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Токен истек'

class TokenAbsentException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Токен отсутствует'

class IncorrectTokenFormatException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Неверный формат токена'

class UserIsNotInTokenException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED

class RoomCannotBeBooked(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail='Не осталось свободных номеров'

class MissedBooking(BookingException):
    status_code=status.HTTP_404_NOT_FOUND
    detail='Бронирование не найдено'


#---------------------------------------
class MissedHotel(BookingException):
    status_code=status.HTTP_404_NOT_FOUND
    detail='Отель не найден'

class NoHotelsInLocation(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail='Отелей в этой локации нет'