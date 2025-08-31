import random
import time

class Question:
    def __init__(self, question, options, correct_answer, explanation=""):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0
        
    def add_question(self, question, options, correct_answer, explanation=""):
        """Add a question to the quiz"""
        self.questions.append(Question(question, options, correct_answer, explanation))
        self.total_questions = len(self.questions)
    
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("=" * 60)
        print("🎯 WELCOME TO THE PYTHON QUIZ APP! 🎯")
        print("=" * 60)
        print("Instructions:")
        print("- Answer each question by entering A, B, C, or D")
        print("- You'll get immediate feedback on your answers")
        print("- Your final score will be displayed at the end")
        print("- Good luck! 🍀")
        print("=" * 60)
        print()
    
    def display_question(self, question_obj, question_num):
        """Display a single question with options"""
        print(f"Question {question_num}: {question_obj.question}")
        print()
        
        for i, option in enumerate(question_obj.options):
            letter = chr(65 + i)  # A, B, C, D
            print(f"{letter}. {option}")
        print()
    
    def get_user_answer(self):
        """Get and validate user input"""
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print("❌ Invalid input! Please enter A, B, C, or D.")
    
    def check_answer(self, user_answer, correct_answer):
        """Check if user answer is correct"""
        return user_answer == correct_answer
    
    def display_feedback(self, is_correct, correct_answer, explanation):
        """Display feedback for user's answer"""
        if is_correct:
            print("✅ Correct! Well done!")
            self.score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {correct_answer}")
        
        if explanation:
            print(f"💡 {explanation}")
        print()
        time.sleep(1)  # Brief pause for better UX
    
    def display_final_results(self):
        """Display final quiz results"""
        print("=" * 60)
        print("🎉 QUIZ COMPLETED! 🎉")
        print("=" * 60)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(f"Final Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        # Provide feedback based on score
        if percentage >= 90:
            print("🏆 Excellent! You're a quiz master!")
        elif percentage >= 80:
            print("🌟 Great job! You really know your stuff!")
        elif percentage >= 70:
            print("👍 Good work! You have solid knowledge!")
        elif percentage >= 60:
            print("📚 Not bad! Keep learning and improving!")
        else:
            print("📖 Keep studying! Practice makes perfect!")
        
        print("=" * 60)
    
    def run_quiz(self):
        """Run the complete quiz"""
        if not self.questions:
            print("❌ No questions available! Please add questions first.")
            return
        
        self.display_welcome()
        
        # Shuffle questions for variety
        shuffled_questions = self.questions.copy()
        random.shuffle(shuffled_questions)
        
        for i, question in enumerate(shuffled_questions, 1):
            self.display_question(question, i)
            user_answer = self.get_user_answer()
            
            # Convert user answer to correct format for comparison
            correct_letter = chr(65 + question.options.index(question.correct_answer))
            is_correct = self.check_answer(user_answer, correct_letter)
            
            self.display_feedback(is_correct, correct_letter, question.explanation)
        
        self.display_final_results()

def create_sample_quiz():
    """Create a sample quiz with Python-related questions"""
    quiz = Quiz()
    
    # Add sample questions
    quiz.add_question(
        "What is the correct way to create a function in Python?",
        [
            "function myFunction():",
            "def myFunction():",
            "create myFunction():",
            "func myFunction():"
        ],
        "def myFunction():",
        "In Python, functions are defined using the 'def' keyword."
    )
    
    quiz.add_question(
        "Which of the following is used to create a list in Python?",
        [
            "()",
            "[]",
            "{}",
            "<>"
        ],
        "[]",
        "Lists in Python are created using square brackets []."
    )
    
    quiz.add_question(
        "What is the output of print(2 ** 3)?",
        [
            "6",
            "8",
            "5",
            "Error"
        ],
        "8",
        "The ** operator is used for exponentiation. 2^3 = 8."
    )
    
    quiz.add_question(
        "Which method is used to add an element to a list?",
        [
            "add()",
            "append()",
            "insert()",
            "push()"
        ],
        "append()",
        "The append() method adds an element to the end of a list."
    )
    
    quiz.add_question(
        "What does the 'self' keyword represent in Python classes?",
        [
            "The class itself",
            "The instance of the class",
            "A reserved keyword",
            "The parent class"
        ],
        "The instance of the class",
        "'self' refers to the instance of the class that is being created."
    )

    quiz.add_question(
        "what command is used to install packages in python",
        ["pop",
         "pap",
         "wow",
         "pip"
         ],
         "pip",
         "pip is used to install python packages via the terminal"
         
    )
    
    return quiz


def main():
    """Main function to run the quiz app"""
    print("🎯 Python Quiz App")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Take the sample quiz")
        print("2. Create a custom quiz")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            quiz = create_sample_quiz()
            quiz.run_quiz()
            
        elif choice == "2":
            print("\nCustom quiz feature coming soon!")
            print("For now, enjoy the sample quiz!")
            
        elif choice == "3":
            print("👋 Thanks for playing! Goodbye!")
            break
            
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
        
        # Ask if user wants to play again
        if choice in ["1", "2"]:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again != 'y':
                print("👋 Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    main()
