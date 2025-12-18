def solve_euler_836():
    # The problem asks for the concatenation of the first letters of each bolded word.
    # The bolded phrases in the original problem text are:
    bolded_phrases = [
        "affine plane",
        "radically integral local field",
        "open oriented line section",
        "jacobian",
        "orthogonal kernel embedding"
    ]
    
    result = ""
    for phrase in bolded_phrases:
        # Split the phrase into words
        words = phrase.split()
        for word in words:
            # Append the first letter of each word
            result += word[0]
            
    return result

if __name__ == "__main__":
    answer = solve_euler_836()
    print(f"The concatenation of the first letters is: {answer}")