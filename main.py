# This is a sample Python script.
from RightBracketSeq import RightBracketSeq

if __name__ == '__main__':
    r = ['()()())())((()))))((((',  # можно посчитать вручную - 4 изменения для преобразования в псп
         '(()())()())()()())((()',  # 2
         '(()())()())()()())((()))()()())(',  # неправильная посл
         '(()())()())()()())((()))()()())(x',  # есть симв, с непр вводом
         '((()())))(()())()()())((()))()()())(((((',
         '((()())))(()())()()())((()))()()())(((']  # 3
    test_bracket_seq = RightBracketSeq()
    for i in r:
        try:
            test_bracket_seq.seq = i
            print(test_bracket_seq)
        except AttributeError:
            print(f"Ошибка в введенных данных '{i}'\n")
