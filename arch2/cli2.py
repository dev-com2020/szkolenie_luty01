import click


@click.command()
@click.option('--greeting', default='Hej', help='Jak chcesz pozdrowić?')
@click.option('--name', default='Tomek', help='Kogo chcesz pozdrowić?')
def greet(greeting, name):
    print(f'{greeting} {name}')


if __name__ == '__main__':
    greet()
