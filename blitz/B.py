
def longest_palindrome(s):
    max_length = 1
    start = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]

            if len(substr) > max_length and is_almost_palindrome(substr):
                start = i
                max_length = len(substr)
  
    return max_length

def is_almost_palindrome(s):
    mismatches = 0
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            mismatches += 1
        if mismatches > 1:
            return False
        left, right = left + 1, right - 1

    return True
input()


print(longest_palindrome(input()))