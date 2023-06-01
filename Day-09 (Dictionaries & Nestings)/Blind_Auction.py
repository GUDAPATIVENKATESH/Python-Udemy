# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from Art import logo
print("Welcome to Blind Auction")
print(logo)
start_auction = False
Auction = {}
while not start_auction :    
    name = input("Enter the name of the bidder\n: ")
    bidding = int(input("Enter the bidding amount\n: "))
    bidders_remain = input("Are there any other bidders? Type 'yes' or 'no'\n: ").lower()
    Auction[name] = bidding
    if bidders_remain == "no" :
        start_auction = True
        intiate_auction()
    

def intiate_auction():
    for bidders in Auction :
        bid = Auction[bidders]
        print(bid)

    