### When to do the tests

#### Linting

Why “linting” important and why should we use it?
Linting helps to prevent bugs in our app. 
Linting makes you a better developer by helping write a better code (checking against coding standards)
Helps prevent things like syntax errors, typos, bad formatting, incorrect styling, etc
Saves your time as a developer
We are using Flake8 which is the wrapper which verifies pep8, pyflakes and circular complexity

**To run test:**

     `make lint`


### Unittest 
Test application functionality like supported outputs and text message output format.

**To run test:**

    `make test`

### Coverage test 
Coverage test measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not.

**To run test:**

    `make test_cov`

### Smoke test 

Smoke Testing is performed after application run to ascertain that the critical functionalities of the aplication are working fine. It is executed "before" any detailed functional or regression tests are executed on the software build. The purpose is to reject a badly broken application. Developer does not waste time installing and testing the software application.

**To run test:**

    `make test_smoke`
 
