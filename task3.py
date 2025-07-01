import re

def password_complexity_checker( passwrod ):
    
    # Check lenght
    lenght_score = len(passwrod) >=8

    # Check for Uppercase letters
    uppercaseScore = bool( re.search( r'[A-Z]', passwrod ) )

    # Check for lowercase letters
    lowercase_score = bool( re.search(r'[a-z]', passwrod))

    # Check for numbers
    numberScore = bool( re.search( r'[0-9]' , passwrod) )

    # Check for special charracters
    special_char_score = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]' , passwrod ) )

    # Calculate total score
    totalScore = lenght_score + uppercaseScore + lowercase_score + numberScore + special_char_score

    # Give feedback
    if totalScore == 5:
        return "Strong password!"
    elif totalScore >=3 :
        return "Good passwrod."
    else:
        return "Weak password, try again."

password = input( "Type your password: ")
result = password_complexity_checker(password)
print ( f"Password strenght : {result}" )
