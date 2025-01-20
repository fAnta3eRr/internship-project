
Feature: Test for Main Page

  Scenario: User can filter the off plan products by Unit price range
    When Open the main page
    Then Input fanta3er.yu@gmail.com and fantazer120393 to Log in to the page
    Then Click on Off-plan at the left side menu
    And Verify the right page opens
    And Click the Filters button in the top right corner
    Then Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)