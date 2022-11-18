*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username   joonatan
    Set Password   jonttu123
    Confirm Password  jonttu123
    Submit Credentials
    Register Should Succeed

Register With Too Short Usename And Valid Password
    Set Username   j
    Set Password   jonttu123
    Confirm Password  jonttu123
    Submit Credentials
    Register Should Fail With Message  Username can contain only letters a-z and must have at least 3 characters
    
Register With Valid Username And Too Short Password
    Set Username   joonatan
    Set Password   j123
    Confirm Password  j123
    Submit Credentials
    Register Should Fail With Message  Password can not contain only letters and must have at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username   joonatan
    Set Password   jonttu123
    Confirm Password  jonttu321
    Submit Credentials
    Register Should Fail With Message  Nonmatching passwords

Login After Successful Registration
    Go To Login Page
    Set Username   joonatan
    Set Password   jonttu123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username   j
    Set Password   jonttu123
    Submit Login Credentials
    Login should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}