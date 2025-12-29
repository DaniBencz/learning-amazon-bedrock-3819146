#Imports
import json
import boto3

#Create the bedrock client
bedrock = boto3.client('bedrock-runtime')

#Setting the prompt
prompt_data = """Translate the following English text to French: 'Hello, how are you today?'

Translation:
"""

#Model specification
modelId = 'amazon.titan-text-express-v1'
accept = 'application/json'
contentType = 'application/json'

#Configuring parameters to invoke the model
body = json.dumps({
  "inputText": prompt_data,
  "textGenerationConfig": {
    "maxTokenCount": 1000,
    # "temperature": 0.5,
    # "topP": 0.9
  }
})

#Invoke the model
response = bedrock.invoke_model(
  modelId=modelId,
  body=body,
  accept=accept,
  contentType=contentType
)

#Parsing and displaying the output
response_body = json.loads(response.get('body').read())
output = response_body.get('results')[0].get('outputText')
print("Model Output:\n", output)
