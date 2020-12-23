# BTEXT
Bear Au Jus Text (btext) is a tool used for processing a text/string, optimized for data science and data analytics.\
btext can also implemented with pandas dataframe.

> + Latest Version Github Directory [1.0](https://github.com/haryobagas/bearaujus/tree/main/1.0)
> + PyPI [https://pypi.org/project/btext/](https://pypi.org/project/btext/)
> + Webpages [https://haryobagas.github.io/btext/](https://haryobagas.github.io/btext/)

# Latest Changelog
Release Date : 12/23/2020 `Version 1.0`
> + Initial Commit

# Installation
Get latest version of bearaujus
```
pip install btext --upgrade
```

# Documentation
## A. Core Module
Core module contains base functions of base text processing from bearaujus.
```.py
import btext as bt
```

### Core Module : Table of Contens
> + A.1. Converting Text to Consecutive Letter
> + A.2. Converting Text to Tokenized Consecutive Letter
> + A.3. Converting Text to Consecutive Number
> + A.4. Converting Text to Tokenized Consecutive Number
> + A.5. Converting Text to Consecutive Punctuation
> + A.6. Converting Text to Tokenized Consecutive Punctuation
> + A.7. Converting Text to Lower Case
> + A.8. Removing Spaces 
> + A.9. Removing Double Spaces
> + A.10. Removing Char by User Option
> + A.11. Removing Char by User Desired Length
> + A.12. Get All Valid Alphabet
> + A.13. Get Tokenized All Valid Alphabet
> + A.14. Get All Valid Number
> + A.15. Get Tokenized All Valid Number
> + A.16. Get All Valid Punctuation
> + A.17. Get Tokenized All Valid Punctuation
> + A.18. Normalizing a Text or a Collections
> + A.19. Converting Object to String

### A.1. Converting Text to Consecutive Letter
```.py
def conslet(val, sep=' ')
```
+ Example 1
```.py
text = '=,= im getting hungry~'
text = bt.conslet(text)
print(text)
```
> -> `im getting hungry`\
> Return Type : `String`

+ Example 2
```.py
text = '=,= im getting hungry~'
text = bt.conslet(text, sep = '~')
print(text)
```
> -> `im~getting~hungry`\
> Return Type : `String`

### A.2. Converting Text to Tokenized Consecutive Letter
```.py
def conslet_tokenized(val, sep=' ')
```
+ Example 1
```.py
text = 'John Mayer, Honne, Minami, Lisa'
text = bt.conslet_tokenized(text)
print(text)
```
> -> `['John', 'Mayer', 'Honne', 'Minami', 'Lisa']`\
> Return Type : `List`

+ Example 2
```.py
text = 'John Mayer, Honne, Minami, Lisa'
text = bt.conslet_tokenized(text, sep = ',')
print(text)
```
> -> `['John Mayer', 'Honne', 'Minami', 'Lisa']`\
> Return Type : `List`

### A.3. Converting Text to Consecutive Number
```.py
def consnum(val, sep='')
```
+ Example 1
```.py
text = '+62.81231.1231.123. This is random phone numbers ! -999-'
text = bt.consnum(text)
print(text)
```
> -> `62812311231123999`\
> Return Type : `String`

+ Example 2
```.py
text = '+62.81231.1231.123. This is random phone numbers ! -999-'
text = bt.consnum(text, sep = '-')
print(text)
```
> -> `62-81231-1231-123-999`\
> Return Type : `String`

### A.4. Converting Text to Tokenized Consecutive Number
```.py
def consnum_tokenized(val)
```
+ Example 1
```.py
text = '+62.81231.1231.123. This is random phone numbers ! -999-'
text = bt.consnum_tokenized(text)
print(text)
```
> -> `['62', '81231', '1231', '123', '999']`\
> Return Type : `List`

+ Example 2
```.py
text = '+62-81231-1231-123. This is random phone numbers ! ~~'
text = bt.consnum(text, sep = '-')
print(text)
```
> -> `62-81231-1231-123`\
> Return Type : `String`

### A.5. Converting Text to Consecutive Punctuation
```.py
def conspunc(val, sep = '') :
```
+ Example 1
```.py
text = 'Nyummy.... !!!! this is the best pancake ever :))))'
output = bt.conspunc(text)
print(output)
```
> -> `....!!!!:))))`\
> Return Type : `String`

+ Example 2
```.py
text = 'Nyummy.... !!!! this is the best pancake ever :))))'
output = bt.conspunc(text, sep = ' ')
print(output)
```
> -> `. . . . ! ! ! ! : ) ) ) )`\
> Return Type : `String`

### A.6. Converting Text to Tokenized Consecutive Punctuation
```.py
def conspunc_tokenized(val) :
```
+ Example
```.py
text = 'Nyummy.... !!!! this is the best pancake ever :))))'
output = bt.conspunc_tokenized(text)
print(output)
```
> -> `['.', '.', '.', '.', '!', '!', '!', '!', ':', ')', ')', ')', ')']`\
> Return Type : `List`

### A.7. Converting Text to Lower Case
```.py
def lower(val) :
```
+ Example
```.py
text = 'HeloOo WORLd !'
output = bt.lower(text)
print(output)
```
> -> `helooo world !`\
> Return Type : `String`

### A.8. Removing Spaces 
```.py
def remove_spaces(val) :
```
+ Example
```.py
text = 'Hel     lo Wor     ld'
output = bt.remove_spaces(text)
print(output)
```
> -> `HelloWorld`\
> Return Type : `String`

### A.9. Removing Double Spaces
```.py
def remove_double_spaces(val) :
```
+ Example
```.py
text = 'Hello    World from        Universe !'
output = bt.remove_double_spaces(text)
print(output)
```
> -> `Hello World from Universe !`\
> Return Type : `String`

### A.10. Removing Char by User Option
```.py
def removeby_char(val, exclude, sep = '') :
```
+ Example 1
```.py
text = 'i dont like math, i dont like wasabi'
output = bt.removeby_char(text, exclude = 'dont')
print(output)
```
> -> `i like math, i like wasabi`\
> Return Type : `String`

+ Example 2
```.py
text = 'i dont like math, i dont like wasabi'
output = bt.removeby_char(text, exclude = 'dont', sep = 'didnt')
print(output)
```
> -> `i didnt like math, i didnt like wasabi`\
> Return Type : `String`

+ Example 3
```.py
text = 'i dont like math, i dont like wasabi'
output = bt.removeby_char(text, exclude = ['i dont', 'like'])
print(output)
```
> -> `math, wasabi`\
> Return Type : `String`

+ Example 4
```.py
text = 'i dont like math, i dont like wasabi'
output = bt.removeby_char(text, exclude = ['i dont', 'like'], sep = '~')
print(output)
```
> -> `~ ~ math, ~ ~ wasabi`\
> Return Type : `String`

### A.11. Removing Char by User Desired Length
```.py
def removeby_length(val, exclude, sep = ' ') :
```
+ Example 1
```.py
text = 'Hi hi hi welcome to the jungle'
output = bt.removeby_length(text, exclude = 2)
print(output)
```
> -> `welcome the jungle`\
> Return Type : `String`

+ Example 2
```.py
text = 'Hi hi hi welcome to the jungle'
output = bt.removeby_length(text, exclude = 2, sep = '~')
print(output)
```
> -> `welcome~the~jungle`\
> Return Type : `String`

+ Example 3
```.py
text = 'Hi hi hi welcome to the jungle'
output = bt.removeby_length(text, exclude = [2, 3])
print(output)
```
> -> `welcome jungle`\
> Return Type : `String`

+ Example 4
```.py
text = 'Hi hi hi welcome to the jungle'
output = bt.removeby_length(text, exclude = [2, 3], sep = ' HEI ')
print(output)
```
> -> `welcome HEI jungle`\
> Return Type : `String`

### A.12. Get All Valid Alphabet
```.py
def getall_alphabet(sep = '', include_upper = False) :
```
+ Example 1
```.py
output = bt.getall_alphabet()
print(output)
```
> -> `abcdefghijklmnopqrstuvwxyz`\
> Return Type : `String`

+ Example 2
```.py
output = bt.getall_alphabet(sep = ' ')
print(output)
```
> -> `a b c d e f g h i j k l m n o p q r s t u v w x y z`\
> Return Type : `String`

+ Example 3
```.py
output = bt.getall_alphabet(include_upper = True)
print(output)
```
> -> `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`\
> Return Type : `String`

+ Example 4
```.py
output = bt.getall_alphabet(sep = '-', include_upper = True)
print(output)
```
> -> `a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z`\
> Return Type : `String`

### A.13. Get Tokenized All Valid Alphabet
```.py
def getall_alphabet_tokenized(include_upper = False) :
```
+ Example 1
```.py
output = bt.getall_alphabet_tokenized()
print(output)
```
> -> `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']`\
> Return Type : `List`

+ Example 2
```.py
output = bt.getall_alphabet_tokenized(include_upper = True)
print(output)
```
> -> `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']`\
> Return Type : `List`

### A.14. Get All Valid Number
```.py
def getall_number(sep = '') :
```
+ Example 1
```.py
output = bt.getall_number()
print(output)
```
> -> `0123456789`\
> Return Type : `String`

+ Example 2
```.py
output = bt.getall_number(sep = ' ')
print(output)
```
> -> `0 1 2 3 4 5 6 7 8 9`\
> Return Type : `String`

### A.15. Get Tokenized All Valid Number
```.py
def getall_number_tokenized() :
```
+ Example
```.py
output = bt.getall_number_tokenized()
print(output)
```
> -> `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']`\
> Return Type : `List`

### A.16. Get All Valid Punctuation
```.py
def getall_punc(sep = '') :
```
+ Example 1
```.py
output = bt.getall_punc()
print(output)
```
> -> `!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`\
> Return Type : `String`

+ Example 2
```.py
output = bt.getall_punc(sep = ' ')
print(output)
```
> -> `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ { | } ~`\
> Return Type : `String`

### A.17. Get Tokenized All Valid Punctuation
```.py
def getall_punc_tokenized() :
```
+ Example
```.py
output = bt.getall_punc_tokenized()
print(output)
```
> -> `['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']`\
> Return Type : `List`

### A.18. Normalizing a Text or a Collections
+ Converting Text to Consecutive Letter
+ Converting Text to Lower Case
+ Removing Double Spaces
```.py
def normalize(obj, show_process = False) :
```
+ Example 1
```.py
text = 'Nyummy8888888888888888 3235.... !!!! this is the best pancake ever :))))'
output = bt.normalize(text)
print(output)
```
> -> `nyummy this is the best pancake ever`\
> Return Type : `String`

+ Example 2
```.py
my_list = ['UwU this is so good :3', 'LETS GOO MAN !', 'okay you fine ! :3']
output = bt.normalize(my_list)
print(output)
```
> -> `['uwu this is so good', 'lets goo man', 'okay you fine']`\
> Return Type : `List`

+ Example 3
```.py
my_list = ['UwU this is so good :3', 'LETS GOO MAN !', 'okay you fine ! :3']
output = bt.normalize(my_list, show_process = True)
print(output)
```
> `Normalizing Data: [####################] 100.0% | P: 3 / 3 [ Done ]`\
> -> `['uwu this is so good', 'lets goo man', 'okay you fine']`\
> Return Type : `List`

### A.19. Converting Object to String
```.py
def to_string(obj) :
```
+ Example 1
```.py
number = 125.12525215
output = bt.to_string(number)
print(output)
```
> -> `125.12525215`\
> Return Type : `String`

+ Example 2
```.py
my_list = ['UwU this is so good :3', 'LETS GOO MAN !', 'okay you fine ! :3']
output = bt.to_string(my_list)
print(output)
```
> -> `UwU this is so good :3 LETS GOO MAN ! okay you fine ! :3`\
> Return Type : `String`

# Credit
+ Main Github Page : [https://github.com/haryobagas/](https://github.com/haryobagas/)
+ Linkedin : [https://www.linkedin.com/in/haryobagas08/](https://www.linkedin.com/in/haryobagas08/)
> Other documentation work in progress.

**Bear Au Jus - ジュースとくま** @2020
