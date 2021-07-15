from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields, marshal
from service import *
import json

app = Flask(__name__)
app.config['RESTPLUS_VALIDATE'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False

api = Api(app = app,
          version = "1.0",
          title = "Arabic named entity recognition",
          description = "Develope some models or algorithems to extract named entities")

ns = api.namespace('named_entity_recognition', description='extract up to 9 different types of entities: Person, Location, Organization, Nationality, Job, Product, Event, Time, Art-Work')

# define request payload json structure
req_info = {}
req_info['sentence'] = fields.String(required=True, example="تلقى تعليمه في الكتاب ثم انضم الى الأزهر عام 1873م. تعلم على يد السيد جمال الدين الأفغاني والشيخ محمد عب")

# define return payload json structure
req_info_model = api.model("req_info", req_info)
resp_info_model = api.model('resp_info', {
    'text': fields.String(),
    'entities': fields.Raw()})

entities_model = api.model("entityModel", {
        "type": fields.String(required=True, description=''),
        "entity": fields.String(required=True, description=''),
        "start_offset": fields.Integer(),
        "end_offset": fields.Integer()})



@ns.route("/")
class tagger(Resource):
    @ns.expect(req_info_model)
    @api.marshal_with(resp_info_model)

    def post(self):
        sentence = request.json['sentence']
        retV = {"text": sentence, "entities": self.get_entity()}
        return retV, 200

    def get_entity(self):
        sentence = request.json['sentence']
        result = json.loads(extractor(sentence))['entities']
        return marshal(result, entities_model)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3838)