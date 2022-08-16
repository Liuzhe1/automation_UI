*** Settings ***
Library    Selenium2Library
*** Test Cases ***
Baidu search case
    open browser    http://www.baidu.com    chrome
    input text    css:#kw   123
    click button    css:#su
    sleep    5
    close browser


