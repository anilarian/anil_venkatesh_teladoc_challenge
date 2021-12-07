# TELADOC CODING CHALLANGE

**Recieved instructions**

Using an automation framework of your choice. 

Share a repository with your coding challenge (You should be able to set up a free account on github, bitbucket, sourceforge, etc. to share your coding challenge.)
* Name it with your "firstname_lastname_teladoc_challenge"
* Update your README to show how to run your scripts
* Fulfill the following two scenarios:
* Feature: As an Engr. Candidate I need to automate http://www.way2automation.com/angularjs-protractor/webtables/ So I can show my awesome automation skills
  - Scenario: Add a user and validate the user has been added to the table
  - Scenario: Delete user User Name: novak and validate user has been delete


## Environment Setup (on Mac):

* Install behave on your system using pip - 
    *pip install behave*

* Install selenium on your system using pip - 
    *pip install selenium*
    
* Install chromedriver on your system using homebrew (This is automatically adds the driver to path) - 
    *brew install chromedriver*
    
## Execution automation scenarios:

* Navigate to tdoc_interview_feature
    *cd tdoc_interview_feature* 
    
* Please, refer to the following module for the different automation scenarios.
    *tdoc_interview_feature/features/webtabbles_automation.feature*
    
* Please, refer to the following module for Page Object Models used to interact with the web page.
    *tdoc_interview_feature/pages/*
    
* Please, refer to the following module for Feature steps.
    *tdoc_interview_feature/features/steps

* Executing the feature automation using behave.
    *behave tdoc_interview_feature/features/webtabbles_automation.feature*
    
## Further improvements

* Setup driver as a fixture instead of using **Given.
* Extend user addition to validate all fields of the user being added.
* Improve error handling and edge cases.
* Implement unit tests
* Improve logging
* This is the first project where I'm learning to use both behave & selenium for web automation. Will defenitely continue learning more about these tools regardless.

## Thank you
