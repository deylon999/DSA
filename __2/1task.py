from decimal import Decimal
from fractions import Fraction

prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

total_f = sum(prices)
discount_f = total_f * (1 - 0.07)
nds_f = discount_f * 1.2
part_f = nds_f / 3
print("float:", total_f, discount_f, nds_f, part_f)

prices_d = [Decimal(str(p)) for p in prices]
total_d = sum(prices_d)
discount_d = total_d * Decimal('0.93')
nds_d = discount_d * Decimal('1.2')
part_d = nds_d / Decimal('3')
print("decimal:", total_d, discount_d, nds_d, part_d)

prices_fr = [Fraction(str(p)) for p in prices]
total_fr = sum(prices_fr)
discount_fr = total_fr * Fraction(93, 100)
nds_fr = discount_fr * Fraction(120, 100)
part_fr = nds_fr / 3
print("fraction:", total_fr, discount_fr, nds_fr, part_fr)