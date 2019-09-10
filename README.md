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

## For Instructors

### Install requires

- python 3.6.0 or layer

- requests

```
% pip install requests
```
### Instalation
 1. Clone this repository:
    ```
    % git clone https://github.com/mastnk/shipython
    ```
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

 1. Upload all files in web/ and *check.xlsx*.
 1. Make sure file permissions and other settings.
 1. Specify the *URL* in dist/shipython/submit.py.
 1. Zip files
     ```
     % cd dist
     % zip -r shipython.zip shipython
     ```
 1. Distribute **new** dist/shipython.zip to learners.
    Then, when learners submit the code, *check.xlsx* is automatically updated.
 
 ## Adding problems

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
 1. If you added some problems, the learner should specify *--dev* option to submit:
    ```
    % python submit.py --dev hoge.py
    ```
 1. For making the xls file, please use the the following commands:
    ```
    % cd dist
    % sh id2xls.sh --dev
    ```
    Note that the checking code is different with and without the *--dev* option.
 
# Problems

1. **A00.py** : Multiply a and b.
1. **A01.py** : Calculate the sum of the list.
1. **A02.py** : Find the second largest value in the list.
1. **A03.py** : Calculate the sum of the ASCII code of each character.
1. **A04.py** : Replace four-character word starting with "F" or "f" by "****".
