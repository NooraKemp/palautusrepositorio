*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  joonatan  joonatan123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  noora  joonatan123
    Output Should Contain  Username is already taken 

Register With Too Short Username And Valid Password
    Input Credentials  jo  joonatan123
    Output Should Contain  Username can contain only letters a-z and must have at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  joonatan  j123
    Output Should Contain   Password can not contain only letters and must have at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  joonatan  joonatan
    Output Should Contain   Password can not contain only letters and must have at least 8 characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  noora  noora123