from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from transformers import AutoTokenizer, AutoModelForCausalLM


app = Flask(__name__)
api = Api(app)

# Can change models - just picked a popular small instruct model
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

persistent_text = ""

class TextString(Resource):
    
    # Currently just takes the input text and feeds it to LLM for a reply. Returns reply
    def get(self):
        input_text = persistent_text
        print(input_text)
        input_ids = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(
            **input_ids,
            max_new_tokens=20
        )
        output_text = tokenizer.decode(outputs[0])
        print(output_text)
        # output_text = input_text
        return {"Output": output_text}

    # Post some text to endpoint, it gets saved for processing
    def post(self):
        global persistent_text
        data = request.get_json()
        persistent_text = data.get("text")

        if persistent_text:
            return {"message": persistent_text}, 200
        else:
            return {"message": "No text provided"}, 400


api.add_resource(TextString, "/")

if __name__ == "__main__":
    app.run(debug=True)
