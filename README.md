# ShiPython

It is self-training tool to learn python. Please develop the function for eacy python code. Then, submit it! 

I hope it also helps instructors of the python exercise class. It has the functionality of an automatic checking mechanism. 
It provides the instructors with the excel sheets for checking the progress of learners. It also includes automatic checking functionality with the webserver.

Enjoy!

## For Learners

  1. Get shipython.zip. For the self-training learner, please use shipython.zip on this repository, or an instructor distributes the file for you.
  1. Unzip the file:
     ```
     % unzip shipython.zip
     % cd shipython
     ```
  1. Edit python file like A00.py. Don't forget to change the ID.
  1. Check the code by:
     ```
     % python A00.py
     ```
  1. If your code works fine, submit the code:
     ```
     % python submit.py A00.py
     ```
  1. If the test is passed you will have the message like:
     ```
     -------
     PASSED. testA00.py
     code:  DE94  (01234)
     ```
  1. Report the code to your instructors.
  1. If the test is failed, please re-edit the code and try again.
  1. (Optional) If your instructors provide the *URL*. Your data is automatically uploaded. You can view their progress and the ranking of the code size competition by accesing the *URL* with their your and the code of the first problem.

## Virtual environment (pyenv)

 The virtual environment like pyenv is very useful. 
 
 Please [google by "python pyen"](https://www.google.com/search?q=python+pyenv). 
 
 Visit [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv).

## For Instructors

### Install requires

- python 3.6.0 or layer

- requests

- openpyxl

```
% pip install requests
% pip install openpyxl
```
### Generate ZIP file for your learners
 1. Clone this repository:
    ```
    % git clone https://github.com/mastnk/shipython
    ```
 1. (Optional) Edit the *KEY* in submit.py, where KEY is any code what you want like course number and year.
 1. (Optional) Specify the *URL* in dist/shipython/submit.py, where URL corresponds to the directory to be uploaded web.
 1. Zip files
     ```
     % cd dist
     % zip -r shipython.zip shipython
     ```
 1. Distribute **new** dist/shipython.zip to learners.

### Generate xlsx file to check learners' progress
 1. Solve all problems in dist/shiptyhon/
 1. Edit dist/IDs.txt, for example, you can put learner IDs line-by-line.
 1. Make xlsx file for checking.
    ```
    % cd dist
    % sh id2xls.sh
    ```
 1. Instructors can use the *check.xlsx* to check the progress of students.
 1. Distribute dist/shipython.zip to learners.
  
### Server setting (Optional)
 1. Upload all files in web/ and *check.xlsx* to the directory associated the *URL*.
 1. Change mode:
    ```
    sh chmod.sh
    ```
 1. Make sure file permissions and other settings.
 
 When the learners solve the problem, the *check.xlsx* would be automatically updated.
 The number of characters are counted and it also registerd in the *check.xlsx*. The minimum size of the code competition may be fun.
 If the code size is less than registered data, the data would be overwritten.

 Please download the *check.xlsx* to check the progress.
 
 The learners can also view their progress and the ranking of the code size competition by accesing the URL with their ID and the code of the first problem.

 
### Adding problems

 1. Prepare *hoge*.py and TEST/test*hoge*.py. 
 1. *hoge*.py should include:
    - ID = '01234'
    - def func
    - def sample( func )
 1. TEST/test*hoge*.py should include:
    - def check( func ) with several assert for test
    - sample:
       ```
       def check( func ):
           assert func( 3, 2 ) == 6, 'func( 3, 2 )'
           assert func( 3, 0 ) == 0, 'func( 3, 0 )'
       ```
 1. If you want to integrate your problems, please contact: [https://github.com/mastnk/shipython](https://github.com/mastnk/shipython)
 
# Problems

## Basic

1. **A00.py** : Multiply a and b.
1. **A01.py** : Calculate the sum of the list.
1. **A02.py** : Find the second largest value in the list.
1. **A03.py** : Calculate the sum of the ASCII code of each character.
1. **A04.py** : Replace four-character words starting with "F" or "f" by "****".
1. **A05.py** : Remove duplicate elements in the list.
1. **A06.py** : Remove unique elements in the list.
1. **A07.py** : Remove successive characters in the text.
1. **A08.py** : Rotate the list, where the right is positive direction.
1. **A09.py** : Encrypt the text by Caesar cipher.
1. **A10.py** : Find the second oldest person in dictionary.
1. **A11.py** : Calculate histgoram of frequency of characters in the text.
1. **A12.py** : Translate (row,colmun) to the excel-style cell identifier.
1. **A13.py** : Calculate days between two dates.
