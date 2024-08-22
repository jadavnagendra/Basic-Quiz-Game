def quiz_game():
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Spain?",
            "options": ["A) Lisbon", "B) Madrid", "C) Rome", "D) Athens"],
            "answer": "B"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["A) 28", "B) 29", "C) 30", "D) 31"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        }
    ]

    score = 0

    print("Welcome to the Python Quiz Game!")
    print("You will be asked a series of multiple-choice questions. Try to answer them correctly.")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")
    print("Thank you for playing!")

# Directly call the quiz game function
quiz_game()
