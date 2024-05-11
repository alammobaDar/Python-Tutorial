# map funtion

Auction =[("Deion", 187000),
          ("Jamar", 205000),
          ("Zhair", 168000),
          ("Jaden", 197000),
          ("Ethan", 700000)]

to_euros = lambda value: (value[0], value[1]*0.016)
to_dollars = lambda value: (value[0], value[1]*0.017)
to_yen = lambda value: (value[0], value[1]*2.71)
to_won = lambda value: (value[0], value[1]*23.82)

auction_slaves = list(map(to_won, Auction))

value = lambda values: values[1]
sorted_slaves = sorted(auction_slaves, key= value, reverse= True)


for i in sorted_slaves:
    print(i)

