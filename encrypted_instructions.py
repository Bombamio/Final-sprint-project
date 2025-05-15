"""A. Шифрованные инструкции. ID: 138383214."""


from string import digits


def instructions(data: str):
    """Расшифровывает краткие команды."""

    # Список кортежей, нужет для правильного преобразованиявложенных списков.
    stack: list[tuple[int, str]]
    stack = []
    # Кортежь чисел, нужен для приобразования элементов списка в формат int().
    NUMS = set(digits)
    num = ''    # Число, на которое множится строка.
    current_str = ''    # Строка, с которой функция будет работать.

    for elm in data:

        if elm in NUMS:
            # Ищем множитель для строки.
            num += elm

        elif elm == '[':
            # Добавляем в стэк множитель и прошлую строку
            # для коректной работы с вложенными списками.
            stack.append((int(num), current_str))
            num = ''
            current_str = ''

        elif elm == ']':
            # Раздляем последний элеменс стэка на составляющие для коректной
            # работы с вложенными списками.
            prev_num, prev_str = stack.pop()
            current_str = prev_str + current_str * prev_num

        else:
            # Заполнение текущей строки новыми элементами.
            current_str += elm

    return current_str


if __name__ == '__main__':
    data = input()
    print(instructions(data))
