"""A. Шифрованные инструкции. ID: 138355917."""


def instructions(data: str):
    """Расшифровывает краткие команды."""

    # Список кортежей, нужет для правильного преобразованиявложенных списков.
    stack = []
    # Кортежь чисел, нужен для приобразования элементов списка в формат int().
    nums_examples = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    num = ''    # Число, на которое множится строка.
    current_str = ''    # Строка, с которой функция будет работать.

    for elm in data:

        if elm in nums_examples:
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
