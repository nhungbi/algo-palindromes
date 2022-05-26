def palindrome(word):
    """
    Given a string or integer, return True if it is a palindrome,
    (reads the same backward or forward).
    """
    if not isinstance(word, str):
        word = str(word)
    
    word = word.lower()
    new_string = ''.join(filter(str.isalnum, word)) #before join is what is separating each element 

    reverse = new_string[::-1] 
    return reverse == new_string

# print(palindrome('Noon'))
# print(palindrome('Sore was I ere I saw Eros.'))
# print(palindrome('A man, a plan, a canal -- Panama'))
