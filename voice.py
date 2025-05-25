from omnidimension import Client

# Initialize client
client = Client(api_key)

# Create an agent
response = client.agent.create(
    name="Limited-Edition Sneaker Deal Finder",
    welcome_message="""Hello, I am your assistant here to find the best deals on limited-edition sneakers like the Jordan 1 Retro Low OG Game Royal Men's. Can I ask if you have a preferred reseller or price range to start?""",
    context_breakdown=[
                {"title": "Sneaker Preference Capture", "body": """ Ask the user about the specific limited-edition sneakers they are interested in. Confirm details like size or any special preferences. For example: 'You mentioned the Jordan 1 Retro Low OG Game Royal Men's; do you have a size preference or any specific features you're looking for?' After obtaining details, proceed to contact resellers. """},
                {"title": "Calling Resellers for Quotes", "body": """ Simulate calling five different resellers to inquire about the specific sneakers. When speaking to each reseller, clearly mention the sneaker model, then ask: 'I'm looking for the current price and estimated delivery time for the Jordan 1 Retro Low OG Game Royal Men's.' Record the reseller's name, price, and delivery time accurately for comparison. """},
                {"title": "Data Verification & Recording", "body": """ Ensure all gathered information from resellers—namely, the reseller name, offered price, and delivery time—is recorded accurately. Cross-verify details with user if necessary: 'Just to confirm, based on our calls, I have these details: Reseller A offers at [price A] with delivery by [time A], Reseller B offers at [price B] with delivery by [time B]. Is that correct?' This sets the stage for comparison. """},
                {"title": "Deal Comparison & Evaluation", "body": """ With all data collected, compare the deals based on price and delivery time. Present the comparisons clearly: 'Reseller A offers the sneakers at [price A] but with a longer delivery time than Reseller B who offers [price B].' Frame recommendations by ranking the best combinations of price and delivery: 'Based on price and delivery, your best options are...' """},
                {"title": "Top Deals Recommendation", "body": """ Propose the top three deals to the user, providing concise summaries of each: 'After evaluating, the top deals are from Reseller X at [price] with a delivery time of [delivery days]. Would you like more details on any of these options, or shall we proceed with a choice?' Ensure clarity for user decisions. """},
                {"title": "Webhook Activation & Email Summary", "body": """ Following the deal recommendation, inform the user about triggering a summary email and logging data. Mention: 'I'm sending a detailed summary of the top deals to your email and logging this session for your future reference. Would you like any additional deals included in the summary or have any final requests?' Then proceed to trigger the webhook that sends the summary and logs the details. """},
                {"title": "Conversation Closing", "body": """ Finalize the interaction by thanking the user for using the service. Encourage future assistance: 'Thank you for choosing our service to find the best deals on your sneakers. If you think of anything else you need, feel free to reach out!' Conclude the conversation professionally. """}
    ],
    transcriber={
        "provider": "azure_stream",
        "silence_timeout_ms": 400
    },
    model={
        "model": "gpt-4o-mini",
        "temperature": 0.7
    },
    voice={
        "provider": "eleven_labs",
        "voice_id": "8"
    },    web_search={
        "enabled": True,
        "provider": "DuckDuckGo"
    },
   "post_call_actions": {
    "email": {
        "enabled": True,
        "recipients": ["example@example.com"],
        "include": ["summary", "extracted_variables"]
    },
    "webhook": {
        "enabled": True,
        "url": "https://hooks.zapier.com/hooks/catch/xxxxx/yyyyy",  # replace with your Zapier webhook URL
        "payload": [
            {"key": "user_email", "value": "example@example.com"},
            {"key": "requested_sneaker", "source": "extracted_variables"},
            {"key": "user_preferred_price_range", "source": "extracted_variables"},
            {"key": "reseller_name", "source": "extracted_variables"},
            {"key": "price", "source": "extracted_variables"},
            {"key": "delivery_time", "source": "extracted_variables"},
            {"key": "top_3_deal_recommendations", "source": "extracted_variables"}
        ]
    },
    "extracted_variables": [
        {"key": "requested_sneaker", "prompt": "Extract the specific sneaker model and any preferences discussed."},
        {"key": "user_preferred_price_range", "prompt": "Record any preferred price range mentioned by the user."},
        {"key": "reseller_name", "prompt": "For each reseller, extract and record their name."},
        {"key": "price", "prompt": "Record the price given by each reseller for the sneakers."},
        {"key": "delivery_time", "prompt": "Extract and log the estimated delivery time given by each reseller."},
        {"key": "top_3_deal_recommendations", "prompt": "Summarize the top 3 deal recommendations including reseller names, prices, and delivery times."}
    ]
 },
)

print(f"Status: {response['status']}")
print(f"Created Agent: {response['json']}")

# Store the agent ID for later examples
agent_id = response['json'].get('id')


