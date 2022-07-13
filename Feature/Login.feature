Feature: verify the login using data driven testing

  Scenario Outline: verify the login with different set of user login details
    Given user in the login page
    When user enter username as "<user>" and password is "<pwd>"
    When user click on login
    Then user will verify the title of the page

    Examples:
      | user       |  | pwd        |
      | shrinisen  |  | Sr23ss23@  |
      | rajnish7kr |  | Kr7rajnish |