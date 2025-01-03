class PasswordAnalyzer:
    def analyze(self, password: str) -> tuple[str, str]:
        length = len(password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "!@#$%^&*()" for char in password)

        if length < 8:
            return "Слабый", "Пароль слишком короткий. Минимальная длина — 8 символов."
        elif has_upper and has_lower and has_digit and has_special:
            return "Сильный", "Пароль надежен."
        else:
            return "Средний", "Добавьте больше символов разных типов (заглавные, цифры, спецсимволы)."
