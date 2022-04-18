import random
mark = 0
complexity = 0
test_first = 0

while test_first != 1:
    try:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        complexity_input = int(input())
        if complexity_input == 1:
            test_first += 1
            complexity = 1
            for i in range(1, 6):
                a = random.randint(2, 9)
                b = random.randint(2, 9)
                c = random.choice('-+*')
                result = 0

                if c == '+':
                    result = a + b
                    print(a, c, b)
                elif c == '-':
                    result = a - b
                    print(a, c, b)
                elif c == '*':
                    result = a * b
                    print(a, c, b)

                testing = 0

                while testing != 1:
                    try:
                        user_test = int(input())
                        if user_test == result:
                            print('Right!')
                            mark += 1
                            testing += 1
                        else:
                            print('Wrong!')
                            testing += 1
                    except ValueError:
                        print('Incorrect format.')

        elif complexity_input == 2:
            test_first += 1
            complexity = 2
            for i in range(1, 6):
                a = random.randint(11, 29)
                result = a ** 2
                print(a)

                testing = 0

                while testing != 1:
                    try:
                        user_test = int(input())
                        if user_test == result:
                            print('Right!')
                            mark += 1
                            testing += 1
                        else:
                            print('Wrong!')
                            testing += 1
                    except ValueError:
                        print('Incorrect format.')
        else:
            print('Incorrect format.')

    except ValueError:
        print('Incorrect format.')

print(f'Your mark is {mark}/5.')

print('Would you like to save your result to the file? Enter yes or no.')

answer = input()
mark_str = str(mark)

if answer == 'yes' or answer == 'YES' or answer == 'y' or answer == 'Yes':
    print('What is your name?')
    name = input()
    if complexity == 1:
        result_print = f'{name}: {mark}/5 in level 1 (simple operations with numbers 2-9).'
    else:
        result_print = f'{name}: {mark}/5 in level 2 (integral squares of 11-29).'
    file_result = open('results.txt', 'a', encoding='utf-8')
    file_result.write(result_print)
    file_result.close()
    print('The results are saved in "results.txt".')
else:
    pass
