Feature: Test Scenarios for Login Target step

  Scenario: Developer checking the login functionality
    Given Open Target main page
    And Target Signin button pressed
    And Target Signin button popup
    And Target input credentials
    And Click sign in user
    Then Verify the account
    Given Verify the name
    Then Verify the URL

