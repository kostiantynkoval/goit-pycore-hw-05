from re import finditer

def generator_numbers(text):
    for match in finditer(r" \d+\.\d+ | \d+ ", text):
        yield float(match.group())

def sum_profit(text, generator_function):
    return sum(generator_function(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 та 324.00 доларів."
text1 = "Пункт 28а: Загальний дохід працівника складається з декількох частин: 1000 як основний дохід, доповнений додатковими надходженнями 27.45555555555555555 та 324.000000000000001 доларів."
total_income = sum_profit(text1, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")