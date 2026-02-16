import random

# Prize ladder (15 questions)
ladder = [
    1000, 2000, 3000, 5000,
    10000, 20000, 40000, 80000,
    160000, 320000, 640000,
    1250000, 2500000, 5000000,
    10000000
]

# Guaranteed money levels (question index starts from 0)
safe_levels = {
    4: 5000,
    9: 160000
}

questions = [
    {
        "question": "Which bird is the fastest in the world?",
        "options": ["Hummingbird", "Black Widow", "Falcon", "Seagull"],
        "answer": "c"
    },
    {
        "question": "From which direction does the sun rise?",
        "options": ["North", "South", "West", "East"],
        "answer": "d"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "a"
    }
]

lifelines = {
    "50-50": True,
    "audience": True,
    "expert": True
}

money_won = 0

print("WELCOME TO KAUN BANEGA CROREPATI")

for i, q in enumerate(questions):
    print(f"\nQuestion {i + 1} for Rs.{ladder[i]}")
    print(q["question"])

    for key, option in zip(["a", "b", "c", "d"], q["options"]):
        print(f"{key}. {option}")

    print("\nAvailable lifelines:")
    for ll, status in lifelines.items():
        if status:
            print("-", ll)

    choice = input("\nEnter option (a/b/c/d), L for lifeline, Q to quit: ").lower()

    if choice == "q":
        print("You quit the game.")
        print("You take home Rs.", money_won)
        break

    if choice == "l":
        ll = input("Choose lifeline (50-50 / audience / expert): ").lower()

        if ll == "50-50" and lifelines["50-50"]:
            lifelines["50-50"] = False
            correct = q["answer"]
            wrong = [o for o in ["a", "b", "c", "d"] if o != correct]
            removed = random.sample(wrong, 2)
            print("Remaining options:", correct, removed[0])
        elif ll == "audience" and lifelines["audience"]:
            lifelines["audience"] = False
            print("Audience poll suggests option:", q["answer"])
        elif ll == "expert" and lifelines["expert"]:
            lifelines["expert"] = False
            print("Expert suggests option:", q["answer"])
        else:
            print("Lifeline not available.")

        choice = input("Enter your final answer: ").lower()

    if choice == q["answer"]:
        money_won = ladder[i]
        print("Correct answer. You have won Rs.", money_won)

    else:
        print("Wrong answer.")
        for level in sorted(safe_levels.keys(), reverse=True):
            if i >= level:
                money_won = safe_levels[level]
                break
        else:
            money_won = 0

        print("Game over.")
        print("You take home Rs.", money_won)
        break

else:
    print("Congratulations. You completed the game.")
    print("You won Rs.", money_won)
