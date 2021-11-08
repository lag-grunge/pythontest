import typing
from alarm import SQUEAK

@SQUEAK
def empty(purse: typing.Dict[str, int] = None):
    return dict({})

@SQUEAK
def add_ingot(purse: typing.Dict[str, int] = None):
#    if purse == None:
#        return dict({"gold_ingots" : 1})   
#    elif "gold_ingots" in purse.keys():
#        purse["gold_ingots"] += 1;
#    else:
#        purse["gold_ingots"] = 1;
#    return purse
    if purse is None:
        purse = empty()
    purse.update({"gold_ingots" : purse.get("gold_ingots", 0) + 1})
    print("Add an ingot!")
    return purse

@SQUEAK
def get_ingot(purse: typing.Dict[str, int] = None):
    # if purse is None:
    #     purse = empty(purse)
    # elif "gold_ingots" in purse.keys():
    #     if purse["gold_ingots"] <= 0:
    #         return purse
    #     purse["gold_ingots"] -= 1
    # return purse
    if purse is None:
        purse = empty()
    val = purse.get("gold_ingots", 0)
    if val:
        print('Get a ingot!')
        val -= 1
    else:
        print('There are no any ingots!')
    purse.update({"gold_ingots":  val})
    return purse