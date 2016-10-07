def palindrome(number):
    number_string = str(number)
    reversed_string = number_string[::-1]
    return number_string == reversed_string

def traverse():
    max_palindrome = 0
    n_1 = 999
    while(n_1 > 99):
        n_2 = n_1
        while(n_2 > 99):
            product = n_1 * n_2
            if(palindrome(product)):
                print n_1, n_2, product
                if product>max_palindrome:
                    max_palindrome = product
                break
            n_2 -= 1
        n_1 -= 1
    return max_palindrome

print traverse()
