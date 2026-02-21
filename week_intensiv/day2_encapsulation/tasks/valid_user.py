class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val):
        if len(self._password) < 8:
            raise ValueError('Ваш пароль слишком короткий')
        a = 0
        for i in '0123456789':
            if i in self._password:
                a = 1
            if a == 0:
                raise ValueError('Цифры отсутствуют')
            self._password = val
