def isHappy(n):
    visit = set()  

    def get_next_number(n):
        output = 0

        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10

        return output

    while n not in visit:
        visit.add(n)   
        n = get_next_number(n)
        if n == 1:
            return True

    return False

print(isHappy(19))

 # Example Dry Run for n = 19:
        # Step 1: 19 → (1² + 9²) = 82
        # Step 2: 82 → (8² + 2²) = 68
        # Step 3: 68 → (6² + 8²) = 100
        # Step 4: 100 → (1² + 0² + 0²) = 1