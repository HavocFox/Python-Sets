customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]


def remdupe(idlist):
    unique_ids = []
    print("Individual Unique IDs: ")
    for id in idlist:
        if id not in unique_ids:
            unique_ids.append(id)
            print(id)
        else:
            idlist.remove(id)
    return unique_ids

customer_ids = remdupe(customer_ids)
print("Complete set of unique IDs: ")
print(customer_ids)