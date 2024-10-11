def flames_game(name1, name2):
    # Step 1: Normalize the names (remove spaces and convert to lowercase)
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Step 2: Remove common characters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)

    # Step 3: Total number of remaining letters
    remaining_count = len(name1) + len(name2)

    # Step 4: FLAMES logic
    flames = "FLAMES"
    # Calculate the index to land on
    idx = (remaining_count - 1) % len(flames)

    # Step 5: Determine relationship
    result = flames[idx]

    relationship = {
        'F': "Friends",
        'L': "Lovers",
        'A': "Admirer",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Secret Admirer"
    }

    return result, relationship[result]
