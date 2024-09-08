user1 = {"Target","Banana Republic","Old Navy"}
user2 = {"Banana Republic","Gap","Kohl's"}

def jaccard(user1, user2):
    stores_in_common = len(user1.intersection(user2))
    stores_all_together = len(user1.union(user2))
    
    return stores_in_common / float(stores_all_together)

print(jaccard(user1, user2))