import math
import random
from itertools import permutations

# 1. Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(100))


# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

print(fahrenheit_to_celsius(212))


# 3. Chickens and rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

print(solve(35, 94))


# 4. Filter primes from list
def filter_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in nums if is_prime(n)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 11, 13]))


# 5. Permutations of string
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(string_permutations("abc"))


# 6. Reverse words in a sentence
def reverse_sentence(s):
    return ' '.join(s.split()[::-1])

print(reverse_sentence("I love Python"))


# 7. Check if list contains 3 next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3, 4]))


# 8. Check if list contains 007 in order
def spy_game(nums):
    pattern = [0, 0, 7]
    j = 0
    for n in nums:
        if n == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))


# 9. Volume of sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

print(sphere_volume(5))


# 10. Unique elements of a list
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_list([1, 2, 2, 3, 4, 4, 5]))


# 11. Palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))


# 12. Histogram
def histogram(lst):
    for n in lst:
        print('*' * n)

histogram([4, 9, 7])


# 13. Guess the number game (автоматическая версия)
def guess_the_number():
    name = "Zhansaya"
    number = random.randint(1, 20)
    guesses = 0
    test_guesses = [5, 10, number]  # тестовые ходы
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    for guess in test_guesses:
        guesses += 1
        print(f"Guess: {guess}")
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()
