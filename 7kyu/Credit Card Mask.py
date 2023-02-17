# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.
# Examples

# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""

# // "What was the name of your first pet?"

# "Skippy" --> "##ippy"

# "Nananananananananananananananana Batman!"
# -->
# "####################################man!"

# return masked string
def maskify(card):
    l = 0
    listing = list(card)
    if len(card) <= 4:
        return card
    else:
        while l <= len(listing) - 5:
            listing[l] = '#'
            l += 1
        return ''.join(listing)
