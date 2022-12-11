everyone = {}
loop_questions = False

def check_bids(bid_no):
    empty_value = 0

    #user_id gets imported from another file
    winner = ""
    for items in bid_no:
        if empty_value < everyone[items]:
            empty_value = everyone[items]
            winner = items
    
    #we will show bits on here with mapping
    print(f"{winner} won with the bid amount of ${empty_value}.")

while not loop_questions:
    name = input("Enter your name: ")
    bid = int(input("Enter your sum: $"))
    everyone[name] = bid
    again = input("Is there another person that wants to bid? 'Yes' or 'No': ").lower()

    #we can have optional answers on a list and iterate over them to compare as an additional functionality
    if again == "no":
        loop_questions = True
        check_bids(everyone)