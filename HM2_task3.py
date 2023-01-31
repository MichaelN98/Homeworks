# 3

casino_blacklist = ["Jack Pie", "Erik Man", "Lili Evans"]
poker_blacklist = ["Patrick Low", "Ann Downstown", "Mari Darret"]
alcohol_blacklist = ["Albert Second", "Kate Signi", "Iri Mane"]

for x in [casino_blacklist, alcohol_blacklist]:
    poker_blacklist.extend(x)

print(poker_blacklist)

# second option
# all_blacklists=(*casino_blacklist, *poker_blacklist, *alcohol_blacklist)
# print(all_blacklists)

# third option
# all_blacklists = casino_blacklist + poker_blacklist + alcohol_blacklist
# print(all_blacklists)

#  fourth option
# all_blacklists = [j for i in [poker_blacklist, casino_blacklist, alcohol_blacklist] for j in i]
# print(all_blacklists)
