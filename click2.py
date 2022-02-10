import click


@click.group()
def cli():
    pass

@click.group(help='Komendy o żaglówkach')
def ships():
    pass
cli.add_command(ships)

@ships.command(help='Żeglowanie...')
def sail():
    ship_name = 'Twoja żaglówka'
    print(f"{ship_name} stawia żagle")

@ships.command(help='Lista statków')
def list_ships():
    ships = ['Statek1', 'Statek2', 'Statek3']
    print(f"Żaglówki: {','.join(ships)}")

@cli.command(help='Komendy o żeglarzach')
@click.option('--greeting',default='Ahoj',help='Pozdrowienie...')
@click.argument('name')


def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli()
