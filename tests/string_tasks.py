def reverse(string):
    rv=''
    for char in string:
        rv = char + rv
    return(rv)