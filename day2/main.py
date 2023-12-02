import functools
import operator
import pathlib


def reader(path: str | pathlib.Path) -> tuple[str, ...]:
    if isinstance(path, str):
        path = pathlib.Path(path)
    with pathlib.Path.open(path, "r") as f:
        return tuple(f)


def main():
    games = [
        line.strip().split(": ")[1].split("; ") for line in reader("part2.txt")
    ]
    summe = []
    for rounds in games:
        red = 0
        blue = 0
        green = 0
        for round in rounds:
            for values in round.split(", "):
                v, k = values.split()
                if k == "red" and red < int(v):
                    red = int(v)
                elif k == "green" and green < int(v):
                    green = int(v)
                elif k == "blue" and blue < int(v):
                    blue = int(v)
        summe.append(functools.reduce(operator.mul, (red, green, blue)))
    print(sum(summe))


if __name__ == "__main__":
    main()
