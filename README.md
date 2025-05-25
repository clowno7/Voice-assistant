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
• Send an email with the top 3 offers 
• Log each seller interaction (price, availability, etc.) to Google Sheets or a CRM 




steps invvolved to run it on Your system:

step 1:Install omnidimension Module
pip install omnidimension


step 2: Copy paste the code

from voice.py
