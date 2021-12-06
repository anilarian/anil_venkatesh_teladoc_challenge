Feature: Automating webtable

  Scenario Outline: Add a user and validate the user has been added to the table
    Given Launch chrome browser
    When Web tables page is opened
    Then Add user f_name: "<f_name>" u_name: "<u_name>" ph_num: "<ph_num>" to the table
    Then Validate the user f_name: "<f_name>" has been added to the table
    Then close the browser
    Examples:
      | f_name | u_name | ph_num |
      | Anil   | anil   | 111111 |
      | Ryan   | ryan   | 333333 |
      | John   | john   | 444444 |

  Scenario Outline: Delete user User and validate user has been deleted
    Given Launch chrome browser
    When Web tables page is opened
    Then Add user f_name: "<f_name>" u_name: "<u_name>" ph_num: "<ph_num>" to the table
    Then Validate the user f_name: "<f_name>" has been added to the table
    Then Delete a User u_name: "<u_name>" from the table
    Then Validate the user u_name: "<u_name>" has been deleted
    Then Close the browser
    Examples:
      | f_name | u_name | ph_num |
      | Anil   | anil   | 111111 |
      | Ryan   | ryan   | 333333 |
      | John   | john   | 444444 |

  Scenario: Delete user User Novak and validate user has been deleted
    Given Launch chrome browser
    When Web tables page is opened
    Then Delete a User u_name: "novak" from the table
    Then Validate the user u_name: "novak" has been deleted
    Then Close the browser
