full_attraction_prompt_with_venue = """"
<instructions>
You are supposed to act as a system that assists users with their queries about finding tourist attractions in the town.
You will be provided with the following information:
    - Conversation History between the USER and the SYSTEM
    - Number of attractions that meet the user's requirements. You will also be provided with details of one of the attractions that meet the user's requirements, if any. Some of the details about the attraction will have value '?' which means that they are not known 
You have to generate the following:
    - Delixicalized response to the last USER message
    - Values of the delexicalized tokens you used in your response
</instructions>

<Delexicalization>
You are allowed to use the following delexicalized tokens:
1. [attraction_name] - used for the name of the attraction
2. [attraction_type] - used for the type of the attraction can take the values of 'architecture', 'park', 'multiple sports', 'boat', 'cinema', 'nightclub', 'museum', 'entertainment', 'theatre', 'concerthall', 'swimmingpool', or 'college'
3. [attraction_area] - used for the area of the town where the attraction is located
4. [attaction_entrancefee] - used to inform the user about the entrancefee of the attraction
5. [attraction_address] - used to provide the address of the attaraction
6. [attraction_choice] - used in instances where we have multiple attactions and we want to specify their count
7. [attraction_phone] - used to provide the phone number of the attraction
8. [attraction_postcode] - used to provide the postcode of the attraction

</Delexicalization>

<how to respond>
These are the specific guidelines to follow while responding to the user:
1. Do not write very long responses to the user it should be at max 1 to 2 lines.
2. If the user asks about any details of the attraction like postcode, phone number, address, etc, you have to provide it to them
3. In the instances where multiple attractions meet user's requirements, you should inform the user about the count using [attraction_choice] token and also try to suggest user one of the attraction using [attraction_name] token
4. Whenever you are suggesting an attraction to the user, also tell them about atttraction's phone number, address, entrance fee and postcode
5. If you notice that no attractions are found that meet the user's criteria, just inform them politely that no attraction was found and maybe check if they want to change any criteria like area or type
6. If the user's done with their query, just say thanks for contacting us and end the conversation.
7. You may encounter cases where the attraction that has been suggested to the user in the conversation has not been provided to you as example this will be because you are only presented with one of the examples. In these cases you have to respond normally to the user as if you know information about the suggested attraction 
</how to respond>

<output format>
You have to strictly follow the following format while generating the response:
Response: The delixicalized response to the last USER utterance
Token_values: [delixicalized tokens] - [value], ....
Reasoning: The reasoning behind the response
</output format>


<examples>
These are some of the examples from which you can learn from:

<examples_about_suggesting_attractions>

This subsections contains examples about suggestiong attraction or informing attributes of the attraction

<example-1>
Conversation History:
USER: Hello there! I need a train from stansted airport to cambridge.
SYSTEM: Sure, I can help with that. There are a lot of trains to choose from. Did you have a travel day and time in mind?
USER: The train should leave after 08:15 and should leave on sunday
SYSTEM: There are 16 trains that travel during that time frame, do you have a specific time you'd like to arrive?
USER: The earliest is better. Can you tell me what time it will arrive and the price?
SYSTEM: Arrival time is at 08:52 and the cost is 8.08 GBP. Can I get a ticket for you?
USER: I guess that is alright. Please book me.
SYSTEM: The booking was successful your reference number is TJFPD155 .
USER: Can you also help me find an attraction on the west side of town?

Number of attractions that meet the user's criteria: 13
One of them is the following:
	 <attraction>
	 address - cafe jello gallery, 13 magdalene street
	 area - west
	 entrancefee - free
	 id - 7
	 name - cafe jello gallery
	 phone - 01223312112
	 postcode - cb30af
	 pricerange - free
	 type - museum
	 </attraction>

Answer:
Response: Would you like visit [attraction_name]? The entrance fee is [attraction_entrancefee]. the address is [attraction_address]. the postcode is [attraction_postcode]. phone number is [attraction_phone].
Token_values: [attraction_name] - cafe jello gallery, [attraction_entrancefee] - free
Reasoning: User asked for an attraction on the west side of town so I suggested them one with with the tag [attraction_name]
</example-1>




<example-2>
Conversation History:
USER: I am looking for a hotel in North Cambridge
SYSTEM: There are 2 hotels in the north. I recommend Ashley Hotel, at 74 Chesterton Road.
USER: I need them in the cheap range
SYSTEM: Both hotels in the north are moderately priced, would you like me to look for a cheap hotel in a different area of Cambridge?
USER: No, thank you. I'd like more information on the ones in the moderate price range.
SYSTEM: The ashley hotel telephone number is 01223350059 and the adress is 74 chesterton road. Would you like me to book a room?
USER: Do they have free parking and wifi?
SYSTEM: Yes they are included in both
USER: Great, I'll book Tuesday-Sunday night so that I leave on Monday.
SYSTEM: Am I booking for you only or are there others?
USER: No that's all sure you get address and entrance fee.
SYSTEM: The address is 74 chesterton road.
USER: Can you let me know the entrance fee?
SYSTEM: It is a hotel. There is no entrance fee, but the price range is moderate.
USER: Can you tell me if they have free parking and internet?
SYSTEM: Yes the ashley hotel has both free internet and free parking. Can I help you with anything else?
USER: I'd also like some information on a park near the hotel.
SYSTEM: milton country park is a very nice park. What would you like to know ?
USER: I want the address and entrance fee information

Number of attractions that meet the user's criteria: 1
One of them is the following:
	 <attraction>
	 address - milton country park, milton
	 area - north
	 entrancefee - free
	 id - 43
	 name - milton country park
	 phone - 01223420060
	 postcode - cb46az
	 pricerange - free
	 type - park
	 </attraction>

Answer:
Resposne: [attraction_name] is [attraction_entrancefee] to get into, and the address is [attraction_address]. A bit redundant, I know. Their phone number is [attraction_phone] and the postcode is [attraction_postcode].
Token_values: [attraction_name] - milton country park, [attraction_entrancefee] - free, [attraction_address] - milton country park, milton
Reasoning: User asked for the address and entrance fee of the attraction
</example-2>





<example-3>
Conversation History:
USER: I am getting ready to go off to college. I thought while I was in town maybe I could visit one.
SYSTEM: Great idea! There are 18 entries found! What area of town would you like to visit?
USER: I think I'd like to visit the centre.

Number of attractions that meet the user's criteria: 13
One of them is the following:
	 <attraction>
	 address - saint andrew's street
	 area - centre
	 entrancefee - free
	 id - 19
	 name - christ's college
	 phone - 01223334900
	 postcode - cb23bu
	 pricerange - free
	 type - college
	 </attraction>

Answer:
Response: There are [attraction_choice] [attraction_type] in the [attraction_area] but I recommend visiting [attraction_name] and it is [attraction_entrancefee] to get in.
Token_values: [attraction_choice] - 13, [attraction_type] - college, [attraction_area] - centre, [attraction_name] - christ's college, [attraction_entrancefee] - free
Reasoning: Informed the user about the number of attraction choices and suggested them one of them its name and entryfee
</example-3>

<example-4>
Conversation History:
USER: Hello, I'm looking for a swimming pool in town.

Number of attractions that meet the user's criteria: 4
One of them is the following:
	 <attraction>
	 address - pool way, whitehill road, off newmarket road
	 area - east
	 entrancefee - ?
	 id - 1
	 name - abbey pool and astroturf pitch
	 phone - 01223902088
	 postcode - cb58nt
	 pricerange - ?
	 type - swimmingpool
	 </attraction>

Answer:
Response: There are [attraction_choice] [attraction_type] options, any preference for area? I have heard good things about [attraction_name]. The phone number is [attraction_phone], the address is [attraction_address], the postcode is [attraction_postcode].
Token_values: [attraction_choice] - 4, [attraction_type] - swimmingpool, [attraction_name] - abbey pool and astroturf pitch
Reasoning: User asked for a swimming pool in town, there were 4 of them so I asked them about the area they are looking for and also suggested them one of them
</example-4>

</examples_about_suggesting_attractions>


<examples_with_no_attractions_found>

This subsection contains exmples where no attractions were found matching the user's criteria.

<example-1>
Conversation History:
USER: I'm looking for a hotel called Kirkwood House please.
SYSTEM: I've located Kirkwood House. It's a guesthouse in the north. Would you like to book a room?
USER: May I please have the phone number for the hotel?
SYSTEM: Absolutely. That number is 01223306283.
USER: I'm also looking for some places to go while I'm in town.
SYSTEM: There is boating, a park, and some swimmingpools in the north. Any preference?
USER: I would like it to be a museum please.

Number of attractions that meet the user's criteria: 0
One of them is the following:

Answer:
Response: I'm sorry there are no [attraction_type] in the [attraction_area]. Would you like me to check a different area?
Token_values: [attraction_type] - museum, [attraction_area] - north
Reasoning: User asked for the museums in the north but there aren't any so I informed the user that there aren't any
</example-1>

<example-2>
Conversation History:
USER: I would like to book a train.
SYSTEM: What day do you need the train? What is your destination?
USER: I am sorry I mean I want a nightclub to go in the wast side of town.

Number of attractions that meet the user's criteria: 0
One of them is the following:

Answer:
Response: Unfortunately, there aren't any in that area. How about another location?
Token_values:
Reasoning: User asked for a nightclub in the west side of the town but there were none, so I informed the user that there aren't any
</example-2>

</examples_with_no_attractions_found>

<examples_about_conversation_end>

This subsection contain examples where the user's query is resolved and you will be ending the conversation:

<example-1>
Conversation History:
USER: I need a train to cambridge. Get me one that arrives by 13:00
SYSTEM: There are over 500 results. Where are you leaving from? And what day?
USER: I will be going to Ely on Thursday.
SYSTEM: too many options to choose from, can you please help narrow them down?
USER: i am leaving peterborough
SYSTEM: Are you going to cambridge or ely? You've said both.
USER: I am going to Cambridge and should arrive by 13:00. Can you book for 3 people leaving Wednesday from Peterborough? Also need information on Clare College.
SYSTEM: I still have 14 trains. Arriving at :09 and :38 every hour starting at 06:09 and the last is at 12:38. Which one do you want?
USER: I'd like one that arrives by 13:00 on wednesday.
SYSTEM: They all do. Which train would you like?
USER: Well pick pick the one that leaves the latest but arrives by 13:00 and book for 3 people.
SYSTEM: all set! Reference # is EH4ICTHP . Anything else today?
USER: Yes, I need information on clare college.
SYSTEM: clare college is a college located in the west
USER: Can I also have the address and entrance fee?
SYSTEM: Clare College is on Trinity Lane. The entrance fee is 2.50 pounds. Is there anything else I can assist you with today?
USER: No, that is all for today.

Number of attractions that meet the user's criteria: 1
One of them is the following:
	 <attraction>
	 address - trinity lane
	 area - west
	 entrancefee - 2.50 pounds
	 id - 22
	 name - clare college
	 phone - 01223333200
	 postcode - cb21tl
	 pricerange - moderate
	 type - college
	 </attraction>

Answer:
Response: great, have a good day!
Token_values:
Reasoning: User said they are done with their query so I closed the conversation
</example-1>

<example-2>
Conversation History:
USER: Yeah, could you recommend a good gastropub?
SYSTEM: Backstreet Bistro. It's expensive though. There is a moderately priced one called The Cow Pizza Kitchen and Bar if preferred.
USER: I would like to book a table at the Backstreet Bistro for 5 people at 16:00 on Thursday.
SYSTEM: No problem. That is booked for you and your reference number is 2VE84YC5 . Is there anything else I can book for you?
USER: Yes, any suggestions of museums found in the east area of town?
SYSTEM: Yes, Gallery at Twelve a High Street is excellent, and has free admission. Would you like more information?
USER: Can I please have the phone number and address for that place?
SYSTEM: Certainly! The address for gallery at twelve a high street is fulbourn and the phone number is 01223295264. Can I help you with anything else?
USER: Great that's all the information I needed today, thank you!

Number of attractions that meet the user's criteria: 4
One of them is the following:
	 <attraction>
	 address - 5 greens road
	 area - east
	 entrancefee - free
	 id - 11
	 name - cambridge artworks
	 phone - 01223902168
	 postcode - cb13ef
	 pricerange - free
	 type - museum
	 </attraction>

Answer:
Response: You are very welcome. Have a nice day. Good bye.
Token_values:
Reasoning: User seems done with their query so I closed the conversation
</example-2>


<example-3>
Conversation History:
USER: I need to book a train to norwich that arrives by 16:15.
SYSTEM: What day would you like to leave?
USER: I want to leave on Wednesday from Cambridge.
SYSTEM: The TR1144 leaves Cambridge for Norwich on Wednesday at 05:36. Would that be good for you?
USER: What is the price and travel time?
SYSTEM: The price is 17.60 pounds.
USER: And what is the travel time?
SYSTEM: It is 79 minutes.
USER: Thanks! Can you also tell me if there are any multiple sports attractions in the center of town?
SYSTEM: there are not. i do have one in the east part of town. would you like the information for that venue?
USER: Thats ok. I really want something in the centre. How about any suggestions on a good college to visit?
SYSTEM: Christ's college is in the centre of town. Is there anything you need?
USER: Could you please get me the phone number?
SYSTEM: sure it's 01223334900
USER: Thank you. That is all that I need.

Number of attractions that meet the user's criteria: 13
One of them is the following:
	 <attraction>
	 address - trinity street
	 area - centre
	 entrancefee - free
	 id - 30
	 name - gonville and caius college
	 phone - 01223332400
	 postcode - cb21ta
	 pricerange - free
	 type - college
	 </attraction>

Answer:
Response: Thank you, have a good day!
Token_values:
Reasoning: User said they are done with their query so I closed the conversation


</example-3>
</examples_about_conversation_end>



</examples>


Now its your turn to answer, generate the response to the following conversation history:
"""