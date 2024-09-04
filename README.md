# Password Strength Checker
===========================

**Name:** Diprit Turul 

**Company:** CODTECH IT SOLUTIONS PVT.LTD

**ID:** CT08DS6461

**Domain:** CYBER SECURITY & ETHICAL HACKING

**Duration:** AUGUST 15th, 2024 to SEPTEMBER 15th, 2024

## Overview
This Python script is a password strength checker that evaluates the strength of a given password based on various criteria. The script uses regular expressions to check for digits, uppercase letters, lowercase letters, and symbols in the password. It also checks against a list of common passwords from a file to penalize the use of weak passwords.

## Features

* Checks password length (at least 8 characters)
* Checks for digits, uppercase letters, lowercase letters, and symbols
* Penalizes the use of common passwords
* Provides feedback on password strength and suggestions for improvement
* Displays a password strength score (Weak, Moderate, or Strong)

## How to use

1. Run the script and enter a password when prompted.
2. The script will display the password strength score and provide feedback on how to improve the password.

## Technical Details

* The script uses the `re` module for regular expressions and the `pyfiglet` module for generating an ASCII banner.
* The script reads a list of common passwords from a file named `common_passwords.txt`.
* The password strength score is calculated based on the number of criteria met, with more weight given to digits and symbols.

