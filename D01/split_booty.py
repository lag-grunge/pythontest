#!/bin/python3

#for typing.Dict
import typing
#for function empty, add_ingot, get_ingot
import functional_purse
#for random if booty not divided by 3
import random

#using Arbitrary Arguments, *args for receive any number
#of purses, check for negatives

# summing all split_ingots
# then dividing them into equal 3 parts
# dividing mod randomly part if it exists 
# creating tuple of 3 dicts with respective values of list

#def split_booty(*booty):
#    assert all(map(lambda x: type(x["gold_ingots"]) == int and x["gold_ingots"] >= 0, list(filter(lambda x: "gold_ingots" in x.keys(), booty)))), "One of booty gold_ingots is negative or non-integer!"
#    #sum all gold_ingots
#    split_ingots = sum([x["gold_ingots"] for x in list(filter(lambda x: "gold_ingots" in x.keys(), booty))])
#    # sum is divided by 3 eq parts
#    res = [split_ingots // 3 for i in range(3)]
#    # if mod not zero do random choice
#    if split_ingots % 3:
#        lucky = random.randint(0, 2)
#        if split_ingots % 3 == 1:
#            l = map(lambda x: int(x == lucky), range(3))
#        else:
#            l = map(lambda x: int(x != lucky), range(3))
#        res = [x + y for x, y in zip(l, res)]
#    return tuple([dict({"gold_ingots" : x}) for x in res])

# Work with every purse of booty
# Get ingots from purse while it has ingots
# Every ingot is given to current of 3 men, then to next
# more accurately who will get ingot depend on the number of ingot
# we consider
# Total amount of ingots on this moment (or number of current ingots) is counted in split_ingots



def split_booty(*booty: typing.Dict[str, int]):
    def correct_input(*booty: typing.Dict[str, int]):
        def correct_ingot(x: typing.Dict[str, int]):
            return type(x["gold_ingots"]) == int and x["gold_ingots"] >= 0
        item_ingots = list(filter(lambda x: "gold_ingots" in x.keys(), booty))
        Error_message = "One of booty gold_ingots is negative or non-integer!"
        assert all(map(correct_ingot, item_ingots)), Error_message

    correct_input(*booty)
    Bert = functional_purse.empty()
    Tom = functional_purse.empty()
    Will = functional_purse.empty()
    res = (Bert, Tom, Will)
    split_ingots = 0
    for purse in booty:
        if not "gold_ingots" in purse.keys():
            continue
        while purse["gold_ingots"] > 0:
            purse = functional_purse.get_ingot(purse)
            cur_purse = res[split_ingots % len(res)]
            cur_purse = functional_purse.add_ingot(cur_purse)
            split_ingots += 1
    return res

#test_cases
if __name__ == "__main__":
    print(split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}))
    print(split_booty({"gold_ingots":2}, {"gold_ingots":2}, {"apples":2}))
    print(split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}))
    print(split_booty({"gold_ingots":201}, {"gold_ingots":21}, {"apples":203}))
    #error case split_ingot
    print(split_booty({"gold_ingots": "srhydsfxh"}, {"gold_ingots":21}, {"apples":203}))
