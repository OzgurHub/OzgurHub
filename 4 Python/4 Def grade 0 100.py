def grade_calculator():
    while True:
        # Prompt the user for input
        user_input = input("Enter the student's numerical grade (0-100), or type 'exit' to quit: ").strip().lower()
        
        # Check if the user wants to exit
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        try:
            # Attempt to convert the input into a number
            score = float(user_input)
            
            # Validate the score range
            if 0 <= score <= 100:
                # Determine the letter grade
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                
                # Display the result
                print(f"The student's grade is: {grade}")
            else:
                print("Error: The score must be between 0 and 100.")
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a valid numerical grade or type 'exit' to quit.")

# Run the grade calculator
grade_calculator()
