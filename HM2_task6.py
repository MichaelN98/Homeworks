import numpy as n
# 6 through numpy, I did not find another option
group = ["Jack Pie", "Erik Man", "Lili Evans", "Patrick Low", "Lili Evans", "Patrick Low"]
group = n.unique(group)
print(group)



# first try
# uniq_group = []
# for item in group:
#     if item not in uniq_group:
#         uniq_group.append(item)
# print(uniq_group)


