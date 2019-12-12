def longest_substring(strng):
    len_substring=0
    longest=0
    for i in range(len(strng)):
        if i > 0:
            if strng[i] != strng[i-1]:
                len_substring = 0
        len_substring += 1
        if len_substring > longest:
            longest = len_substring          
    return longest
