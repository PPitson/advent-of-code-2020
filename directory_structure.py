import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-day", type=int, default=1, help="from which day the structure should be created")
    parser.add_argument("--end-day", type=int, default=25, help="to which day the structure should be created")
    return parser.parse_args()


def create_directory_structure(start_day: int, end_day: int) -> None:
    directory_names = (f"day{day}" for day in range(start_day, end_day + 1))
    for directory_name in directory_names:
        _create_directory_and_files(directory_name)


def _create_directory_and_files(directory_name: str) -> None:
    _create_directory(directory_name)
    _create_file(f"{directory_name}/__init__.py")
    _create_file(f"{directory_name}/description.md")
    _create_file(f"{directory_name}/solution.py")
    _create_file(f"{directory_name}/test_solution.py")
    _create_directory(f"{directory_name}/data")
    _create_file(f"{directory_name}/data/input.txt")
    _create_file(f"{directory_name}/data/test_input.txt")


def _create_directory(directory_name: str) -> None:
    Path(directory_name).mkdir(exist_ok=True)


def _create_file(path: str) -> None:
    Path(path).touch(exist_ok=True)


if __name__ == "__main__":
    args = parse_args()
    create_directory_structure(args.start_day, args.end_day)
