with open('input2.txt') as f:

    valid_pw_count = 0
    for line in f.readlines():
        # Parse input text
        frequencies, letter, password = line.split()
        lower, upper = map(int, frequencies.split('-'))
        letter = letter[0]

        # Check the password fits the criteria
        letter_frequency = password.count(letter)
        if lower <= letter_frequency <= upper:
            valid_pw_count += 1

    print(valid_pw_count)
    f.close()
