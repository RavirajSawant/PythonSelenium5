Feature: Find Flights for 1 person business class

  Scenario: Book a flight from Hyd to Pune(one way)
    Given User user is on search page
    When user selects Hyderabad as a Origin
    When User user selects Pune as a Destination
    When user select today date from the Departure
    When user select Business class from the Travellers field
    When User clicks on the Search button
    Then user flights are presented on the search result page
    Then User capture the result screenshot and save in the project folder