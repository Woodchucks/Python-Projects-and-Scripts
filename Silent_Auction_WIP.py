from replit import clear
from art import logo
print(logo)

next_bidder = True
bidder = {}
while next_bidder == True:
  clear()
  name = input("What's your name?")
  price = int(input("What's your price?"))
  next_person = input("Is there another person who would like to bet?")

  def add_bidder(name, price_auction):
    bidder[name] = price_auction
  
  add_bidder(name, price)

  if next_person.lower() == "no":
    next_bidder = False

max_price = 0
bidder_name = ''
for item in bidder:
  if max_price < bidder[item]:
    max_price = bidder[item]
    bidder_name = item
print(f"The winner is {bidder_name} with amount {max_price} PLN")
