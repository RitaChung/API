from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields
from service import *

app = Flask(__name__)
app.config['RESTPLUS_VALIDATE'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False

api = Api(app = app,
          version = "1.0",
          title = "Arabic text analyses",
          description = "Develope some models or algorithems to analysis arabic text")

ns = api.namespace('sentence_embedding', description='convert sentence into 512 dims vector, supported languages: Arabic, Chinese, Dutch, English, French, German, Italian, Korean, Polish, Portuguese, Russian, Spanish, Turkish')



# define request payload json structure
req_info = {}
req_info['sentence'] = fields.String(required = True, example = "الأمين العام للأمم المتحدة يقول إنه لا يوجد حل عسكري في سوريا.")

# define return payload json structure
req_info_model = api.model("req_info", req_info)
resp_info_model = api.model('resp_info', {'embeddingVector': fields.List(fields.Float())})


@ns.route("/")
class convert2Embedding(Resource):
    @ns.expect(req_info_model)
    @api.marshal_with(resp_info_model)
    def post(self):
        global current_algorithm,model
        sentence = request.json['sentence']
        result = sentence2vector([sentence])
        retV = {"embeddingVector": result[0].tolist()}
        return retV, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)