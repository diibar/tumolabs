def get_number(prompt):
    while True:
        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number!")


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty!")

def Template1():
  number = get_number("Input a number: ")
  number2 = get_number("Input a number again: ")
  time_measure = get_text("Measure of time: ")
  transport = get_text("Mode of transportation: ")
  adjective = get_text("Input an adjective: ")
  adjective2 = get_text("Input an adjective again: ")
  adjective3 = get_text("Input an adjective again: ")
  color = get_text("Input a color: ")
  body_part = get_text("Input a part of the body: ")
  body_part2 = get_text("Input a part of the body again: ")
  verb = get_text("Input a verb: ")
  noun = get_text("Input a noun: ")
  noun2 = get_text("Input a noun again: ")
  noun3 = get_text("Input a noun again: ")
  noun4 = get_text("Input a noun again: ")
  silly_word = get_text("Input a silly word: ")

  print(f'''It was about {number} {time_measure} ago when I arrived at the hospital in a {transport}.
  The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun}s here.
  There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first.
  I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}.
  I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun} !''')

def Template2():
  person_name = get_text("Input a person's name: ")
  noun = get_text("Input a noun: ")
  noun2 = get_text("Input a noun again: ")
  adjective_feeling = get_text("Input an adjective (feeling): ")
  adjective_feeling2 = get_text("Input an adjective (feeling) again: ")
  verb = get_text("Input a verb: ")
  verb2 = get_text("Input a verb again: ")
  animal = get_text("Input an animal: ")
  color = get_text("Input a color: ")
  verb_ing = get_text("Input a verb + ing: ")
  adverb_ly = get_text("Input an adverb + ly: ")
  number = get_number("Input a number: ")
  time_measure = get_text("Measure of time: ")
  silly_word = get_text("Input a silly word: ")

  print(f'''This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun}.
  I am so {adjective_feeling} to {verb} in a tent. I am {adjective_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous.
  While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}.
  Then we will {adverb_ly} hike through the forest for {number} {time_measure}.
  If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!! ''')

def Template3():
  person_name = get_text("Input a person's name: ")
  color = get_text("Input color: ")
  animal = get_text("Input an animal: ")
  place = get_text("Input a place: ")
  adjective = get_text("Input an adjective: ")
  adjective2 = get_text("Input an adjective again: ")
  adjective3 = get_text("Input an adjective again: ")
  adjective4 = get_text("Input an adjective again: ")
  adjective5 = get_text("Input an adjective again: ")
  magical_creatures = get_text("Input magical creatures: ")
  magical_creatures2 = get_text("Input magical creatures again: ")
  room_in_house = get_text("Input room in a house: ")
  noun = get_text("Input a noun: ")
  noun2 = get_text("Input a noun again: ")
  noun3 = get_text("Input a noun again: ")
  nouns_plural = get_text("Input nouns: ")
  nouns_plural2 = get_text("Input nouns: ")
  number = get_number("Input a number: ")
  time_measure = get_text("Measure of time: ")
  verb_ing = get_text("Input verb + ing: ")

  print(f'''Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest.
  I found myself here one day after going for a ride on a {color} {animal} in {place}.
  There are {adjective2} {magical_creatures} and {adjective3} {magical_creatures2} here! In the {room_in_house} there is a pool full of {noun}.
  I fall asleep each night on a {noun2} of {nouns_plural} and dream of {adjective4} {nouns_plural2}. It feels as though I have lived here for {number} {time_measure}.
  I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun3}!!''')

print("Pick a template \n 1.  2.  3.")

while True:
    try:
        template = int(input("Choose template: 1, 2, 3: "))

        if template in [1, 2, 3]:
            break
        else:
            print("Invalid choice! Please choose 1, 2 or 3.")

    except ValueError:
        print("Please enter a valid number!")

if template == 1:
  Template1()
elif template == 2:
  Template2()
else:
  Template3()
