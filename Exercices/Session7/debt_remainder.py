def give_money(borrowed_money, from_person: str, to_person: str, amount: float):
    if from_person == to_person or type(from_person) != str or type(to_person) != str or (type(amount) != int and type(amount) != float) or type(borrowed_money) != dict:
        raise ValueError
    borrowed_money.setdefault(from_person, {})
    borrowed_money.setdefault(to_person, {})

    borrowed_money[from_person][to_person] = borrowed_money[from_person].get(to_person, 0) - amount
    borrowed_money[to_person][from_person] = borrowed_money[to_person].get(from_person, 0) + amount
    return borrowed_money

def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict:
        raise ValueError
    total = 0
    for key in borrowed_money:
        for name in borrowed_money[key]:
            if borrowed_money[key][name] > 0:
                total += borrowed_money[key][name]
    return total

borrowed_money = {}
give_money(borrowed_money, "Mark", "Bill", 2000000)
give_money(borrowed_money, "Mark", "Steve", 2000000)
give_money(borrowed_money, "Serguei", "Bill", 5000000)
give_money(borrowed_money, "Bill", "Larry", 6000000)
give_money(borrowed_money, "Larry", "Linus", 5.5)
give_money(borrowed_money, "Steve", "Mark", 2000000)