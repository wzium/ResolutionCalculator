from typing import Tuple
from os import system


system("title ResolutionCalculator")


def get_resolution() -> Tuple[int, int]:
    while True:
        print("Enter the resolution (for example 1920x1080).")
        resolution: str = input(">>> ").lower()
        try:
            x_str, y_str = tuple(resolution.split("x"))
            return int(x_str), int(y_str)
        except ValueError:
            print("Enter a proper value!")


def get_ratio() -> Tuple[int, int]:
    while True:
        print("Enter the aspect ratio (for example 16:9).")
        ratio: str = input(">>> ").lower()
        try:
            x_ratio, y_ratio = tuple(ratio.split(":"))
            return int(x_ratio), int(y_ratio)
        except ValueError:
            print("Enter a proper value!")


def calculate(resolution: Tuple[int, int], ratio: Tuple[int, int]) -> Tuple[int, int]:
    x_res, y_res = resolution
    x_ratio, y_ratio = ratio
    x_multiplier: int = x_res // x_ratio
    y_multiplier: int = y_res // y_ratio
    multiplier: int = min(x_multiplier, y_multiplier)
    closest_x: int = multiplier*x_ratio
    closest_y: int = multiplier*y_ratio
    return closest_x, closest_y


def start():
    suggested_x, suggested_y = calculate(get_resolution(), get_ratio())
    result: str = f"{suggested_x}x{suggested_y}"
    print(f"The best resolution you can get from that picture is {result}")


start()

while True:
    print("Do you want to try again? (Y/N)")
    answer: str = input(">>> ").lower()
    if answer == "y":
        start()
    elif answer == "n":
        break
    else:
        print("Enter a proper value!")
