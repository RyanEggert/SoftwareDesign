def reverse_text(input_text):
    """
    Takes in some text and returns the text in reversed order
    (character by character)
    """
    
    new_name = ''   # Preallocate empty string for addition
    print range(len(input_text)-1, 0, -1)
    for i in range(len(input_text)-1, 0, -1):     # Added colon. Changed range to reflect zero-indexing
        new_name += input_text[i]
    return new_name     # Added return statement
    

def main():
    my_name = "whadya think?"
    print reverse_text(my_name)


if __name__ == "__main__":
    main()

