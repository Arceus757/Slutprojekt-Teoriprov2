import json
from colours import bcolors

# Ladda JSON-fil
with open('questions.json', 'r') as file:
    data = json.load(file)

questions = [bcolors.DEFAULT + q['question'] for q in data['questions']]
options = [tuple(q['options']) for q in data['questions']]
answers = [q['answer'] for q in data['questions']]

guesses = [""] * len(questions) # Lista för användarens gissningar
score = 0 # Variabel för poäng
question_num = 0  # Variabel för att hålla koll på vilken fråga som är aktuell

while True:
    print(":+:-:+:-" * 8) # Skriver ut en rad med plus-tecken för att separera frågorna 
    print(questions[question_num])
    for option in options[question_num]:
        print(option)
    
    if guesses[question_num]:
        print(f"Previous answer: {guesses[question_num]}")

    guess = input("Enter (A, B, C, D) or 'P' for previous, 'N' for next, 'Q' to quit and submit: " + bcolors.CYAN).upper()
    
    while guess not in ['A', 'B', 'C', 'D', 'P', 'N', 'Q']:  # Kontrollera om inmatningen är giltig
        guess = input(bcolors.RED + "Invalid input. Enter (A, B, C, D) or 'P' for previous, 'N' for next, 'Q' to quit and submit: " + bcolors.CYAN).upper()
    
    if guess == 'Q':  # Avsluta och visa resultat
        break
    elif guess == 'P':  # Gå till föregående fråga
        if question_num > 0:
            question_num -= 1
    elif guess == 'N':  # Gå till nästa fråga
        if question_num < len(questions) - 1:
            question_num += 1
    else:  # Registrera användarens gissning
        guesses[question_num] = guess

# Utvärdera resultatet
print(bcolors.DEFAULT + ":+:-:+:-" * 5) 
print(bcolors.YELLOW + "              RESULTS           ")
print(bcolors.DEFAULT + ":+:-:+:-" * 5)

print(bcolors.CYAN + " answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print(" ur guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Beräknar poängen som en procentandel och skriver ut den 
score = int(score / len(questions) * 100)
print(f" Your score is: {score}%")
