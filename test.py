import numpy as np
import json
import boto3
import os

# from fuzzywuzzy import fuzz
from dotenv import load_dotenv
from botocore.exceptions import ClientError
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client_groq = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

client_aws = boto3.client(
    "bedrock-runtime",
    region_name="us-west-2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_PERSONAL"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY_PERSONAL"),
)

chat_completion = client_groq.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="llama-3.1-70b-versatile",
)
#print("GROQ:", chat_completion.choices[0].message.content)


def call_aws_bedrock(user_prompt, model_id="meta.llama3-1-70b-instruct-v1:0"):
    system_prompt = "You are a useful assistant"
    formatted_prompt = f"""
	<|begin_of_text|>
	<|start_header_id|>system<|end_header_id|>
	{system_prompt}
	<|start_header_id|>user<|end_header_id|>
	{user_prompt}
	<|eot_id|>
	<|start_header_id|>assistant<|end_header_id|>
	"""

    native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 2048,
        "temperature": 0.0,
    }
    request = json.dumps(native_request)

    try:
        # Invoke the model with the request.
        response = client_aws.invoke_model(
            modelId=model_id, body=request, contentType="application/json"
        )

        # Decode the response body.
        model_response = json.loads(response["body"].read())
        response_text = model_response["generation"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can"t invoke "{model_id}". Reason: {e}")


print("AWS:", call_aws_bedrock("Explain the importance of low latency LLMs"))

