from . import api
from flask import request
from app.processing import Processing

processor = Processing()

@api.route('/findcommander', methods = ["POST"])
def commander_search():
    # JSON Check
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    data = request.json
    required_fields = ['commander']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    # return data.get('commander')
    card_retrieval_list = processor.parseEDHrec_for_card_names(data.get('commander'))
    if card_retrieval_list:
        processor.edhrec_list_db_check_and_retrieve(card_retrieval_list, data.get('commander'))
        # print(form.commander.data)
        processor.find_meaning(data.get('commander'))
        return {'message':'Commander has been added or updated!'}
    return {'error':'Either the commander has already been scraped, or the name is misspelled!'}
