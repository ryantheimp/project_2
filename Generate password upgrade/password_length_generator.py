import random
import string
from exceptions import PasswordTooShortError

class PasswordLengthGenerator:
    def generate_password_by_settings(self, length: int, use_uppercase: bool, use_lowercase: bool,
                                       use_digits: bool, use_special: bool) -> str:
        if length < 8:
            raise PasswordTooShortError(length)

        char_pool = ""
        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_lowercase:
            char_pool += string.ascii_lowercase
        if use_digits:
            char_pool += string.digits
        if use_special:
            char_pool += "!@#$%^&*()"

        if not char_pool:
            raise ValueError("Не выбраны символы для генерации пароля.")

        password = "".join(random.choice(char_pool) for _ in range(length))
        return password
