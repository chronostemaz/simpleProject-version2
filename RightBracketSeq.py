class RightBracketSeq:
    """
    Класс RightBracketSeq представляет собой анализатор последовательностей скобок.

    Атрибуты:
    - is_cbs (bool): Флаг, указывающий, является ли последовательность правильной последовательностью скобок (ПСП).
    - seq (str): Последовательность скобок для анализа.
    - amount_moves_to_cbs (int): Количество ходов, необходимых для преобразования последовательности в ПСП.
    - balance_mask ([int]): Маска баланса скобок.

    Методы:
    - __init__(self, seq_to_analyze: str = ''): Конструктор класса. Инициализирует атрибуты объекта.
    - is_valid(self): Проверяет, является ли последовательность ПСП.
    - moves_required(self): Возвращает количество ходов, необходимых для преобразования в ПСП.
    - __repr__(self): Возвращает строковое представление объекта.

    Пример использования:
    seq_instance = RightBracketSeq()
    seq_instance.seq = '(()()()())'
    print(seq_instance)
    """

    def __init__(self, seq_to_analyze: str = ''):
        """
        Конструктор класса RightBracketSeq.

        Параметры:
        - seq_to_analyze (str): Последовательность скобок для анализа (по умолчанию - пустая строка).
        """
        self._balance_mask = None
        self.seq = seq_to_analyze

    @staticmethod
    def _calc_balance_brackets(seq_to_analyze: str, balance=0):
        """
        Внутренний статический метод для вычисления маски баланса скобок.

        Параметры:
        - seq_to_analyze (str): Последовательность скобок для анализа.
        - balance (int): Текущий баланс скобок.

        Возвращает:
        Генератор, возвращающий значения баланса скобок на каждом шаге.
        """
        for char in seq_to_analyze:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            elif char != "":
                raise AttributeError()
            yield balance

    @property
    def seq(self):
        """
        Геттер для атрибута seq.
        Возвращает:
        Последовательность скобок для анализа.
        """
        return self._seq

    @seq.setter
    def seq(self, value: str):
        """
        Сеттер для атрибута seq.

        Параметры:
        - value (str): Последовательность скобок для анализа.
        """
        if value != '':
            self._seq = value
            self._balance_mask = [_ for _ in self._calc_balance_brackets(value)]
            self._is_cbs = self.is_cbs(value)
            self._amount_moves_to_cbs = self.need_to_move(value)

    def is_cbs(self, lisp_reference: str):
        """
        Проверяет, является ли последовательность ПСП.

        Возвращает:
        True, если последовательность является ПСП, иначе False.
        """
        return list(self._balance_mask)[-1] == 0

    def need_to_move(self, lisp_reference: str):
        """
        Возвращает количество ходов, необходимых для преобразования в ПСП.

        Возвращает:
        Количество ходов, необходимых для преобразования в ПСП.
        """
        return abs(min(self._balance_mask, default=0))

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f'Последовательность "{self.seq}"\n' \
               f'Маска {self._balance_mask}\n' \
               f'Возможность ПСП? {"да" if self._is_cbs else "нет"}\n' \
               f'{f"Ходов для изменения в ПСП {self._amount_moves_to_cbs}" if self._is_cbs else ""}\n'
