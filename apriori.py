import pandas as pd
from apyori import apriori

df = pd.read_csv("C:\\Users\\beniv\\OneDrive\\שולחן העבודה\\big data final\\apriori_end.csv")
records = []
for i in range(1, 30):
    records.append([str(df.values[i, j]) for j in range(85,95)])
print(records)
association_rules = apriori(records, min_support=0.002, min_confidence=0.3, min_lift=3, min_length=2)
association_results = list(association_rules)
print("length:", len(association_results))
# the rules accordind to the result we get in length...
print(association_results[0])
print(association_results[1])
print(association_results[2])
print(association_results[3])

for item in association_results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")



