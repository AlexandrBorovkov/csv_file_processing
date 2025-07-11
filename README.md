## Тестовое задание ##
### Обработка csv файла ###

## Как установить и запустить приложение? ##
1. **Клонирование репозитория**:
    ```sh
    git clone https://github.com/AlexandrBorovkov/csv_file_processing.git
   ```
    или
    ```sh
    git clone git@github.com:AlexandrBorovkov/csv_file_processing.git
    ```
2. **Установка зависимостей**:
    - Установить uv:
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
    ```
    ```sh
    make install
    ```
3. **Варианты запуска приложения**:
    ```sh
    uv run csv-process products.csv --where "price<=500"
    ```
    ```sh
    uv run csv-process products.csv --aggregate "rating=max"
    ```
    ```sh
    uv run csv-process products.csv --where "brand=apple" --aggregate "rating=max"
    ```

4. **Выполнить проверки**:
    ```sh
    make lint
    ```
    ```sh
    make test
    ```
    ```sh
    make test-coverage
    ```

## Что нужно сделать? ##

Нужно написать скрипт для обработки CSV-файла, поддерживающий операции: 
- фильтрацию с операторами «больше», «меньше» и «равно»
- агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения

Собираем прототип, поэтому всё по простому. Фильтрацию и агрегацию делаем по одной любой колонке. Делать фильтрации с составными условия, например с and или or, а также по нескольким колонкам одновременно не нужно. Фильтрация поддерживает любые колонки, то есть с текстовыми и числовыми значениями, а агрегация только числовые. Гарантируется что входные файлы валидны, например если в колонке числа, то там все значения числа. Чтобы сфокусироваться на функционале и не отвлекаться на рутинные задачи (обработка аргументов скрипта, чтение файла и форматированный вывод), можно использовать стандартную библиотеку argparse и csv, а для красивого отображения в консоли установить библиотеку tabulate.
Пример файла csv:
```
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
``` 
Для фильтрации используем where, для агрегации aggregate, значение передаются как “column=value”. Не меняем интерфейс скрипта, например не разбиваем параметр aggregate на два параметра aggregate-column и aggregate-value. 

### Какие функциональные требования? ###
- можно передать путь к файлу
- можно указать условие фильтрации
- можно указать условие агрегации
- в консоль выводится таблица с результатами выборки или агрегации
### Какие не функциональные требования? ###
- для всего кроме тестов и красивого вывода в консоль, можно использовать только стандартную библиотеку, например:
  - для работы с параметрами скрипта нельзя использовать click, но можно использовать argparse
  - для чтения файлов нельзя использовать pandas, но можно использовать csv
- код покрыт тестами написанных на pytest
- для тестов можно использовать любые дополнительные библиотеки
- код соответствует:
  - общепринятым стандартам написания проектов на python
  - общепринятому стилю 
