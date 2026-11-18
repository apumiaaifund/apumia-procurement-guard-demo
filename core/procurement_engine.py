from decimal import Decimal, ROUND_HALF_UP

Q2 = Decimal('0.01')
Q4 = Decimal('0.0001')

def r2(val):
    return Decimal(str(val)).quantize(Q2, rounding=ROUND_HALF_UP)

def audit_line(spec_p, spec_u, inv_p, inv_u, qty, rate_y):
    sp = Decimal(str(spec_p))
    su = Decimal(str(spec_u))
    ip = Decimal(str(inv_p))
    iu = Decimal(str(inv_u))
    q = Decimal(str(qty))
    r = Decimal(str(rate_y)) / Decimal('100')
    unit_spec = (sp / su).quantize(Q4, rounding=ROUND_HALF_UP)
    unit_inv = (ip / iu).quantize(Q4, rounding=ROUND_HALF_UP)
    creep_u = max(Decimal('0'), unit_inv - unit_spec)
    leak_rub = r2(creep_u * iu * q)
    cap_cost = r2(ip * q * r * Decimal('14') / Decimal('365'))
    return {
        'unit_spec': str(unit_spec),
        'unit_inv': str(unit_inv),
        'leak_rub': str(leak_rub),
        'cap_cost': str(cap_cost),
        'total_loss': str(r2(leak_rub + cap_cost)),
    }
