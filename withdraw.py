'''
    Change Making Machine:
    Given an amount return the minimum of bills possible.

    Examples:
        withdraw(230): [1, 1, 4]
        withdraw(40): [0, 0, 2]
'''

bills = [100, 50, 20]


def withdraw(amount: int) -> list:
    bill_count = process_withdraw(amount)

    return list(bill_count.values())


def process_withdraw(amount: int) -> dict:
    bills_count_result = {bill: 0 for bill in bills}
    if amount in bills:
        bills_count_result[amount] = 1

    else:
        for bill in bills:
            ref_amount = amount - bill
            if bill <= ref_amount:
                bills_count_result = process_withdraw(ref_amount)
                bills_count_result[bill] = bills_count_result[bill] + 1
                break

    return bills_count_result


assert withdraw(230) == [1, 1, 4]
assert withdraw(40) == [0, 0, 2]
assert withdraw(60) == [0, 0, 3]
assert withdraw(210) == [1, 1, 3]
assert withdraw(280) == [1, 2, 4]
