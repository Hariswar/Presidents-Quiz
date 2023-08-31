import random

presidents = [
    ("George Washington", "None"),
    ("John Adams", "Federalist"),
    ("Thomas Jefferson", "Democrat-Republican"),
    ("James Madison", "Democrat-Republican"),
    ("James Monroe", "Democrat-Republican"),
    ("John Quincy Adams", "Democrat-Republican"),
    ("Andrew Jackson", "Democrat"),
    ("Martin Van Buren", "Democrat"),
    ("William Harrison", "Whig"),
    ("John Tyler", "Whig"),
    ("James Polk", "Democrat"),
    ("Zachary Taylor", "Whig"),
    ("Millard Fillmore", "Whig"),
    ("Franklin Pierce", "Democrat"),
    ("James Buchanan", "Democrat"),
    ("Abraham Lincoln", "Republican"),
    ("Andrew Johnson", "Democrat"),
    ("Ulysses Grant", "Republican"),
    ("Rutherford Hayes", "Republican"),
    ("James Garfield", "Republican"),
    ("Chester Arthur", "Republican"),
    ("Grover Cleveland", "Democrat"),
    ("Benjamin Harrison", "Republican"),
    ("Grover Cleveland", "Democrat"),
    ("William McKinley", "Republican"),
    ("Theodore Roosevelt", "Republican"),
    ("William Taft", "Republican"),
    ("Woodrow Wilson", "Democrat"),
    ("Warren Harding", "Republican"),
    ("Calvin Coolidge", "Republican"),
    ("Herbert Hoover", "Republican"),
    ("Franklin Roosevelt", "Democrat"),
    ("Harry Truman", "Democrat"),
    ("Dwight Eisenhower", "Republican"),
    ("John Kennedy", "Democrat"),
    ("Lyndon Johnson", "Democrat"),
    ("Richard Nixon", "Republican"),
    ("Gerald Ford", "Republican"),
    ("Jimmy Carter", "Democrat"),
    ("Ronald Reagan", "Republican"),
    ("George H W Bush", "Republican"),
    ("Bill Clinton", "Democrat"),
    ("George W Bush", "Republican"),
    ("Barack Obama", "Democrat"),
    ("Donald Trump", "Republican"),
    ("Joe Biden", "Democrat")
]

min_president = int(input("Enter the min president number: "))
max_president = int(input("Enter the max president number: "))
mode = input("Enter '1' to guess the president, '2' to guess the party: ")
replit.clear()

while True:
    num = random.randint(min_president, max_president)
    president_name, party = presidents[num - 1]
    if mode.lower() == '1':
        guess = input(f"Who was president number {num}? ")
        if guess.lower() == president_name.lower():
            print("Correct!")
        else:
            print(f"Sorry, the correct answer was {president_name}.")
    else:
        guess = input(f"What was the political party of {president_name}? ")
        if guess.lower() == party.lower():
            print("Correct!")
        else:
            print(f"Sorry, the correct answer was {party}.")

    input("Press enter to generate a new president.")
    replit.clear()