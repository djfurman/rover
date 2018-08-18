Feature: It fetches API data from GitHub

    Scenario: Get basic user information from GitHub

       Given GitHub user "djfurman"
       When rover fetches the data
       Then that status code should be "200"
       and a json object should be returned
       and login should equal the github user
