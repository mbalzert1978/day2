import pathlib


def reader(path: str | pathlib.Path) -> tuple[str, ...]:
    if isinstance(path, str):
        path = pathlib.Path(path)
    with pathlib.Path.open(path, "r") as f:
        return tuple(f)


def main():
    part1 = reader("part1.txt")
    max_values = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    games = {
        x.replace("Game", "")
        .strip()
        .split(": ")[0]: x.replace("Game", "")
        .strip()
        .split(": ")[1]
        .split("; ")
        for x in part1
    }
    summe = set()
    for idx, rounds in games.items():
        invalid = False
        for round in rounds:
            for values in round.split(", "):
                v, k = values.split()
                if int(v) <= max_values[k]:
                    continue
                else:
                    invalid = True
        if not invalid:
            summe.add(int(idx))

    summe = sum(summe)
    print(summe)


if __name__ == "__main__":
    main()
