# CommanderGrams Scraper
#### Unhosted but Dockerized
This project contains the Flask Scraper App that scrapes EDHrec.com for the CommanderGrams project.  The Frontend portion of this project can be [found here](https://github.com/robertblindt/CommanderGrams-Frontend), and the backend can be [found here](https://github.com/robertblindt/CommanderGrams-Backend).
#### Full App Running at: https://commandergrams.netlify.app/

## Installation 
Currently this project is not hosted, however I tried to get it running on AWS ECS. The Dockerization is fully functionally locally, but I could not get the backend to display publicly for some reason.  The administrative process can still be run locally in a docker container, and I reverted the changes back to work that way.

**Clone this repository, then add the file ```.env``` to the root directory.  In that file, paste in:**
```
FLASK_RUN_HOST="0.0.0.0"
```
This reroutes the flask app to run on the internal port for the docker container. 

**With Docker already installed on your system run:**
```
docker build -t cgram_scraper:1.0 .
docker run -p 5000:5000 cgram_scraper:1.0
```
At this point, you should be able to run the scraper locally!

If you want to work on your own database, in the routes in templates, towards the bottom you will see a variables `URL` which points to my hosted API on Render.  Just point that at your own API and it should work fine.

## Project Overview
This project is pretty simple.  Due to the amount or ram Chrome needs to run, I needed to separate this from the rest of the project. Additionally, installing Chrome is very different from installing an NLP core on a server, so I only needed to dockerize the scraper part.
- Used Flask to trigger Selenium scrape of EDHrec page
    - Due to page being dynamic couldn't use requests package.
        - Also needed to scroll down the page once it loaded to load in the assets to get the list of cards that I wanted to see.
    - Returns a list in json form to the requests package to trigger the commander insert in the backend project

### Methodology
When the page that I was looking to scrape loads, you see an image of each card that is related to the card I am scraping in relation to.  Once loaded, I grab the name from the div that contains the image.

## Future Improvements
- Create some automation scripts
    - Automate collecting 'all the commanders' to start off.
        - There are 1,150ish unique singular commanders, and finding them all should be pretty easy with Scryfall.
        - Finding commander pairs isn't exactly supported right now.
    - New cards get added every month or so, so I should be scraping every month or two.

- Get this hosted with AWS ECS
    - I was trying to do it before, but in the short term its not really that much of a deal to get the POC started on my own system.
    - The docker container works, I just couldn't get the instance to be public.