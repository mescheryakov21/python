list_ishod = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_ishod)
a_long = len(list_ishod)
list_new = [list_ishod[irc] for irc in range(1, a_long) if list_ishod[irc] > list_ishod[irc-1]]
print(list_new)
