# Setting up open ai compatible api for bedrock in openweb ui:
Openweb ui only accepts api's that are openai compatible. So, we need to convert the bedrock model to openai compatible model. \
This notebook will guide you through the process of converting bedrock model to openai compatible model.

## set up the openai compatible api for bedrock in openweb ui:
https://github.com/aws-samples/bedrock-access-gateway/tree/main?tab=readme-ov-file#deployment

Tried Step1 and Step2 and it works like a charm.

## Run openweb ui:
Run the openweb ui and you run the following steps:
- click on the profile icon on the top right corner of the screen.
- click on the settings option -> Admin settings -> connections -> Manage OpenAI connections
- Add the api key(FROM WHAT YOU MADE IN STEP 1 ABOVE) and the endpoint (from cloudformation OUTPUTS TAB)
