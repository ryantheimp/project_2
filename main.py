from password_mask_generator import PasswordMaskGenerator
from password_length_generator import PasswordLengthGenerator
from password_analyzer import PasswordAnalyzer
from password_storage import PasswordStorage
from exceptions import InvalidMaskError, PasswordTooShortError


def main():
    mask_generator = PasswordMaskGenerator()
    length_generator = PasswordLengthGenerator()
    analyzer = PasswordAnalyzer()
    storage = PasswordStorage()

    while True:
        print("\nДобро пожаловать в генератор паролей! \nВыберите функцию:")
        print("1. Сгенерировать пароль")
        print("2. Проверить надежность пароля")
        print("3. Сохранить пароли в файл")
        print("4. Информация о программе")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            print("\nВыберите метод генерации пароля:")
            print("1. По маске")
            print("2. По длине и сложности")
            method_choice = input("Введите номер метода: ")

            if method_choice == "1":
                print("\nПример маски: AA00$$\n"
                      "Где:\n"
                      " A - Заглавная буква (например: A, B, C)\n"
                      " a - Строчная буква (например: a, b, c)\n"
                      " 0 - Цифра (например: 0, 1, 2)\n"
                      " $ - Специальный символ (например: @, $, %, &)")
                mask = input("\nВведите маску пароля: ")

                try:
                    password = mask_generator.generate_password_by_mask(mask)
                    print(f"Сгенерированный пароль: {password}")
                    storage.add_password(password)
                except InvalidMaskError as e:
                    print(e)  # Выводим сообщение об ошибке для неверной маски
                except PasswordTooShortError as e:
                    print(e)

            elif method_choice == "2":
                while True:
                    try:
                        length = int(input("Введите длину пароля (от 8 до 32): "))

                        if length < 8 or length > 32:
                            raise PasswordTooShortError(length)

                        break
                    except ValueError:
                        print("Ошибка: введите корректное число.")
                    except PasswordTooShortError as e:
                        print(e)

                use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
                use_lowercase = input("Использовать строчные буквы? (y/n): ").lower() == 'y'
                use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
                use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'

                try:
                    password = length_generator.generate_password_by_settings(
                        length, use_uppercase, use_lowercase, use_digits, use_special
                    )
                    print(f"Сгенерированный пароль: {password}")
                    storage.add_password(password)
                except PasswordTooShortError as e:
                    print(e)

        elif choice == "2":
            password = input("\nВведите пароль для анализа: ")
            level, advice = analyzer.analyze(password)
            print(f"Надежность пароля: {level}")
            print(f"Рекомендации: {advice}")

        elif choice == "3":
            storage.export_to_file()
            print("\nПароли сохранены.")

        elif choice == "4":
            print("\nДанный генератор паролей позволяет:\n"
                  "- Сгенерировать пароли по заданной маске.\n"
                  "- Сгенерировать пароли по длине и сложности.\n"
                  "- Проверить надежность пароля и получить рекомендации.\n"
                  "- Сохранить сгенерированные пароли в файл.")

        elif choice == "5":
            print("\nВыход.")
            break

        else:
            print("\nНекорректный выбор. Попробуйте снова.")


# Проверка вызова main() для запуска программы
if __name__ == "__main__":
    main()
