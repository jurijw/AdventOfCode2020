with open('input2.txt') as f:

    valid_pw_count_part1 = 0
    valid_pw_count_part2 = 0
    for line in f.readlines():
        # Parse input text
        frequencies, letter, password = line.split()
        lower, upper = map(int, frequencies.split('-'))
        letter = letter[0]

        # Check the password fits the criteria for part 1
        letter_frequency = password.count(letter)
        if lower <= letter_frequency <= upper:
            valid_pw_count_part1 += 1

        # Check the password fits the criteria for part 2
        if (password[lower - 1] == letter and password[upper - 1] !=
                letter) or (password[lower - 1] != letter and password[upper - 1] == letter):
            valid_pw_count_part2 += 1

    print(valid_pw_count_part1)
    print(valid_pw_count_part2)
    f.close()
