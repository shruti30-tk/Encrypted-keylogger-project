# Encrypted-keylogger-project

# Overview:
This project is a beginner-level keylogger written in Python. It captures keyboard inputs, encrypts them using Fernet encryption, and stores them securely in a text file. It also simulates sending that data to a remote server by writing it into a local folder called `fake_server`.

# Key Features:
- Captures keystrokes using `pynput`
- Encrypts the data with the `cryptography` library
- Saves the encrypted data in a safe local file
- Simulates a remote server to store the stolen data
- Easy to understand, beginner-friendly code
- Fully functional and secure for learning/demo purposes

# Folder Structure:
- `smart_keylogger.py` → Main script with encryption + logging
- `secret.key` → Encryption key file
- `encrypted_log.txt` → Output of encrypted keylogs
- `fake_server/stolen_data.txt` → Simulated server-side log
- `README.txt` → This file :)

# Tools Used:
- Python 3
- pynput
- cryptography (Fernet)

# How to Run:
1. Make sure you have Python 3 installed.
2. Install the libraries:
pip install pynput cryptography
3. Run `smart_keylogger.py` in any Python IDE or terminal.
4. It will generate and use `secret.key` to encrypt the logs.

# Outcome:
Successfully developed a basic encrypted keylogger using Python.  
Learned how to:
- Capture keyboard input
- Encrypt data using Fernet
- Simulate safe data storage
This project strengthened my understanding of Python libraries and basic cybersecurity concepts.

# Important:
This project is made "Only for Educational Purposes". It is meant to help me understand encryption, logging, and data simulation. Please don’t use it for any unethical activities.

# Conclusion:
This project helped me understand the basics of Python scripting, keyboard input logging, and secure data handling through encryption. It’s a simple yet powerful example of how cybersecurity concepts like keylogging and encryption work together.

