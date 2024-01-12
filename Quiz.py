class QuizGame:
    def __init__(self, questions):
        # Initialize the QuizGame object with a list of questions
        self.questions = questions
        self.user_score = 0  # Initialize the user's score to zero

    def run_quiz(self):
        # Method to run the quiz and gather user input for each question
        for idx, question_data in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question_data['question']}")
            for option in question_data['options']:
                print(option)

            # Get user input and convert to uppercase for case-insensitive comparison
            user_answer = input("Your answer: ").upper()

            # Check if the user's answer is correct and provide feedback
            if user_answer == question_data['correct_answer']:
                print("Correct!")
                self.user_score += 1  # Increment the user's score for each correct answer
            else:
                print(f"Wrong! The correct answer is {question_data['correct_answer']}.")

    def display_final_score(self):
        # Method to display the final score after completing the quiz
        print("\nQuiz completed!")
        print(f"Your final score is: {self.user_score}/{len(self.questions)}")

def main():
    # Define the quiz questions, options, and correct answers
    quiz_data = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
            "correct_answer": "B"
        },
        {
            "question": "Which programming language is known for its readability?",
            "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
            "correct_answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "correct_answer": "B"
        }
    ]

    # Create an instance of the QuizGame class with the defined quiz_data
    quiz_instance = QuizGame(quiz_data)

    print("Welcome to the Basic Quiz Game!\n")
    
    # Run the quiz using the QuizGame class methods
    quiz_instance.run_quiz()
    quiz_instance.display_final_score()

if __name__ == "__main__":
    main()
