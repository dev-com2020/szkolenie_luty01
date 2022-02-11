import logging
import pyautogui

def multi(a, b):
    '''
    Mnożenie dwóch liczb całkowitych

    :raises TypeError - w przypadku, gdy parametry nie będą liczbami.
    '''
    try:
        print(int(a) * int(b))
    except TypeError:
        logging.warning('Niedozwolona operacja')
    except ValueError:
        logging.warning('Niedozwolona operacja 2')


# multi("None", "3")

data = [{'name': 'Jan', 'age': 'age'},
        {'name': 'Dawid', 'age': '25'},
        {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print('Niepoprawne dane: {}'.format(user))
        except ValueError:
            # print('Niepoprawny wiek: {}'.format(user))
            pyautogui.alert('Niepoprawny wiek: {}'.format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("{}. {}".format(i, user))
    return count


print(check_age(data, 25))
