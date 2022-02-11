import fire


def greet(greeting='Hej', name='Tomek'):
    print(f'{greeting} {name}')


def goodbye(goodbye='Żegnaj', name='Tomek'):
    print(f'{goodbye} {name}')


if __name__ == '__main__':
    fire.Fire()
