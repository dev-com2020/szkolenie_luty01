import argparse


def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)


def sail():
    ship_name = 'Twoja żaglówka'
    print(f"{ship_name} stawia żagle")


def list_ships():
    ships = ['Statek1', 'Statek2', 'Statek3']
    print(f"Żaglówki: {','.join(ships)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Żaglówki')

    parser.add_argument('--twice', '-t', help='Zrób dwukrtonie', action='store_true')

    subparsers = parser.add_subparsers(dest='func')
    ship_parser = subparsers.add_parser('ships', help='Komendy związane z żaglówkami')
    ship_parser.add_argument('command', choices=['list', 'sail'])

    sailor_parser = subparsers.add_parser('sailor', help="Komendy związane z żeglarzami")
    sailor_parser.add_argument('name', help="Imię żeglarza")
    sailor_parser.add_argument('--greeting', '-g', help="Pozdrowienie", default='Ahoj')

    args = parser.parse_args()

    if args.func == 'sailor':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()
