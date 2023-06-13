# Encryption and Decryption Program

The Encryption and Decryption Program is a command-line application that provides a simple interface for encrypting and decrypting data using a substitution cipher. It allows you to securely encode your messages and decode them back to their original form.

## How it Works

The program uses a substitution cipher, which is a method of encryption where each letter in the plaintext is replaced with another letter based on a predefined key. In this program, the key is a fixed mapping between the characters of the input alphabet and their corresponding encrypted characters.

The encryption process involves taking a plaintext message and replacing each character with its corresponding encrypted character from the key. Conversely, the decryption process replaces each encrypted character with its original character from the key, thereby recovering the plaintext message.

## Features

- Authentication: The program requires the user to enter a username and password for authentication before accessing the encryption and decryption functionalities.

- Encryption: Users can enter a plaintext message, and the program will encrypt it using the substitution cipher and display the encrypted message.

- Decryption: Users can enter an encrypted message, and the program will decrypt it back to the original plaintext message using the substitution cipher.

- Customizable Key: The program uses a predefined key for encryption and decryption. If you want to change the mapping between characters, you can modify the `key` list in the code to suit your requirements.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/encryption-decryption-program.git
## Navigate to the project directory:

   cd encryption-decryption-program
   
## Install the required dependencies:
    pip install tqdm
## Usage
Run the program:
    python encryption_decryption.py

1. Enter your username when prompted.

2. Enter the password for authentication.

3. Choose whether to encrypt or decrypt a message.

4. Follow the instructions to enter the message and view the result.

5. You can repeat steps 4 and 5 to encrypt or decrypt additional messages.

## License
 This project is licensed under the MIT License.

vbnet

Feel free to modify and customize the README file according to your program's specific features and requirements.


