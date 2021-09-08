from replit import clear
#call clear() to clear the output in the console.
from art import logo
print(logo)

next_bidder = True
bidders = []
bidder = {}
while next_bidder == True:
  name = input("What's your name?")
  price = input("What's your price?")
  next_person = input("Is there another person who would like to bet?")

  def add_bidder(name, price_auction):
    bidder[name] = price_auction
    bidders.append(bidder)
  
  add_bidder(name, price)

  if next_person.lower() == "no":
    next_bidder = False

# max_price = 0
# for item in bidders:
#   if bidders[item][0] > bidders[item+1][0]:
#     max_price = bidders[item][0]
#   else:
#     max_price = bidders[item + 1][0]
# print(bidders[1])
