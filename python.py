# Slutprojekt 
from colours import bcolors

# Lista med frågor om Tom och Jerry
questions = (bcolors.DEFAULT + "Who is the main antagonist in Tom and Jerry?:",
            bcolors.DEFAULT +"What is the primary setting for most Tom and Jerry episodes?:",
            bcolors.DEFAULT +"Which character is known for his cleverness and ability to outsmart Tom?:",
            bcolors.DEFAULT +"What is the typical outcome of Tom's attempts to catch Jerry?:",
            bcolors.DEFAULT +"Who is Tom's owner and often scolds him for his failures?:",
            bcolors.DEFAULT +"What type of animal is Jerry?:",
            bcolors.DEFAULT +"Which character is known for being bigger and often protects Jerry from Tom's attacks?:",
            bcolors.DEFAULT +"What is the primary method Tom uses to try to catch Jerry?:" )

# Alternativ för varje fråga
options = (("A. Spike", "B. Jerry", "C. Tom", "D. Butch"), 
            ("A. A farm", "B. A city", "C. A forest", "D. A desert"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. He catches Jerry", "B. He fails", "C. He gets hurt", "D. He gets rewarded"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. Mouse", "B. Cat", "C. Dog", "D. Bird"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. Traps", "B. His claws", "C. His teeth", "D. His speed"))

answers = ("C", "B", "B", "B", "C", "A", "A", "A") # Korrekta svar för varje fråga
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
    
    if guess == 'Q':  # Avsluta och visa resultat
        break
    elif guess == 'P':  # Gå till föregående fråga
        if question_num > 0:
            question_num -= 1
    elif guess == 'N':  # Gå till nästa fråga
        if question_num < len(questions) - 1:
            question_num += 1
    elif guess in ['A', 'B', 'C', 'D']:  # Registrera användarens gissning
        guesses[question_num] = guess

# Utvärdera resultatet
for i in range(len(questions)):
    if guesses[i] == answers[i]:
        score += 1

print(bcolors.DEFAULT + ":+:-:+:-" * 5) 
print(bcolors.YELLOW + "              RESULTS           ")
print(bcolors.DEFAULT + ":+:-:+:-" * 5)

print(bcolors.CYAN + " answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print(" guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Beräknar poängen som en procentandel och skriver ut den 
score = int(score / len(questions) * 100)
print(f" Your score is: {score}%")
