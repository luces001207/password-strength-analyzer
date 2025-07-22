# analyzer.py
import math
import string

def shannon_entropy(password):
    chars = set(password)
    entropy = -sum((password.count(c)/len(password)) * math.log2(password.count(c)/len(password)) for c in chars)
    return round(entropy, 2)

def contains_dictionary_word(password, dictionary_file="dictionary.txt"):
    try:
        with open(dictionary_file) as f:
            common_words = [line.strip().lower() for line in f]
        return any(word in password.lower() for word in common_words)
    except FileNotFoundError:
        return False

def evaluate_password(password):
    score = 0
    feedback = []

    length = len(password)
    entropy = shannon_entropy(password)
    
    if length >= 12:
        score += 20
    else:
        feedback.append("Password is shorter than 12 characters.")

    if any(c.islower() for c in password): score += 10
    else: feedback.append("No lowercase letters.")
    
    if any(c.isupper() for c in password): score += 10
    else: feedback.append("No uppercase letters.")

    if any(c.isdigit() for c in password): score += 10
    else: feedback.append("No digits.")

    if any(c in string.punctuation for c in password): score += 10
    else: feedback.append("No symbols.")

    if not contains_dictionary_word(password):
        score += 20
    else:
        feedback.append("Contains common dictionary word.")

    if entropy >= 3.5:
        score += 20
    else:
        feedback.append("Low entropy.")

    if score >= 80:
        rating = "Very Strong"
    elif score >= 60:
        rating = "Strong"
    elif score >= 40:
        rating = "Medium"
    else:
        rating = "Weak"

    return {"score": score, "rating": rating, "entropy": entropy, "feedback": feedback}