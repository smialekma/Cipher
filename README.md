# Content of Project
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

## General info
This project is a simple command-line app allowing for text encryption and decryption
using ROT13 and ROT47 ciphers (Ceasar cipher) with extra file handling functionality.
The texts might be decoded/encoded both directly from json file 
and from user input - and bulk-saved to another (or the same) json file.
Thanks to implementing the best coding practices and design patterns (Facade/Factory)
this project is easily modifiable and extendable (for example, with different kinds of ciphers).

## Technologies & Tools
<ul>
<li>Python 3.12</li>
<li>Pytest</li>
<li>Pre-commit</li>
<li>GitHub Actions</li>
</ul>

## Setup
1. Clone the repo
```bash
git clone https://github.com/smialekma/Cipher.git
```

2. Create virtual environment (optional)
```bash
python -m venv .venv
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. To start the program, run the following command:
```bash
python run.py
```

## More detailed information about modules
<details>
<summary><b>Decoders</b></summary>
Includes Decoder Factory and specific cipher classes with their encode/decode methods.
</details>
<details>
<summary><b>File Handler</b></summary>
JSON-based file operations (reading, writing and appending) 
with user-defined file paths and exception handling.
</details>
<details>
<summary><b>Buffer</b></summary>
Memory object that holds all the texts used during the program operation.
Allows for efficient loading from and saving to files.
</details>
<details>
<summary><b>Manager</b></summary>
Simple higher-level interface granting easy access to all the functionalities
(displaying menus, processing texts, file handling).
</details>
<details>
<summary><b>Menu</b></summary>
User-friendly interface for selecting functions.
</details> 

## Application view
<img src="https://github.com/user-attachments/assets/25af4b82-77a3-45b6-acd5-00a132529fa1" width=”50%” height=”50%”></img>
