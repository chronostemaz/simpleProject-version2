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
            else:
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
        self._seq = value
        self._is_cbs = self.is_valid()
        self._amount_moves_to_cbs = self.moves_required()

    def is_valid(self):
        """
        Проверяет, является ли последовательность ПСП.

        Возвращает:
        True, если последовательность является ПСП, иначе False.
        """
        self._balance_mask = list(self._calc_balance_brackets(self._seq))
        return self._balance_mask[-1] == 0

    def moves_required(self):
        """
        Возвращает количество ходов, необходимых для преобразования в ПСП.

        Возвращает:
        Количество ходов, необходимых для преобразования в ПСП.
        """
        if self._is_cbs:
            return abs(min(self._balance_mask, default=0))
        else:
            return 0

    def __repr__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f'Последовательность "{self.seq}"\n' \
               f'Маска {self._balance_mask}\n' \
               f'Возможность ПСП? {"да" if self._is_cbs else "нет"}\n' \
               f'Ходов для изменения в ПСП {self._amount_moves_to_cbs}\n' if self._is_cbs else ''
