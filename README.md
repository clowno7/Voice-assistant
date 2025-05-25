# Voice-assistant
Building a voice assistant for the following problem statement: Finding the Best Deal on High Demand Drops

Problem statment: 
When trying to buy limited-edition sneakers or concert tickets, it’s hard to know who’s offering the 
best price or fastest delivery. Resellers often have different prices and offers, and users don’t have 
time to compare everything. Your task is to build a voice AI agent that can speak with resellers, track 
and negotiate prices, compare options, and help the user choose the best deal.

Steps invloved:

Step 1: Choose a product or ticket (e.g., sneakers, concert passes, cricket final) .I choose sneakers

Step 2: Create or mock a list of reseller offers (price, delivery time, seller name) 

Step 3: Use OmniDimension to build a voice agent that talks to the user and compares these offers 

Step 4: Use OmniDimension’s Post Call API or custom webhook to: 
• Send an email with the top  offers 
• Log each seller interaction (price, availability, etc.) to Google Sheets or a CRM 
 
Note:I have used Custom webhook(zapier)


🔁 Step-by-Step Zapier Setup

✅ 1. Create a Free Zapier Account
Go to `https://zapier.com`

Sign up or log in

✅ 2. Create a New Zap
🔹 Trigger: Webhook
Choose: Webhooks by Zapier

Event: Catch Hook

Click Continue

Copy the Webhook URL

Go back to OmniDimension and paste this URL in the Post-Call Webhook section

In OmniDimension, run a test call to send data

✅ Zapier will now catch the sample payload

✅ 3. Action: Send Email (Gmail)
App: Gmail

Event: Send Email

Connect your Gmail account

Fill in:

To: `user_email` from the webhook payload

Subject: Top 3 Best Deals for Your Order

Body:
`Hi there,`

`Here are your top 3 deals:`

`1. {{sellers__0__name}} - ${{sellers__0__price}} - Delivery: {{sellers__0__delivery}} days
2. {{sellers__1__name}} - ${{sellers__1__price}} - Delivery: {{sellers__1__delivery}} days
3. {{sellers__2__name}} - ${{sellers__2__price}} - Delivery: {{sellers__2__delivery}} days`

Thanks for using OmniDeals!

✅ 4. Action: Add to Google Sheets
App: Google Sheets

Event: Create Spreadsheet Row

Choose a Google account

Create a Google Sheet like this:

Sheet Name: OmniDeals Log

`Columns: Seller | Price | Delivery`

In Zapier:

`Map sellers__0__name, price, delivery → row 1`

Add additional actions to insert all 5 sellers (duplicate this action 5 times, or use a Zapier Loop/Code step for automation)

✅ This logs the seller data for tracking.



steps invvolved to run it on Your system:

step 1:Install omnidimension Module

pip install omnidimension


step 2: Copy paste the code

from voice.py

And Follow The step for Zapier and add your webHook ,Copy your WebHook link aand replace it with "https://hooks.zapier.com/hooks/catch/xxxxx/yyyyy" in voice.py file

And you are Good to Go probably!!

Note: using OmniDimension itself will be highly recommended
