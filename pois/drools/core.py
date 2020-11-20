def calculate_discount(sum, percent):
    sum_percents = sum * percent
    sum_final = sum - sum_percents

    print(f"Your discount: {sum_percents}")
    print(f"Your have to pay: {sum_final}")

    return sum_final
