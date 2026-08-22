# Flight Deal Finder

A Python flight-deal alert system built as part of Angela Yu's 100 Days of Code — Day 39 & Day 40.

The idea is simple:

Find flights cheaper than a user's desired price and automatically send them an email alert.

What started as a straightforward flight-search project turned into a pretty interesting debugging journey involving APIs, Google Sheets, IATA codes, flight-data parsing, and automated email notifications.

## What It Does

Reads destination cities and target prices from Google Sheets.
Finds the IATA airport code for each destination.
Writes the IATA codes back to the spreadsheet.
Searches for flights from Lahore (LHE) using Google Flights data through SerpAPI.
Searches for a one-week trip beginning one week from the current date.
Compares the returned flight price with the user's desired price.
Sends an email when a flight is available at or below the desired price.

For the user-facing version, users can submit their information through a Google Form, allowing the program to send flight alerts to the people who signed up rather than only to the developer.

## Project Flow


                 Google Form
                      │
                      ▼
                Google Sheet
                      │
                      ▼
              Sheety API
                      │
                      ▼
              Destination Cities
                      │
                      ▼
             IATA Code Lookup
                      │
                      ▼
                Flight Search
                 (SerpAPI)
                      │
                      ▼
                Flight Price
                      │
              ┌───────┴───────┐
              │               │
        Price <= Target?      No
              │               │
             Yes              │
              │               │
              ▼               ▼
        Send Email          Nothing
### Technologies Used
Python
SerpAPI — flight search / Google Flights data
Google Sheets — storing destinations, prices, and user information
Sheety API — interacting with Google Sheets through HTTP requests
airportsdata — looking up IATA airport codes

### Some of the Challenges

This project was definitely not a straight line from tutorial to finished program.

Amadeus API

The original project used the Amadeus Flight Offers API.

However, the Amadeus developer setup available to me wasn't usable for this project, so I had to find another way to search for flights.

That led me to SerpAPI and Google Flights.

SerpAPI Response Structure

Google Flights data wasn't always returned in the same convenient structure.

Sometimes the response contained:

best_flights

Sometimes:

other_flights

And sometimes neither contained usable flight data.

This meant I had to inspect the actual API responses instead of assuming every destination would return the same structure.

### Edge Cases

Some destinations didn't behave nicely with the flight API.

Paris and New York, for example, exposed problems with the way flight results were being returned.

Rather than endlessly expanding the project into a full flight-search engine, the current version focuses on getting the core workflow functional.

That is intentional.

SMTP / email — sending flight alerts
Google Forms — collecting users for the alert system
dotenv / environment variables — keeping API credentials out of the source code
🎯 What I Learned

This project taught me much more than just how to call an API.

I learned how to:

work with multiple APIs in one application
consume and inspect JSON responses
deal with inconsistent API response structures
use Google Sheets as a lightweight database
update spreadsheet records programmatically
work with IATA airport codes
compare API data against user-defined values
automate email notifications
manage API credentials with environment variables
debug real-world API failures
handle situations where the original API/service isn't available
turn a personal script into a basic user-facing workflow

Most importantly, I learned that real-world programming rarely looks like the clean example in a tutorial.

Sometimes the API doesn't return what you expect.

Sometimes the service you planned to use isn't available.

Sometimes a perfectly reasonable piece of code suddenly throws a KeyError.

And sometimes you spend way too long staring at a JSON response wondering what the hell you're supposed to do with it. 😂

The important part is learning how to keep moving.

🏁 Final Result

The finished project successfully performs the complete workflow:

User / Destination Data
        ↓
Google Sheets
        ↓
Sheety
        ↓
IATA Lookup
        ↓
SerpAPI Flight Search
        ↓
Price Comparison
        ↓
Email Notification

And the final test wasn't just a print() statement.

Actual email alerts were successfully delivered to test email addresses. 

## Possible Future Improvements

The current project is intentionally simple, but it could eventually be expanded with:

multiple departure airports
more flexible travel dates
user-specific destinations
user-specific currencies
user-specific price limits
better handling of multiple airports per city
better handling of layovers
more robust flight-result parsing
duplicate-alert prevention
a proper database instead of Google Sheets
a web interface for user registration

For now, though, the goal was achieved:

A working automated flight-deal alert system built with Python.

### Part of 100 Days of Code

Angela Yu — 100 Days of Code: The Complete Python Pro Bootcamp

Day 39–40: Flight Deal Finder

Built, debugged, adapted, and finally made functional. 💻✈️🔥

Project status: COMPLETE ✅
