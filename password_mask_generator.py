import random
import string
from exceptions import InvalidMaskError, PasswordTooShortError

class PasswordMaskGenerator:
    def generate_password_by_mask(self, mask: str) -> str:
        self.validate_mask(mask)
        char_map = {
            "A": string.ascii_uppercase,
            "a": string.ascii_lowercase,
            "0": string.digits,
            "$": "!@#$%^&*()"
        }
        password = "".join(random.choice(char_map[char]) for char in mask)
        if len(password) < 8:
            raise PasswordTooShortError(len(password))
        return password

    def validate_mask(self, mask: str) -> None:
        allowed_characters = {'A', 'a', '0', '$'}
        for character in mask:
            if character not in allowed_characters:
                raise InvalidMaskError(mask)
