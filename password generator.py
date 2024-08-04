#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#project for softcod: random password generator 

import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected")
   
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = generate_password(
        length=password_length,
        use_uppercase=include_uppercase,
        use_lowercase=include_lowercase,
        use_digits=include_digits,
        use_special=include_special
    )

    print(f"Generated Password: {generated_password}")


# In[ ]:




