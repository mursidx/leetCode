# Function to join given strings
def combo_string(a, b):

    # your code here
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a