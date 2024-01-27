Feature: Heroku - FormAuthentication Cases

  @test
  Scenario: Success Login FormAuthentication Case
   Given user navigates to HerokuMainPage
   When user on HerokuMainPage clicks on Form Authentication
   When user on FormAuthenticationLoginPage enter username as "tomsmith" and password as "SuperSecretPassword!"
   When user on FormAuthenticationLoginPage clicks on login
   Then user on FormAuthenticationSuccessPage verifies this message "Secure Area"
   When user on FormAuthenticationSuccessPage clicks on logout
   Then user on FormAuthenticationLoginPage verifies this message "Login Page"

  @test
  Scenario: Validate Error Message When Invalid UserName is Passed
   Given user navigates to HerokuMainPage
   When user on HerokuMainPage clicks on Form Authentication
   When user on FormAuthenticationLoginPage enter username as "admin" and password as "SuperSecretPassword!"
   When user on FormAuthenticationLoginPage clicks on login
   Then user on FormAuthenticationLoginPage verifies the error message as "Your username is invalid!"

  @test
  Scenario: Validate Error Message When Invalid Password is Passed
   Given user navigates to HerokuMainPage
   When user on HerokuMainPage clicks on Form Authentication
   When user on FormAuthenticationLoginPage enter username as "tomsmith" and password as "admin"
   When user on FormAuthenticationLoginPage clicks on login
   Then user on FormAuthenticationLoginPage verifies the error message as "Your password is invalid!"