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
