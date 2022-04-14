# CS240 Notes: Software as a Service

## What makes SaaS different from just software?

- SaaS is (centrally) hosted - available, on-demand
- Usually accessed via a "thin client"
  - Web browser
  - Generic app framework
- pay-per-use or licensed

## What features differentiate SaaS from PaaS?

- PaaS is accessed via APIs.
- PaaS is usually targeted to a technical audience.
- SaaS is usually fully managed.
  - End user is always up to date.

## Illinois SaaS Tools

- class management system: Canvas, Moodle, PrairieLearn
- Safer Illinois
- Self Service
- Queue
- Shibboleth (Auth Service)- PaaS and SaaS
- \*Lib Joural Access
- \*FastX
- GitHub
- Campuswire
- Bus System App
- Media Space
- \*Adobe Creative Cloud
- Google Suite/Drive, Office 365
- Scheduling/Doodle
- Zoom
- Discord
- Slack
- ALL Social Media

Most consumer facing tools are SaaS

## Architectural Layers of Software

- Frontend
  - Presentation to the end user
  - How it looks
  - How the data is displayed
- Backend
  - data storage
  - compute business logic
  - 3rd party services
  - Not concerned with user access
- Middleware
  - Provide an abstraction for communication between the frontend and the backend
  - Provide user specific functionality
  - Validate authentication

## Software Study: Coin Flip

- Microservice based (multiple app.py files)
  - Have to launch all app
- 20/app.py
  - HTTP GET /\<sid\>
  - HTTP GET /\<sid\>/play
- 20/illiniCoinService/app.py
  - HTTP GET /\<sid\>
  - HTTP POST /\<sid\>/change
- 20/coinFlipService/app.py
  - HTTP GET /

## Architectural Layers Comparison

- Frontend
  - Middleware may be slow - how should the user see progress? (Spinners)
  - User may have slow or no internet
- Middleware
  - Security/Bad Input from the user
  - Provide safe fallbacks when backends are unavailable
- Backend
  - Compute business logic
  - Scale with requests

## Common Technologies

- Backend
  - Lower level
  - C/C++/Go/Rust/Python/Java/C#
- Middleware
  - flask -> python
  - express -> javascript
  - Spring -> java
- Frontend
  - Web
    - Javascript
  - Mobile
    - Dart/Flutter
    - Android native: Java
    - iOS native: Swift
