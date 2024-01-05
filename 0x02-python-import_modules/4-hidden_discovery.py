#!/usr/bin/python3.8

def print_names():
    import hidden_4 as code

    hidden_names = dir(code)
    for name in hidden_names:
        if not name.startswith('__'):
            print(name)


if __name__ == "__main__":
    print_names()
