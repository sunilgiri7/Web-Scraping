current_year = 2023
def main(*args):
    for arg in args:
        print(f'total age fro {arg} is {current_year - arg}')

# main(1999, 1987, 2002)

def base(**qwargs):
    for index, item in qwargs.items():
        print(f"the params are {index} and item are {item}")

base(name = 'Sunil', age=21)