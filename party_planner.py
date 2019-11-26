def party_planner(people, cookies):
    leftovers = None
    num_each = None
    
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e:
        print("ZeroDivisionError - {}".format(e))
        print("You entered 0 people. Please try with appropriate number of attendees.")

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    people = int(input("How many people are attending? "))
    cookies = int(input("How many cookies are you baking? "))
    
    cookies_each, leftovers = party_planner(people, cookies)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")