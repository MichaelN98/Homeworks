# 3

casino_blacklist = ["Jack Pie", "Erik Man", "Lili Evans"]
poker_blacklist = ["Patrick Low", "Ann Downstown", "Mari Darret"]
alcohol_blacklist = ["Albert Second", "Kate Signi", "Iri Mane"]

casino_blacklist.extend(alcohol_blacklist)
casino_blacklist.extend(alcohol_blacklist)
print(casino_blacklist)

# second option
# all_blacklists = list
# all_blacklists=(*casino_blacklist, *poker_blacklist, *alcohol_blacklist)
# print(all_blacklists)

