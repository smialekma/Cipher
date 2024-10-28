# Content of Project
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

## General info
This project is a simple command-line app allowing for text encryption and decryption using ROT13 and ROT47 ciphers (Ceasar cipher) with extra file handling functionality.
The texts might be decoded/encoded both directly from json file and from user input - and bulk-saved to another (or the same) json file.
Thanks to implementing the best coding practices and design patterns (Facade/Factory) this project is easily modifiable and extendable (for example, with different kinds of ciphers).

## Technologies
<ul>
<li>Python</li>
<li>JSON</li>
</ul>

## Setup
1. Clone the repo
```git clone https://github.com/smialekma/Cipher.git```

2. Install the required dependencies:
```pip install -r requirements.txt```

3. To start the program, run the following command:
```python run.py```

## More detailed information about modules
<details>
<summary><b>Decoders</b></summary>
Includes Decoder Factory and specific cipher classes with their encode/decode methods.
</details>
<details>
<summary><b>File Handler</b></summary>
JSON-based file operations (reading, writing and appending) with user-defined file paths and exception handling.
</details>
<details>
<summary><b>Buffer</b></summary>
Logger that holds all the texts used during the program operation. Allows for efficient loading from and saving to files.
</details>
<details>
<summary><b>Manager</b></summary>
Simple higher-level interface granting easy access to all of the functionalities (displaying menus, processing texts, filehandling).
</details>
<details>
<summary><b>Menu</b></summary>
User-friendly interface for selecting functions.
</details> 

## Application view