table = {
    "rows": [
        {
            "no": 1,
            "topic": "20 Day to Close Automation Issues",
            "count": 4,
            "description": "(1) Timestamp: 2024-06-13T16:01:19Z > Visitor said "my 20 day to close automation is not working"\n(2) Timestamp: 2024-06-13T16:08:18Z > Visitor said "I this that automation has the quote link in there and yesterday we have the call ahead automation that was not working and it was because of a link that was in the text message"\n(3) Timestamp: 2024-06-13T16:08:34Z > Visitor said "I think is the same issue"",
            "status": "No Article Found",
        },
        {
            "no": 2,
            "topic": "Newsletter Automation Issues",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-13T16:04:59Z > Visitor said "also we had an automation for Monthly newsletters  but i can not see it to turn it on"\n(2) Timestamp: 2024-06-13T16:12:05Z > Visitor said "sound like a plan what about the newsletter ?"\n(3) Timestamp: 2024-06-13T16:12:25Z > Visitor said "I already have all the documents ready to go"\n(4) Timestamp: 2024-06-13T16:12:44Z > Visitor said "can you turn it on?"",
            "status": "No Article Found",
        },
        {
            "no": 3,
            "topic": "SimpleGrowth Form Issues",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-12T18:49:58Z > Visitor said "Hello! We\"re having a problem with a SimpleGrowth form"\n(2) Timestamp: 2024-06-12T18:51:21Z > Visitor said "So it this form: 20. Sales - SimpleGrowth Credit Card Update V3 Form : Marketplace (3/2/2022 5:53 PM)"\n(3) Timestamp: 2024-06-12T18:51:43Z > Visitor said "Seems like people are struggling with it. The status we are getting is Error, which I\"ve never seen before"",
            "status": "No Article Found",
        },
        {
            "no": 4,
            "topic": "Email Upsell Setup",
            "count": 1,
            "description": "(2024-06-11 16:19:56) Visitor 85005647: Hi guys,  Benjamin here.  I"ve updated the email for the upsell that"s set to out tomorrow.  Here"s a link to the document.  The first email already went out.  The second one is written, and the third one hasn"t been written yet.  Can we get this set up so it sends tomorrow?",
            "status": "No Article Found",
        },
        {
            "no": 5,
            "topic": "SimpleEstimate Plugin Usage",
            "count": 1,
            "description": "(2024-06-11 14:22:18) Visitor 56495582: We just signed up with SimpleEstimate.  Our goal was for our sales team to use this system from a desktop to measure lawns.  I do not see how to do this from https://app.simpleestimatesystems.com/home",
            "status": "No Article Found",
        },
        {
            "no": 6,
            "topic": "Private Automations Calendar/View",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-10T20:55:28Z > Visitor said "For the private automations, is there a calendar for that or a way I can view those somehow? Or can you send me them so I can add them to ur company calendar?"",
            "status": "No Article Found",
        },
        {
            "no": 7,
            "topic": "Text Automations Not Going Out",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-10T20:35:28Z > Visitor said "We are experiencing an issue with our text automations not going out. not sending text messages or follow-ups."",
            "status": "No Article Found",
        },
        {
            "no": 8,
            "topic": "Failed to Deliver Message Error",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-10T20:49:19Z > Visitor said "why would that happen when the client has gone through the steps to opt in to receive text messages?"",
            "status": "No Article Found",
        },
        {
            "no": 9,
            "topic": "Report of clients with credit cards on file",
            "count": 1,
            "description": "Timestamp: 2024-06-07T15:05:15Z > Visitor said "Do you know if it\"s possible to run a report of who has a credit card on file?"",
            "status": "No Article Found",
        },
        {
            "no": 10,
            "topic": "SA opt-in two way texting",
            "count": 1,
            "description": "Timestamp: 2024-06-07T13:51:11Z > Visitor said "I need some help with the SA opt-in two way texting. I have some questions. Can you help with that?"",
            "status": "No Article Found",
        },
        {
            "no": 11,
            "topic": "Delaying the two text form email",
            "count": 1,
            "description": "Timestamp: 2024-06-07T13:51:11Z > Visitor said "Is there a way to delay the two text form email to be sent maybe 2 days later?"",
            "status": "No Article Found",
        },
        {
            "no": 12,
            "topic": "Lost Connection and Resending Links",
            "count": 1,
            "description": "Timestamp: 2024-06-04T21:19:57Z > Visitor said "Sorry! a lost my connection before save the links. can you resend it, please? I have the Admin for the website waiting for this today."",
            "status": "No Article Found",
        },
        {
            "no": 13,
            "topic": "Editing Recurring Services",
            "count": 1,
            "description": "Timestamp: 2024-06-04T20:21:14Z > Visitor said "I have to edit these recurring services and sent to you by tomorrow."",
            "status": "No Article Found",
        },
        {
            "no": 14,
            "topic": "Lead Capture Form Integration",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T19:44:32Z > Visitor said "I need to add the lead capture on my websites. how this is done? do i need to hava a link for that?"",
            "status": "Article Found: https://help.simplegrowthsystems.com/hc/en-us/articles/7763164580884-How-to-add-a-V3-Website-Lead-Capture-Form-to-Website",
        },
        {
            "no": 15,
            "topic": "SimpleEstimate Tool Integration with CRM (Go High Level)",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:24:31Z > Visitor said "I just want to know how can I integrate the form with a CRM (Go High Level)"",
            "status": "No Article Found",
        },
        {
            "no": 16,
            "topic": "SimpleEstimate Tool Customization",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:24:31Z > Visitor said "some changes in the fields of the form."",
            "status": "No Article Found",
        },
        {
            "no": 17,
            "topic": "SimpleEstimate Tool Placement on Website",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:24:31Z > Visitor said "how the form is placed on the website?"",
            "status": "No Article Found",
        },
        {
            "no": 18,
            "topic": "SimpleEstimate Tool Authorization and Security",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:24:31Z > Visitor said "I\"m logged into the account already"",
            "status": "No Article Found",
        },
        {
            "no": 19,
            "topic": "SimpleEstimate Tool Tutorials and Guidance",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:24:31Z > Visitor said "Any tutorials that can help me with understanding the things?"",
            "status": "No Article Found",
        },
        {
            "no": 20,
            "topic": "Welcome and Follow-up Automation Configuration",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T19:44:32Z > Visitor said "For Welcome and Follow-up automations we would need the service names for which you want the follow-up emails to be sent out to turn the automation Live."",
            "status": "No Article Found",
        },
        {
            "no": 21,
            "topic": "SA Mobile App Texting Issues",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-04T16:07:55Z > Visitor said "On the subject of texting, do you know if it actually works to text clients from the SA mobile app? I\"ve tested it and the app says the text was sent successfully, but I have not received the text on my personal cell #."",
            "status": "No Article Found",
        },
        {
            "no": 22,
            "topic": "NPS Survey Issues",
            "count": 1,
            "description": "(1) Timestamp: 2024-06-03T19:37:08Z > Visitor said "Hey, Benjamin here.  Is there a way to send a one-off NPS survey?  I\"d like to send one to myself to see how it works.  We have a client that says the link isn\"t working for her, but I clicked the link in her email and it came right up."",
            "status": "No Article Found",
        },
        {
            "no": 23,
            "topic": "Upsell Automation Issues",
            "count": 1,
            "description": "(2024-05-31 13:48:54) Visitor 97273439: Good morning!  Benjamin Lawn here.  Just following up on the upsell that we were figuring out yesterday.",
            "status": "No Article Found",
        },
        {
            "no": 24,
            "topic": "Logo Upload Issues",
            "count": 1,
            "description": "(2024-05-31 12:45:25) Visitor 80089582: Need help uploading my logo to my landing page",
            "status": "No Article Found",
        },
        {
            "no": 25,
            "topic": "Logo Upload for Landing Page",
            "count": 1,
            "description": "(2024-05-31 12:43:47) Visitor 16500958: How can I upload my Logo for my landing page?   I don"t currently have a website.",
            "status": "No Article Found",
        },
        {
            "no": 26,
            "topic": "Upsell Request",
            "count": 1,
            "description": "(2024-05-30 20:05:44) Visitor 25859099: Hi there,  Benjamin Lawn here.  I just emailed, but I wanted to see if we could get an upsell to start tomorrow.",
            "status": "No Article Found",
        },
        {
            "no": 27,
            "topic": "Upsell Configuration",
            "count": 1,
            "description": "(2024-05-30 20:15:31) Dave Miller: We see you have Spring Fertilization and Fall Fertilization Upsell, may I know which upsell do you want these for?",
            "status": "No Article Found",
        },
        {
            "no": 28,
            "topic": "Customized Upsell Configuration",
            "count": 1,
            "description": "(2024-05-30 20:49:06) Dave Miller: I have checked with our development team, we can get a customized upsell configured but we requested at least 24 hours notice.",
            "status": "No Article Found",
        },
        {
            "no": 29,
            "topic": "Inactive Upsell",
            "count": 1,
            "description": "(2024-05-30 20:51:39) Visitor 25859099: I had an inactive upsell called Leaf Removal, but I think it was removed earlier this week.",
            "status": "No Article Found",
        },
        {
            "no": 30,
            "topic": "Working Hours",
            "count": 1,
            "description": "(2024-05-30 20:55:02) Visitor 25859099: Thanks so much!  BTW, what are your hours?",
            "status": "No Article Found",
        },
        {
            "no": 31,
            "topic": "Text Consent Automation Issues",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-30T17:38:00Z > Visitor said \"I turned off the text consent automation to make some updates to our email & form first. Now I"m ready to turn it back on. Do I ONLY need to toggle the red switch in the top right corner, or also the ones that say "Wait until 12pm" and "Send Text Opt-In Email + Form"?\"",
            "status": "No Article Found",
        },
        {
            "no": 32,
            "topic": "Upsell Setup",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-29T19:17:54Z > Visitor said "I know it\"s getting kind of late in the day, but is there time to set up an upsell to go out tomorrow?"",
            "status": "No Article Found",
        },
        {
            "no": 33,
            "topic": "Upsell Campaign Setup",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-28T16:40:07Z > Visitor said "Hey there!  Benjamin here.  Would it be possible to get an upsell campaign geared up and ready to start tomorrow?  Here\"s a document with all the details.  Thank you!"",
            "status": "No Article Found",
        },
        {
            "no": 34,
            "topic": "Text Op-In Assistant in SA Marketplace",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-24T16:26:14Z > Visitor said "I have questions about the Text Op-In Assistant in SA Marketplace"",
            "status": "No Article Found",
        },
        {
            "no": 35,
            "topic": "Managing Incoming Texts from SA",
            "count": 1,
            "description": "Timestamp: 2024-05-21T21:58:00Z > Visitor said "We signed up for 2-way texting through SA so we could send texts as part of the 20-DTC automations.  The problem is, managing incoming texts from SA is really difficult.  The notifications get lost in the onslaught of incoming notifications in SA.  As a result, we are not timely in our replies, which is a problem.  How have you seen other companies handle this challenge?"",
            "status": "No Article Found",
        },
        {
            "no": 36,
            "topic": "Mosquito Control Upsell Automation",
            "count": 1,
            "description": "Timestamp: 2024-05-21T17:47:20Z > Visitor said \"Hi there,  Benjamin lawn here.  We"d like our Mosquito Control upsell to go live if possible.  I"ve edited the documents and we"re ready to have the first one send tomorrow (Wednesday 5/22) if possible.  The dates for the next 2 are June 5th and June 20th.\"",
            "status": "No Article Found",
        },
        {
            "no": 37,
            "topic": "2-way texting consent automation setup",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-16T18:13:08Z > Visitor said "I sent an email to the Help Desk about the new 2 way texting consent. Chad said there\"s a free automation with a form and document. Would you be able to help me get this set up for our company?"",
            "status": "No Article Found",
        },
        {
            "no": 38,
            "topic": "Test conversation",
            "count": 1,
            "description": "(1) Timestamp: 2024-05-13T18:58:12Z > Visitor said "Test"",
            "status": "No Article Found",
        },
        {
            "no": 39,
            "topic": "AI Measurements Activation",
            "count": 1,
            "description": "(2024-05-10 16:18:59) Visitor 58827748: Can you check to see if AI measurements was activated on my account. This is Healthylawn@roadrunner.com",
            "status": "No Article Found",
        },
        {
            "no": 40,
            "topic": "Landing Page Location",
            "count": 1,
            "description": "(2024-05-10 16:22:56) Visitor 58827748: where do i find my landing page",
            "status": "No Article Found",
        },
        {
            "no": 41,
            "topic": "Automation Issues",
            "count": 1,
            "description": "(2024-05-09 20:55:52) Visitor 42514703: Automations problem",
            "status": "No Article Found",
        },
        {
            "no": 42,
            "topic": "Automation Request",
            "count": 1,
            "description": "Timestamp: 2024-05-09T03:17:25Z > Visitor said "Asked for an automation to be built a couple weeks ago.  Still waiting for someone to reach out"",
            "status": "No Article Found",
        },
        {
            "no": 43,
            "topic": "Credit Card Form Issue",
            "count": 1,
            "description": "Timestamp: 2024-05-02T18:33:49Z > Visitor said "I insert the SG credit card form. (For example, I insert the email document and then click insert form.) I\"m not sure that the form is working anymore - can you please check on this for me?"",
            "status": "No Article Found",
        },
    ]
}
"""
cohereModelId = "cohere.embed-english-v3"

client = boto3.client(
    "bedrock-runtime",
    region_name="us-west-2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
)

# For the list of parameters and their possible values,
# check Cohere"s API documentation at https://docs.cohere.com/reference/embed
pairs = [["Email Upsell Setup","Upsell Campaign Setup"],
        ["Email Upsell Setup","Upsell Setup"],
        ["Upsell Automation Issues","Upsell Request"],
        ["Upsell request","Upsell setup"],
        ["Upsell Configuration", "Customized Upsell Configuration"],
        ["Automation request", "Automation Issues"],
        ["SimpleEstimate Tool Integration with CRM (Go High Level)","SimpleEstimate Tool Customization"],
        ["SimpleEstimate Tool Placement on Website", "SimpleEstimate Tool Authorization and Security"],
        ["SimpleEstimate Tool Tutorials and Guidance", "SimpleEstimate Tool Placement on Website"],
        ["Mosquito Control Upsell Automation", "2-way texting consent automation setup"],
        ["20 Day to Close Automation Issues", "Newsletter Automation Issues"],
        ["NPS Score Automation Issues", "Upsell Automation Issues"]]

for i, pair in enumerate(pairs):
    print(f"{pairs[i]}:",fuzz.WRatio(pairs[i][0].lower(), pairs[i][1].lower()))

s = "20 Day to Close Automation Issues"
for row in table["rows"]:
    print(f"sim wit {row["topic"]}:", fuzz.WRatio(s.lower(), row["topic"].lower()))

s=s.lower().replace("issue","")
print(s)
"""
