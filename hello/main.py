import sys


def hello(world):
    return f'Hello {world}!'


def main():
    try:
        world, *_ = sys.argv[1:]
    except ValueError:
        world = 'World'
    print(hello(world))


if __name__ == '__main__':
    main()
