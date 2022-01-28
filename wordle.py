def highlight(word, guess):
    result = '-----'
    unguessed = ''
    check_again = ''

    for i in range(len(guess)):
        guess_letter = guess[i]
        actual_letter = word[i]
        
        if guess_letter == actual_letter:
            before = result[: i]
            after = result[i + 1:]
            result = before + actual_letter.upper() + after
        else:
            check_again += guess_letter
            unguessed += actual_letter

    for i in range(len(word)):
        guess_letter = guess[i]
        actual_letter = word[i]

        if actual_letter != guess_letter and guess_letter in unguessed:
            before = result[: i]
            after = result[i + 1:]
            result = before + guess_letter.lower() + after
            unguessed = unguessed.replace(guess_letter, '', 1)
            
    return result


print(highlight('swift', 'stink')) # StI--
print(highlight('swift', 'stiff')) # StIF-
print(highlight('swift', 'swift')) # SWIFT
print(highlight('staff', 'shaft')) # S-AFt
print(highlight('staff', 'fasts')) # fast-
print(highlight('staff', 'puffs')) # --fFs
print(highlight('staff', 'fluff')) # ---FF
print(highlight('aaaaa', 'aabbb')) # AA---
print(highlight('ababa', 'babab')) # baba-

