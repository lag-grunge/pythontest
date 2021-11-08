
from functional_purse import add_ingot, get_ingot, empty

if __name__ == '__main__':
    purse = None
    purse = add_ingot(purse)
    print("1", purse)
    purse = empty()
    print(purse)
    purse["gold_ingots"] = 0
    print(purse)
    add_ingot(purse)
    print(purse)

    import random
    for i in range(10):
        purse = add_ingot(purse)
        if purse["gold_ingots"] == 5:
            for k in range(random.randint(1, 10)):
                purse = get_ingot(purse)
                print(purse)

    purse = add_ingot(get_ingot(add_ingot(empty(purse))))
    print(purse)
