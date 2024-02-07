## Sample Python Selenium Cucumber Framework

The tech stack used in this project are:
1. **Python** as the programming language for writing test code
2. **Cucumber** as the framework
3. **PIP3** as the build tool
4. **VSCode** as the preferred IDE for writing python code.

#### Getting Started
Setup your machine.
1. Python > 3.7 
2. Install VSCode & open the repo
3. On Terminal, navigate to repo and run following commands
    a. Create Virtual Env ```python3 -m venv behavex-env```
    b. Activate Virtual Env ```source behavex-env/bin/activate```
    c. Install Packages ```pip3 install -r requirements.txt```

#### Running tests
* Run tests in Sequence: ```browser=chrome behavex```
* Run tests in Parallel: ```browser=chrome behavex --parallel-processes 5 --tags @test```

#### Report
* Report will be found here: ```/output/report.html```
---

### Tests
1. **[TestCase-1](https://github.com/vinaykumarvvs/sample-selenium-python-cucumber-framework/blob/main/features/TestA.feature):** Heroku - FormAuthentication Cases
2. **[TestCase-2](https://github.com/vinaykumarvvs/sample-selenium-python-cucumber-framework/blob/main/features/TestB.feature):** Heroku - Drag And Drop Cases
