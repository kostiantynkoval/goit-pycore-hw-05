from pathlib import Path
from sys import argv
from collections import Counter, defaultdict


def load_logs(file_path: str) -> list:
    with open(Path(file_path), 'r') as log:
        return log.readlines()


def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.strip().split()
    return {'date': date, 'time': time, 'level': level, 'message': ' '.join(message)}


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].casefold() == level.casefold(), logs))


def count_logs_by_level(logs: list) -> dict:
    count = defaultdict(int)
    for log in logs:
        count[log['level']] += 1
    return count


def display_log_counts(counts: dict) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level}{(17 - len(level)) * ' '}| {count}")


def display_filtered_logs(logs: list, level: str) -> None:
    if len(logs) > 0:
        print(f"Деталі логів для рівня '{level.upper()}':")
        for log in logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"Для рівня '{level.upper()}' логів не знайдено")


def main():
    try:

        logs_list = load_logs(argv[1])
        logs = [parse_log_line(log_line) for log_line in logs_list]
        display_log_counts(count_logs_by_level(logs))
        if len(argv) > 2:
            filtered = filter_logs_by_level(logs, argv[2])
            display_filtered_logs(filtered, argv[2])
    except IndexError:
        print('Введіть шлях до вашого файлу з логами')
    except FileNotFoundError:
        print('Введіть коректний шлях до вашого файлу з логами')


if __name__ == "__main__":
    main()
