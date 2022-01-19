*** Settings ***
Documentation           The file contains argumanets passed when executing the tests
Library                 ../custom_lib/Global_Variable.py

*** Variables ***
${envrionment}          load
${db_url}
${source_db}
${db_user_name}
${db_passowrd_load}


*** Keyword ***
Set Global Variables based on the environment
    [Arguments]         ${envrionment}




