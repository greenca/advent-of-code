import json

with open('day12_input.txt') as f:
    account = json.loads(f.read())

def sumAccount(account):
    total = 0
    if type(account) == dict:
        if 'red' not in account.values():
            for k in account.keys():
                total += sumAccount(account[k])
    elif type(account) == list:
        for a in account:
            total += sumAccount(a)
    elif type(account) == int:
        total += account
    return total

print sumAccount(account)
