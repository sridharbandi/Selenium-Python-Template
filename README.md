## Selenium Python Template with UNITTEST to getting started with

To automate [Selenium Webdriver](https://docs.seleniumhq.org/projects/webdriver/) binaries management in runtime am using [webdrivermanager](https://github.com/SergeyPirogov/webdriver_manager), an excellent library by [Serhii Pirohov](https://github.com/SergeyPirogov)

### How to use?
Create the Page Objects of your Web application under **_pageobjects_** package and call those Page Objects in your  unittests under **_tests_** package (Sample Page Objects, testcase included in this template)

### Install
To install the required dependencies issue the below command in project root directory
```javascript
pip3 install -r requirements.txt
```

### How to run?
Issue the below commands in project root directory

```javascript
python tests/RunTest.py
```
By default it runs in Chrome browser, you can specify which browser to use as well
```javascript
python tests/RunTest.py --browser=firefox
```

Currently supported browsers are
* chrome
* firefox
* edge
* ie

> Feel free to modify it to your own needs :)