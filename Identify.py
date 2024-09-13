questions = ("In what country did the first Starbucks open outside of North America?",
             "In a website browser address bar, what does “www” stand for?",
             "Who was the first woman pilot to fly solo across the Atlantic?",
             "Who was the first woman to win a Nobel Prize?",
             "Chrome, Safari, Firefox and Explorer are different types of what?")

answers = ("Japan", "World Wide Web", "Amelia Earhart", "Marie Curie", "Web Browsers")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    guess = input("Your guess: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
        print("――――――――――――――――――――――――――――")
    else:
        print("Wrong!")
        print(f"Correct answer: {answers[question_num]}")
        print("――――――――――――――――――――――――――――")

    question_num += 1

print("                   Results                   ")
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
