# project_2
# Генератор паролей

Подготовлено:  
Каримов Артём Олегович, ИСУ: 466122

## Описание проекта

Проект создан для того, чтобы пользователям было проще создавать пароли, которые соответствуют определённым критериям. Генератор позволяет создавать пароли с использованием специальных символов, соответствующих заданной маске, а также предоставляет возможность сохранения сгенерированных паролей в удобном формате.

## 1. Базовая функциональность

- Генерация паролей заданной длины:  
  Пользователь может выбрать длину пароля от 8 до 32 символов (или больше, в зависимости от настроек).

- Разнообразие символов:  
  Программа поддерживает различные наборы символов, включая заглавные и строчные буквы, цифры и специальные символы такие как (@, *, $, %, и другие).

## 2. Уникальные и сложные дополнения

- Анализ надежности пароля:  
  Реализован алгоритм, который оценивает надежность сгенерированного пароля. Анализ учитывает длину пароля, разнообразие символов и частоту повторения символов.

## 3. Расширенные функции

- Генератор паролей по шаблону:  
  Пользователи могут задавать шаблон для пароля, например, "AA00$$", где "A" обозначает заглавную букву, "0" — цифру, а "$" — специальный символ.

- Выбор длины пароля:  
  Пользователь может задавать длину пароля в диапазоне от 8 до 32 символов с проверкой на корректность введённого значения.

- Интерактивные рекомендации:  
  Программа предоставляет пользователю обратную связь о надежности пароля и рекомендует улучшения, если пароль не соответствует стандартам безопасности.

- Экспорт паролей в CSV/JSON:  
  Реализована возможность экспорта базы паролей в форматы CSV и JSON для дальнейшего использования и анализа.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone [URL_REPOSITORY]
   cd password_generator
