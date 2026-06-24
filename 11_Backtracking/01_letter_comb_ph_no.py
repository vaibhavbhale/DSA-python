def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res = []

    def backtrack(combination, next_digits):
        if not next_digits:
            res.append(combination)
            return

        for letter in phone[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)
    return res


# Input
digits = "23"

# Function call
print(letterCombinations(digits))


# Dry Run:

# Initial:
# digits = "23"
# res = []

# Call backtrack("", "23")

# next_digits[0] = "2"
# phone["2"] = "abc"

# Loop for "a":
# combination = "" + "a" = "a"
# Call backtrack("a", "3")

#   next_digits[0] = "3"
#   phone["3"] = "def"

#   Loop for "d":
#   combination = "a" + "d" = "ad"
#   Call backtrack("ad", "")
#   next_digits empty → add "ad" to res

#   Loop for "e":
#   combination = "a" + "e" = "ae"
#   Call backtrack("ae", "")
#   add "ae" to res

#   Loop for "f":
#   combination = "a" + "f" = "af"
#   Call backtrack("af", "")
#   add "af" to res


# Loop for "b":
# combination = "" + "b" = "b"
# Call backtrack("b", "3")

#   "bd" → add to res
#   "be" → add to res
#   "bf" → add to res


# Loop for "c":
# combination = "" + "c" = "c"
# Call backtrack("c", "3")

#   "cd" → add to res
#   "ce" → add to res
#   "cf" → add to res


# Final res:
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]