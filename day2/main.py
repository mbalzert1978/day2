from collections import defaultdict
import pathlib
import functools

def reader(path: str | pathlib.Path) -> tuple[str, ...]:
    if isinstance(path, str):
        path = pathlib.Path(path)
    with pathlib.Path.open(path, "r") as f:
        return tuple(f)



def main():
    part1 = reader("part1.txt")
    part2 = reader("part2.txt")
    test = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    min_values = defaultdict(list)
    games = {
        x.replace("Game", "")
        .strip()
        .split(": ")[0]: x.replace("Game", "")
        .strip()
        .split(": ")[1]
        .split("; ")
        for x in part2
    }
    summe = list()
    for idx, rounds in games.items():
        for round in rounds:
            for values in round.split(", "):
                v, k = values.split()
                min_values[k].append(int(v))
        summe.append(functools.reduce(lambda x, y: x * y, (max(value) for value in  min_values.values())))
        min_values.clear()
    summe = sum(summe)
    print(summe)


if __name__ == "__main__":
    main()
