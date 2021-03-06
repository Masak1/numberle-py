from sys import stdin
import urllib.parse

from numberle.numberle import Numberle


def get_color_squares(answer_check_list):
    color_squares = [None] * len(answer_check_list)
    for index, n in enumerate(answer_check_list):
        if n == 0:
            color_squares[index] = '⬛'
        elif n == 1:
            color_squares[index] = '🟩'
        elif n == 2:
            color_squares[index] = '🟨'
    return color_squares


def is_int(s):
    try:
        int(s, 10)
    except ValueError:
        return False
    return True


def main():
    print('Input number of answer\'s number of digits '
        + '(if input other chars means 5) : ', end='', flush=True)
    s = stdin.readline().rstrip()
    number_of_digits = 5 if not is_int(s) else int(s)
    numberle = Numberle(number_of_digits, False)
    print('Let\'s start the game!')

    color_squares_list = []

    while (True):
        print('Input ' + str(number_of_digits)
            + ' numbers you expect : ', end='', flush=True)
        expect_num = stdin.readline().rstrip()
        if not is_int(expect_num) or len(expect_num) != number_of_digits:
            continue

        numberle.check_number(expect_num)

        color_squares = ''.join(get_color_squares(numberle.answer_check_list))
        color_squares_list.append(color_squares)
        print(color_squares, flush=True)
        if color_squares.count('🟩') == number_of_digits:
            break

    print('Congratulations!\nAnswer number is ' + numberle.answer_num,
        flush=True)

    print('Your answers', flush=True)
    for squares in color_squares_list:
        print(squares, flush=True)
    
    tweet_text = 'https://twitter.com/intent/tweet?text='+ urllib.parse.quote(
        'Numberle\n\n'+ '\n'.join(color_squares_list))
    print('Tweet url : ' + tweet_text)


if __name__ == '__main__':
    main()
