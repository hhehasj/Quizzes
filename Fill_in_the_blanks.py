questions = ("The film, \"The ____ Redemption\" is based on a Stephen King novella.",
             "\"Jurassic ____\" is a blockbuster film directed by Steven Spielberg.",
             "In \"The Dark ____,\" Bruce Wayne is the alter ego of the superhero Batman.",
             "The character Jack Dawson appears in the film \"____,\" directed by James Cameron.",
             "The animated film, \"Toy ____\" features a cowboy doll named Woody.")

answers = ("Shawshank", "Park", "Knight", "Titanic", "Story")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    guess = input("Your guess: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
        print("――――――――――――――――――――――――――――")
    else:
        print("Wrong!")
        print(f"Correct answer: {answers[question_num]}")
        print("――――――――――――――――――――――――――――")
    question_num += 1


print("                  Results                     ")
print("――――――――――――――――――――――――――――")

print("Answers: ", end="|")
for answer in answers:
    print(answer, end="|")
print()

print("Guesses: ", end="|")
for guess in guesses:
    print(guess, end="|")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
