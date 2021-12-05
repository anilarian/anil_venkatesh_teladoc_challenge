Feature: Automating webtable
  Scenario: Add a user and validate the user has been added to the table
    Given Launch chrome browser
    When Webtables page is opened
    Then Add users to the table
    Then Validate the user has been added to the table
    Then close the browser
    
#  Scenario: Delete user User Name:  and validate user has been delete
#    Given Launch chrome browser
#    When Webtables page is opened
#    Then Delete a User
#    And Validate the user has been deleted
#    And Close the browser