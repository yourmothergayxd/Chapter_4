# Colten Moran - Python Chapter 4 - 02142018
def compute_grade():
        if user_score > 1.0:
                print ("Bad Score.")

        elif user_score >= 0.9:
                print ("A")
                                
        elif user_score >= 0.8:
                print ("B")
                                
        elif user_score >= 0.7:
                print ("C")
                                
        elif user_score >= 0.6:
                print ("D")

        elif user_score < 0.6 and user_score >= 0.0:
                print("F")

                

try:
        user_score = float(input("Enter score: "))
                        
        if user_score > 1.0:
                compute_grade()
                                
        elif user_score >= 0.9:
                compute_grade()
                                
        elif user_score >= 0.8:
                compute_grade()
                                
        elif user_score >= 0.7:
                compute_grade()
                                
        elif user_score >= 0.6:
                compute_grade()

        elif user_score < 0.6 and user_score >= 0.0:
                compute_grade()

except ValueError:
        print("Please enter a number.")
