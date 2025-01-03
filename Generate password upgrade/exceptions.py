class PasswordError(Exception):
    """Базовый класс для всех исключений."""
    pass

class InvalidMaskError(PasswordError):
    def __init__(self, mask):
        self.message = f"Некорректная маска: {mask}. Проверьте символы (A, a, 0, $)."
        super().__init__(self.message)

class PasswordTooShortError(PasswordError):
    def __init__(self, length):
        self.message = f"Пароль должен быть не менее 8 символов. Указанная длина: {length}."
        super().__init__(self.message)
