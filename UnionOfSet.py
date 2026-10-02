set1 = {"A","B","C","D","E"}
set2 = {"B","D","V","X","Y","Z"}
union = set1.union(set2)
total_guests = list(union)
print("Total no. of guests invited to the party:",len(total_guests)) 
print("Guest List:",total_guests)
intersection = set1.intersection(set2)
budget_total_guests = list(intersection)
print("Total guests invited in a budget:",len(budget_total_guests))
print("Budget Guest List:",budget_total_guests)