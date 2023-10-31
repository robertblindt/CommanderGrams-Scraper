from . import api
import requests

from app.processing import Processing

processor = Processing()

@api.route('/findcommanders/years', methods = ["GET"])
def find_commanders_year():
    # JSON Check
    # Check the website for all the commanders
    print('I got hit')
    card_retrieval_list = processor.parseEDHrec_for_commanders(1)
    # Loop to check if the commander needs to be scraped then scrapes it
    print(card_retrieval_list)
    for commander in card_retrieval_list:
        URL = 'https://commandergrams-api.onrender.com/api/commanders'
        payload = {'cardName': commander}
        r = requests.post(URL, json = payload, timeout=180)
        print(r)
    return {'message': len(card_retrieval_list)}


@api.route('/hi', methods = ["GET"])
def hi():
    print('hi')
    return {'message':'hi'}
