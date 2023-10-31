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
    upadate_count = 0
    for commander in card_retrieval_list:
        URL = 'https://commandergrams-api.onrender.com/api/commanders'
        payload = {'cardName': commander}
        r = requests.post(URL, json = payload, timeout=180)
        if r.json().get('data'):
            card_retrieval_list = processor.parseEDHrec_for_card_names(commander)
            if card_retrieval_list:
                #print(card_retrieval_list)
                URL = 'https://commandergrams-api.onrender.com/api/insertcommander'
                payload = {'card_list': list(card_retrieval_list), 'commander': commander}
                r = requests.post(URL, json = payload, timeout=180)
                upadate_count += 1
    return {'message': f"Year page scraped.  {upadate_count} Commanders added or updated"}

@api.route('/findcommanders/month', methods = ["GET"])
def find_commanders_month():
    # JSON Check
    # Check the website for all the commanders
    print('I got hit')
    card_retrieval_list = processor.parseEDHrec_for_commanders(2)
    # Loop to check if the commander needs to be scraped then scrapes it
    print(card_retrieval_list)
    upadate_count = 0
    for commander in card_retrieval_list:
        URL = 'https://commandergrams-api.onrender.com/api/commanders'
        payload = {'cardName': commander}
        r = requests.post(URL, json = payload, timeout=180)
        if r.json().get('data'):
            card_retrieval_list = processor.parseEDHrec_for_card_names(commander)
            if card_retrieval_list:
                #print(card_retrieval_list)
                URL = 'https://commandergrams-api.onrender.com/api/insertcommander'
                payload = {'card_list': list(card_retrieval_list), 'commander': commander}
                r = requests.post(URL, json = payload, timeout=180)
                upadate_count += 1
    return {'message': f"Month page scraped.  {upadate_count} Commanders added or updated"}

@api.route('/findcommanders/week', methods = ["GET"])
def find_commanders_week():
    # JSON Check
    # Check the website for all the commanders
    print('I got hit')
    card_retrieval_list = processor.parseEDHrec_for_commanders(3)
    # Loop to check if the commander needs to be scraped then scrapes it
    print(card_retrieval_list)
    upadate_count = 0
    for commander in card_retrieval_list:
        URL = 'https://commandergrams-api.onrender.com/api/commanders'
        payload = {'cardName': commander}
        r = requests.post(URL, json = payload, timeout=180)
        if r.json().get('data'):
            card_retrieval_list = processor.parseEDHrec_for_card_names(commander)
            if card_retrieval_list:
                #print(card_retrieval_list)
                URL = 'https://commandergrams-api.onrender.com/api/insertcommander'
                payload = {'card_list': list(card_retrieval_list), 'commander': commander}
                r = requests.post(URL, json = payload, timeout=180)
                upadate_count += 1
    return {'message': f"Week page scraped.  {upadate_count} Commanders added or updated"}


@api.route('/hi', methods = ["GET"])
def hi():
    print('hi')
    return {'message':'hi'}
