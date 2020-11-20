from business_rule_engine import RuleParser

from ..core import calculate_discount


def test_only_new_year():
    rules = """
    rule "new year"
    when
        products_in_stock > 10
    then
        calculate_discount(sum, 0.1)
    end

    rule "autumn"
    when
        sum > 1500
    then
        calculate_discount(sum, 0.05)
    end
    """

    params = {
        'sum': 1000,
        'products_in_stock': 20,
    }

    parser = RuleParser()
    parser.register_function(calculate_discount)
    parser.parsestr(rules)
    result = parser.execute(params)

    assert result == 900


def test_only_autumn():
    rules = """
    rule "autumn"
    when
        sum > 1500
    then
        calculate_discount(sum, 0.05)
    end
    
    rule "new year"
    when
        products_in_stock > 10
    then
        calculate_discount(sum, 0.1)
    end
    """

    params = {
        'sum': 2000,
        'products_in_stock': 20,
    }

    parser = RuleParser()
    parser.register_function(calculate_discount)
    parser.parsestr(rules)
    result = parser.execute(params)

    assert result == 1900


def test_not_autumn_and_new_year():
    rules = """
    rule "autumn"
    when
        sum > 1500
    then
        calculate_discount(sum, 0.05)
    end

    rule "new year"
    when
        products_in_stock > 10
    then
        calculate_discount(sum, 0.1)
    end
    """

    params = {
        'sum': 1000,
        'products_in_stock': 20,
    }

    parser = RuleParser()
    parser.register_function(calculate_discount)
    parser.parsestr(rules)
    result = parser.execute(params)

    assert result == 900
