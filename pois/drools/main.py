"""
Описать бизнес-правила для онлайн покупки на условиях лояльности клиента
(рассчитать стоимость покупки с учетом скидки в зависимости от условий)

Реализовано два сценария скидок:
- new year
- autumn

Метод execute изменен таким образом, чтобы возвращал результат выполнения (return rvalue_action)
"""

from business_rule_engine import RuleParser

from rules import rules
from core import calculate_discount


if __name__ == "__main__":
    params = {
        'sum': float(input("Введите полную сумму заказа: ")),
        'products_in_stock': int(input("Введите количество товара в заказе: ")),
    }

    parser = RuleParser()
    parser.register_function(calculate_discount)
    parser.parsestr(rules)
    result = parser.execute(params)

    print(result)
