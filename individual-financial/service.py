import ast

files = open("database.txt", "r")
contents = files.read()
transactions = ast.literal_eval(contents)
files.close()


def all_transaction():
    return [transactions[key] for key in sorted(transactions.keys())]


def one_transaction(ID="AE020330000000693123456"):
    trans = []
    for sub in transactions.values():
        if sub["identifier"] == ID:
            trans.append(sub)
    return trans


def one_transaction_by_category(ID="AE020330000000693123456", category="Credit Card"):
    trans = []
    for sub in transactions.values():
        if sub["identifier"] == ID and sub["category"] == category:
            trans.append(sub)
    return trans


def financial_balance_monthly(ID="AE020330000000693123456"):
    trans = []
    cur = {}
    for sub in transactions.values():
        if sub["identifier"] == ID:
            tag = "-".join([sub["transactionTime"], sub["currency"], sub["direction"]])
            if tag not in cur.keys():
                cur[tag] = float(sub["amount"])
            else:
                cur[tag] += float(sub["amount"])
    for item in cur:
        trans.append({"transactionTime": item.split("-")[0],
                      "currency": item.split("-")[1],
                      "direction": item.split("-")[2],
                      "amount": cur[item]})
    return trans


def financial_balance_unq_month(ID="AE020330000000693123456", transactionTime="202009"):
    subset = financial_balance_monthly(ID=ID)
    trans = []
    for sub in subset:
        if sub["transactionTime"] == transactionTime:
            trans.append(sub)
    return trans


def one_transaction_for_salary(ID="AE020330000000693123456"):
    trans = []
    cur = {}
    for sub in transactions.values():
        if sub["identifier"] == ID and sub["category"] == "Salary" and sub["direction"] == "Credit":
            if sub["transactionTime"] not in cur.keys():
                cur[sub["transactionTime"]] = {"amount": float(sub["amount"]),
                                               "num_of_event": 1}
            else:
                cur[sub["transactionTime"]]["amount"] += float(sub["amount"])
                cur[sub["transactionTime"]]["num_of_event"] += 1
    for item in cur:
        trans.append({"transactionTime": item,
                      "amount": cur[item]["amount"],
                      "num_of_transaction": cur[item]["num_of_event"]})
    return trans


