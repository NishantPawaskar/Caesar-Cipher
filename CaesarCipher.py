logo = '''
   ____                              ____ _       _               
  / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
 | |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
 | |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
  \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
                                           |_|                    
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(s_direction, o_text, s_num):
    f_text = ""
    if s_direction == "decode":
        s_num *= -1
    for char in o_text:
        if char in alphabet:
            o_position = alphabet.index(char)
            n_position = o_position + s_num
            f_text += alphabet[n_position]
        else:
            f_text += char
    
    print(f"The {direction}d text is {f_text}")

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(direction, text, shift)
    
    result = input("Do you wish to continue?\n").lower()
    if result == "n" or result == "no":
        should_continue = False
        print("Goodbye")