import os
import sys


# print(sys.byteorder)
# print(sys.getsizeof(1))
# print(sys.platform)

# if sys.version_info.major < 3:
#     print("Twoja wersja Python to 2.xx, do widzenia!")
# elif sys.version_info.minor < 7:
#     print("Dokonaj aktualizacji swojego Pythona...")
# else:
#     print("Wszystko ok!")
#
# print(os.getcwd())
# os.chdir('output')
# print(os.getcwd())
# os.environ.get('LOGLEVEL')
# os.environ['LOGLEVEL'] = 'DEBUG'
# print(os.environ.get('LOGLEVEL'))
# print(os.getlogin())

def say_it(greeting,target):
    message = f'{greeting}{target}'
    print(message)

if __name__ == '__main__':
    greeting = 'Witaj '
    target = 'Tomek'


    if '--help' in sys.argv:
        help_message = f"Sposób użycia: '{sys.argv[0]}' --name<IMIĘ> --greeting<POWITANIE>"
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        name_index = sys.argv.index('--name') + 1

        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        greeting_index = sys.argv.index('--greeting') + 1

        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    # say_it(greeting,name)




# print(f"Pierwszy argument: '{sys.argv[0]}'")
# print(f"Pierwszy argument: '{sys.argv[1]}'")
# print(f"Pierwszy argument: '{sys.argv[2]}'")
# print(f"Pierwszy argument: '{sys.argv[3]}'")