def re_strip(input_string, chars=None):
    if chars is None:
        chars = " \t\n\r\x0b\x0c"
    start = 0
    end = len(input_string)

    while start < end and input_string[start] in chars:
        start += 1
    
    while start < end and input_string[end - 1] in chars:
        end -= 1
    
    return input_string[start:end]

print(re_strip("  Hello, World!  "))  
print(re_strip("**Hello, World!**", "*"))  
print(re_strip("--Hello, World!--", "-")) 

