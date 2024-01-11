import random
import string
import tqdm
import time

from tqdm import tqdm
import time

for i in tqdm(range(101),
              desc="Loading…",
              ascii=False, ncols=75):
    time.sleep(0.05)

print("Complete.")
print("▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒")
print("▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒")
print("▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒")
print("▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒")
print("▒▒▒▌────────▌▒▒▒▒▒▒▒")
print("▒▒█─────────▐▒▒▒▒▒▒▒")
print("▒▐▌─▐───────▐▄▄▒▒▒▒▒")
print("▒▐▌─▐────────▄▀▀█▒▒▒")
print("▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒")
print("▐▌────██▀█░█▄▒▄▄█▀▀▌")
print("▐▌──▌▐───▐░░▐▀░░░░░▌")
print("▐▌──▌────▐░░▐░░░░░░▌")
print("▐───▌────▐░░▐░░░░░░▌")
print("▐───█────▐░░▐░░░░░░▌")
print("▐───█────▐░░▐░░░░░░▌")
print("▐───█─────▀█▐▄▄▄█▀▀▒")
print("▀▄▄─▐───────▄█▒▒▒▒▒▒")
print("▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒")
print("▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒")
 time.sleep(0.02)

print("WELCOME")
user_name = input("Please enter your USERNAME : \n")
user_a = 'D3VSUM1'
user_b = 'SUM1D3V'
passw_ans = 'anusunil2214'
from tqdm import tqdm

for i in tqdm(range(100), desc="Loading..."):
    pass
time.sleep(0.05)
print(user_name)


if (user_name == user_a or user_name == user_b ):
    passw_1 = input("Please enter the Key : \n ")

    if (passw_1 == passw_ans):
        print("welcome", user_name)
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = ['w', ':', 'F', '|', 'u', 'g', 'P', '!', '?', 'j', 'G', 'l', '[', 'f', 'a', 'z', 's', '(', 'k', 'p', 'h', 'X', 'C', 'x', 'c', 'd', 'E', '+', '-', '>', '%', '}', '@', '~', '<', 'O', 'N', ' ', 'R', '`', '\\', '=', 'n', 'J', "'", 'e', '2', 'm', 'T', ';', 'B', 'Y', 'i', 'D', 'H', 'Q', '#', 'L', '7', '5', ']', 'o', ')', 'v', 'q', 'I', '.', 'r', '4', '/', 't', '0', '&', '{', 'V', 'W', '_', ',', '1', '3', '6', '8', 'y', '*', 'b', 'M', 'Z', '^', 'A', '$', '"', '9', 'K', 'S', 'U']

        print(chars)
        print(key)


        def main_pro():
            user_a = 'D3VSUM1'
            user_b = 'SUM1D3V'
            passw_ans = 'anusunil2214'
            ans_main = input("for encryption enter 1 : \n""for decryption press 0 : \n")
            if (ans_main == '1'):
                print("ENCRYPTING \n")

                plain_text = input("Enter a message to ENCRYPT: ")
                cipher_text = ""

                for letter in plain_text:
                    index = chars.index(letter)
                    cipher_text += key[index]

                print(f"original message : {plain_text}")
                print(f"encrypted message: {cipher_text}")
                restart_1 = input("AGAIN? 1/0 \n ")
                if (restart_1 == '1') :
                    for Q in tqdm(range(101),
                                  desc="REDIRECTING TOWARDS MAIN PAGE...",
                                  ascii=False, ncols=75):
                        time.sleep(0.01)
                    main_pro()
                else:
                    for w in tqdm(range(101),
                                  desc="EXITING...",
                                  ascii=False, ncols=75):
                        time.sleep(0.01)
                    exit()

            elif (ans_main == '0'):
                print("DECRYPTING\n")

                cipher_text = input("Enter a message to DECRYPT: ")
                plain_text = ""

                for letter in cipher_text:
                    index = key.index(letter)
                    plain_text += chars[index]

                print(f"encrypted message: {cipher_text}")
                print(f"original message : {plain_text}")
                restart_2 = input("AGAIN? 1/0 \n ")
                if (restart_2 == '1'):
                    for E in tqdm(range(101),
                                  desc="REDIRECTING TOWARDS MAIN PAGE...",
                                  ascii=False, ncols=75):
                        time.sleep(0.01)
                    main_pro()
                else:
                    for U in tqdm(range(101),
                                  desc="EXITING...",
                                  ascii=False, ncols=75):
                        time.sleep(0.01)
                    exit()

            else:

                print("invalid value entered try again ")
                exit()
        main_pro()

    else:

        print("wront password please try again later")
        exit()
else :
    print("Illegal login \n""0 Users found from the address", user_name)