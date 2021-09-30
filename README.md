# Omicron
![GitHub last commit](https://img.shields.io/github/last-commit/eoBattisti/Omicron?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eoBattisti/Omicron?style=flat-square)

Omicron is a Command Line Interface -- CLI building to delete, extract, list, move and organize files.

## Features
- Delete one or all directory's files :wastebasket:
- Extract files from ZIP and RAR archives :package:
- List all directory's files :page_with_curl:
- Move a file to a directory :mailbox_with_no_mail:
- Organize all files in a directory  :books:
  
### Features to implement
- Delete
  - Implement functionalities to the user delete files by:
    - Date;
    - File size.
- Extract
  - List the files inside the archive .zip or .rar;
  - Extract just one or more files from the .zip/.rar.
- List Files:
  - Implement list the files by:
    - Date;
    - Size;
    - Name.
- Open Files:
  - allow the user to create or read files   
## How to install
- goes to setup.py
- in the terminal:

``` pip install . -e ```

## Motivation
So, I decided to code that project because I was bored that always I needed to organize my directories and folders, and know the challenges building a CLI program,
so Omicron could/ and now helps me doing that!:smile: I was thinking how simple and minimalistic it could works, then I start searching about CLIs and how it works, 
googling seemmed easy to code (During the process I discovered that was a bit harder:sweat_smile:).


### Why Python :snake:?
Python was the first language that I learned and I have a affection for. Using python for me it's very fun
and flexible. And konwing the language and some packages and librarys was really helpful while coding Omicron.


### Why Click :computer_mouse:?
When I was googling searching for tools to develop the project Click appeared between others librarys and package,
I started to read a little bit of each documentation and some tutorials on Youtube, and in Click website [here](https://click.palletsprojects.com/en/8.0.x/)
they say that package: "It aims to make the process of writing command line tools quick and fun". 


### Challenges 
First things first, realize how to code that project in OOP was a bit harder for me, until I realize that I needed to pass my object through the arguments for the
others commands, so there they could handle it.

Code all commands in the same file that was my main object, in that case the code was becoming bigger and was really harder to identify
the commands and the functions that helps each one. To overcome that, I resolved to split all my commands inside a folder named "commands", 
doing that helps me a lot debbuging and refactoring. The problem was solved but another become alive.

Importing my commands in my main file didn't work, so back to googling and searching into the Click documentation I discovered about Multicommand lines. It
was the necessary to Omicron runs perfectly as I wanted.  



