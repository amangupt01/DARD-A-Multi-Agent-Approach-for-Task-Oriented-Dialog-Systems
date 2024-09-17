full_DST_prompt = """

<instructions>
You are an intelligent agent and have been assigned the task to perform Dialogue State Tracking on a conversation between a USER and an SYSTEM.
You will be provided with a conversation history between the USER and the SYSTEM and you need to detect the slots present in the conversation history.
Each slot will have a domain, a slot name and a slot value. The domain can be one of the following: restaurant, attraction, hotel, taxi, train.
You will need to track only those slots which the USER informs the SYSTEM about.
</instructions>

<slot-types>
Some of the domain-slots can only take categorical values while the rest can take any values depending on the utterance. 
The following is an exhaustive list of all possibles slot that you need to detect in the conversation history:
Serial Number, Domain, Possible Slots, Categorical or Non-Categorical
1, restaurant, area, categorical
2, restaurant, pricerange, categorical
3, restaurant, bookday, categorical
4, restaurant, bookpeople, categorical
5, restaurant, food, non-categorical
6, restaurant, name, non-categorical
7, restaurant, booktime, non-categorical
8, attraction, area, categorical
9, attraction, type, categorical
10, attraction, name, non-categorical
11, hotel, area, categorical
12, hotel, bookday, categorical
13, hotel, bookpeople, categorical
14, hotel, bookstay, categorical
15, hotel, internet, categorical
16, hotel, parking, categorical
17, hotel, stars, categorical
18, hotel, type, categorical
19, hotel, pricerange, categorical
20, hotel, name, non-categorical
21, train, destination, categorical
22, train, departure, categorical
23, train, day, categorical
24, train, bookpeople, categorical
25, train, arrive, non-categorical
26, train, leave, non-categorical
27, taxi, arrive, non-categorical
28, taxi, leave, non-categorical
29, taxi, departure, non-categorical
30, taxi, destination, non-categorical
</slot-types>

<categorical-slots-values>
Since categorical domain-slots can only take some fixed values, all possible such slots and their possible values are listed below:   
Serial Number, domain, slot, possible values
1, restaurant, area - ['south', 'centre', 'east', 'west', 'north']
2, restaurant, bookday - ['thursday', 'tuesday', 'sunday', 'monday', 'saturday', 'wednesday', 'friday']
3, restaurant, bookpeople - ['8', '5', '2', '6', '4', '3', '7', '1']
4, restaurant, pricerange - ['moderate', 'expensive', 'cheap']
5, attraction, area - ['south', 'centre', 'east', 'west', 'north']
6, attraction, type - ['architecture', 'park', 'multiple sports', 'boat', 'cinema', 'nightclub', 'museum', 'entertainment', 'theatre', 'concerthall', 'swimmingpool', 'college']
7, hotel, area - ['south', 'centre', 'east', 'west', 'north']
8, hotel, bookday - ['thursday', 'tuesday', 'sunday', 'monday', 'saturday', 'wednesday', 'friday']
9, hotel, bookpeople - ['8', '5', '2', '6', '4', '7', '3', '1']
10, hotel, bookstay - ['5', '2', '4', '3', '1']
11, hotel, parking - ['no', 'yes']
12, hotel, stars - ['5', '2', '4', '3', '0']
13, hotel, type - ['guesthouse', 'hotel']
14, hotel, internet - ['no', 'yes']
15, hotel, pricerange - ['moderate', 'expensive', 'cheap']
16, train, bookpeople - ['8', '5', '2', '10', '6', '4', '7', '3', '1']
17, train, day - ['thursday', 'tuesday', 'sunday', 'monday', 'saturday', 'wednesday', 'friday']
18, train, departure - ['stansted airport', 'cambridge', 'leicester', 'london liverpool street', 'birmingham new street', 'kings lynn', 'stevenage', 'bishops stortford', 'london kings cross', 'peterborough', 'norwich', 'broxbourne', 'ely']
19, train, destination - ['stansted airport', 'cambridge', 'leicester', 'london liverpool street', 'birmingham new street', 'kings lynn', 'stevenage', 'bishops stortford', 'london kings cross', 'norwich', 'peterborough', 'broxbourne', 'ely']
</categorical-slots-values>

<output-format>
You always have to follow the following format for generation. Be sure to strictly follow the format. Do not generate any domain or slot which is not mentioned in the list above, for categorical slots generate values
form the list above and for non-categorical slots generate values from the utterance. Do not generate anything else apart from what is being asked. The output format is as follows:

I found the following slots present in the conversation history you have provided:
domain1: slot1 - value1, slot2 - value2
domain2: slot3 - value3
domain3: slot4 - value4, slot5 - value5
</output-format>

<examples>
This section contains some of the examples that you can learn from:

<example>
Example 1
The following is the conversation history:
USER: Hi, I'm looking for information on concert halls in the east. Can you give me any suggestions?
SYSTEM: I'm afraid I didn't find any. Would you like to look in another area?
USER: Yes an you check the south please?
SYSTEM: unfortunately there isn't anything in that area either. would you like to try another location?
USER: how about just entertainment instead?
SYSTEM: I have two entertainment venues in the south. I have Nusha and Tenpin. Would you like their phone numbers?
USER: could you please provide the phone number, postcode, and entrance fee for each.
SYSTEM: The tenpin is located at cambridge leisure park, clifton way. The phone number is 08715501010 and the post cod is cb17dy.
USER: I also need a guesthouse with free wifi.
SYSTEM: I have several guesthouses available. What area of town would you like?
USER: Any area will do. Is there a cheap one that's 4 stars, with wifi?

Answer: I found the following slots present in the conversation history you have provided:
hotel: internet - yes, pricerange - cheap, stars - 4, type - guesthouse, 
attraction: area - south, name - tenpin, type - entertainment, 
</example>


<example>
Example 2
The following is the conversation history:
USER: Can you get me a train leaving after 18:15 departing from cambridge?

Answer: I found the following slots present in the conversation history you have provided:
train: departure - cambridge, leave - 18:15, 
</example>


<example>
Example 3
The following is the conversation history:
USER: I'm looking for information on 4-star rated guesthouses in Cambridge
SYSTEM: I have a number of 4 star guesthouses available, would you like to book one in a particular area?
USER: Not really. Could you suggest one with free parking?
SYSTEM: Okay, how about the Acorn Guest House in the north?
USER: Sure. Can we spend 5 nights starting on Sunday? I am going to need room for 7 people.
SYSTEM: Reference number is 29IN9CT3 for the acorn guesthouse.
USER: I would also like to eat somewhere cheap in the middle of town.
SYSTEM: I suggest the dojo noodle bar, an asian oriental restaurant, would you like to make a reservation?
USER: do you have one the is portuguese food ?
SYSTEM: There is. How does Nandos City Centre sound?
USER: Sounds great if it is portuguese. I'll take a reservation for 7 people at 20:00 for the same day.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - sunday, bookpeople - 7, booktime - 20:00, food - portuguese, name - nandos city centre, pricerange - cheap, 
hotel: bookday - sunday, bookpeople - 7, bookstay - 5, name - acorn guest house, parking - yes, stars - 4, type - guesthouse, 
</example>


<example>
Example 4
The following is the conversation history:
USER: I'm visiting Cambridge as a tourist! I'm looking for an expensive place to stay that includes free parking!

Answer: I found the following slots present in the conversation history you have provided:
hotel: parking - yes, pricerange - expensive, 
</example>


<example>
Example 5
The following is the conversation history:
USER: Can you assist me in finding me an Expensive Restaurant in Cambridge where I can dine? The restaurant should be serving British foods.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: food - british, pricerange - expensive, 
</example>


<example>
Example 6
The following is the conversation history:
USER: I'm looking for a place to dine that's in the cheap price range and that serves Indian food.
SYSTEM: Would you like a recommendation, or do you want to specify an area?
USER: I'd like a recommendation that is able to book a table for 5 people at 14:45 on Friday.
SYSTEM: Alright, I booked you a table for 5 on Friday at 14:45 at the Kohinoor. Your reference number is 20OK4WP8 . Can I help you with anything else?
USER: Thanks, I'd also like to find an attraction in the east, please.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: bookday - friday, bookpeople - 5, booktime - 14:45, food - indian, name - kohinoor, pricerange - cheap, 
attraction: area - east, 
</example>


<example>
Example 7
The following is the conversation history:
USER: I would like to find a moderately priced restaurant in the west part of town.
SYSTEM: Meghna is an indian restaurant that meets your criteria. Would you like their location?
USER: west part of town.
SYSTEM: Meghna is located in the west part of town.
USER: Can you please let me know the address?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - west, name - meghna, pricerange - moderate, 
</example>


<example>
Example 8
The following is the conversation history:
USER: I need a place to stay that is a guesthouse.
SYSTEM: Of course, in which area of town will you be staying?
USER: I want it in the west, and it should be moderately priced.

Answer: I found the following slots present in the conversation history you have provided:
hotel: area - west, pricerange - moderate, type - guesthouse, 
</example>


<example>
Example 9
The following is the conversation history:
USER: I am looking for a train. I need to leave on Tuesday and want to arrive by 20:45.
SYSTEM: Where are you departing from? And where would you like to go?
USER: I'm heading to Cambridge, and I'd like to leave from peterborough.
SYSTEM: The last train into cambridge before 20:45 is the TR2673, arriving at 20:38. You would leave peterborough at 19:48.
USER: That will do, what is the price and train ID?

Answer: I found the following slots present in the conversation history you have provided:
train: arrive - 20:45, day - tuesday, departure - peterborough, destination - cambridge, 
</example>


<example>
Example 10
The following is the conversation history:
USER: I'm looking for a moderate priced place to dine in the centre of town
SYSTEM: I've got many here that match that description. Would you like a specific food type? Maybe British food?
USER: How about Chinese food?
SYSTEM: jinling noodle bar is a chinese restaurant in the centre, 11 Peas Hill City Centre
USER: That sounds great! Can you see if there's a table for 3 available at 16:00 on Monday?
SYSTEM: Your table for 3 has been reserved on Monday at 16:00 at Jinling Noodle Bar. Your reference number is 3UL0PL4Q . Can I help with anything else today?
USER: Great. i also need to find a place to stay in the same price range as the restaurant and I am looking for a hotel.
SYSTEM: Would you also like that in the same area as the restaurant?
USER: Yes, please, so moderately priced hotel in the centre.
SYSTEM: I have one listing for cityroomz in the centre of town.
USER: Great, we need that booked as well starting monday for 5 nights.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - monday, bookpeople - 3, booktime - 16:00, food - chinese, name - jinling noodle bar, pricerange - moderate, 
hotel: area - centre, bookday - monday, bookstay - 5, name - cityroomz, pricerange - moderate, type - hotel, 
</example>


<example>
Example 11
The following is the conversation history:
USER: I feel like visiting a museum, find me one please
SYSTEM: We have lots! What part of town will you be in?
USER: I don't have a preference. Can you recommend one and provide info on it?
SYSTEM: cambridge artworks in the east is rather nice. It has free admission and is located at 5 greens road. Is there any other information I can provide?
USER: No, that is fine. I also need a train that should arrive by 11:15 and should leave on saturday.
SYSTEM: Did you have a departure site or destination in mind?
USER: Oh duh, sorry! I jumped the gun there! I'd like to go to Cambridge from London Kings Cross.
SYSTEM: TR4824 leaves london kings cross at 9:17 and arrives at 10:08. Would you like to book tickets?
USER: How much would the ticket cost?
SYSTEM: The cost of a ticket is 18.88 pounds. Would you like me to book you a ticket?
USER: Not right now, but could you give me the estimated travel time for the train trip?
SYSTEM: The travel time for TR4824 is 51 minutes.
USER: cool that's all i need thanks
SYSTEM: thanks for inquiring from us. have a great day
USER: Thank you for helping me today.

Answer: I found the following slots present in the conversation history you have provided:
attraction: type - museum, 
train: arrive - 11:15, day - saturday, departure - london kings cross, destination - cambridge, 
</example>


<example>
Example 12
The following is the conversation history:
USER: I need an inexpensive restaurant in the centre of Cambridge.
SYSTEM: There is nothing cheap in centre. Can you expand your price range?
USER: Not really, try kosher food types.
SYSTEM: I'm sorry, but there is no Kosher restaurant in the area, can I check other part of town?
USER: How about one that serves Asian Oriental food?
SYSTEM: I've located 2 inexpensive restaurants, Dojo noodle bar and J Restaurant. Which would you like?
USER: I'll try the noodle bar. I'd like to reserve a table as well.
SYSTEM: How many people would you like to reserve a table for? And, what time and day would you like to make the reservation?
USER: for seven people on wednesday.
SYSTEM: Sure, I can book that. What time would you like the reservation for?
USER: I would like the reservation to be at 16:00 please.
SYSTEM: Okay. Your booking at the Dojo Noodle Bar was successful. The reference number is 0EGLWEQK . Can I help with anything else today?
USER: Great, now I need a train to leave on Thursday departing from cambridge going to peterborough, it needs to arrive by 14:30.
SYSTEM: How many tickets do you need?
USER: I actually don't need to book any tickets. I just need the train id, travel time and departure time please.
SYSTEM: TR7098 departs Thursday at 05:06 and has a travel time of 50 minutes.
USER: Thanks. You have been so helpful with the restaurant and train. That's all. Goodbye.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - wednesday, bookpeople - 7, booktime - 16:00, food - asian oriental, name - dojo noodle bar, 
train: arrive - 14:30, day - thursday, departure - cambridge, destination - peterborough, 
</example>


<example>
Example 13
The following is the conversation history:
USER: I'm looking for a train that leaves after 13:45 on Wednesday.
SYSTEM: Can you give me departure and destination locations, please?
USER: Yes. I'm departing from Broxbourne and going to Cambridge.
SYSTEM: The TR3470 leaves at 16:32. That's the first train on that route after 13:45.
USER: Thank you, can I get tickets for 2 people and the reference number if successful?
SYSTEM: I will book that for you now.
USER: Can I have that reference number please?
SYSTEM: I will have that reference number in one moment.
USER: Okay thank you, and I need the postcode too.

Answer: I found the following slots present in the conversation history you have provided:
train: bookpeople - 2, day - wednesday, departure - broxbourne, destination - cambridge, leave - 13:45, 
</example>


<example>
Example 14
The following is the conversation history:
USER: I want to find a place to eat Chinese in the cheap price range.
SYSTEM: I have 3 chinese restaurants located in city centre that meet your price range request. Can I book one for you?
USER: Not today, can you recommend one of them to me?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: food - chinese, pricerange - cheap, 
</example>


<example>
Example 15
The following is the conversation history:
USER: We will be on the west side of town and would like to find a place to eat while there.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - west, 
</example>


<example>
Example 16
The following is the conversation history:
USER: I am looking for a swimming pool here in Cambridge.

Answer: I found the following slots present in the conversation history you have provided:
attraction: type - swimmingpool, 
</example>


<example>
Example 17
The following is the conversation history:
USER: Sure. I am looking for a restaurant near the centre of Cambridge.
SYSTEM: What type of food are you looking for?
USER: I am looking for Eastern European food.
SYSTEM: I'm sorry, there aren't any Eastern European eateries in the centre. Can I check another part of town for you, or look for a different type of cuisine?
USER: Thai food sounds good. Could you check for a restaurant again in the centre of Cambridge?
SYSTEM: Bangkok City is an expensive thai place in the centre of town, would you like more info or a booking?
USER: yes, i'd like the phone number please.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - thai, name - bangkok city, 
</example>


<example>
Example 18
The following is the conversation history:
USER: I am looking for more information regarding the cambridge chop house.
SYSTEM: Sure! That's a great expensive British restaurant in the centre of town. What other information would you like to know?
USER: I guess I just need the address.
SYSTEM: Their address is 1 Kings Parade.
USER: That's all I needed. Thank you!

Answer: I found the following slots present in the conversation history you have provided:
restaurant: name - cambridge chop house, 
</example>


<example>
Example 19
The following is the conversation history:
USER: I would like to get information about some tourist attractions in Cambridge, especially those located in town.
SYSTEM: We have many wonderful attractions in the area. Is there a specific type of attraction or area you are looking for perhaps?
USER: I am looking for a nightclub in the centre and a phone number.

Answer: I found the following slots present in the conversation history you have provided:
attraction: area - centre, type - nightclub, 
</example>


<example>
Example 20
The following is the conversation history:
USER: I need a train that arrives by 11:45 leaving from Ely. Can you help me?
SYSTEM: What day will you be traveling?
USER: I'm leaving on Wednesday.
SYSTEM: Train TR5348 leaves at 05:35 and arrives at 5:52. Is that suitable for you?
USER: Does it go to Cambridge?
SYSTEM: Yes it does.
USER: That's great. Can you make a booking for me for 5 people?
SYSTEM: Booking for 5 people on TR5348 on wednesday at 05:35 going to cambridge was successful. I donothavereservationnumbers at the moment. Cost is 4.40.
USER: I will need the reference number please.
SYSTEM: Booking was successful I will get you the reference number
USER: Okay, I need that. Didn't they give you a reference number when you booked it?
SYSTEM: I apologize for that. The booking number is OWXJ46II and the cost will be 22 GBP.
USER: Thanks. Now please help me find a moderate guesthouse that offers wifi
SYSTEM: There are 14 to choose from. Do you have a preference for area or star rating?
USER: I'd like to stay in Cambridge, but no area or star rating preference. Just the free wifi. Any suggestions?
SYSTEM: I recommend avalon, which is a 4 star lodging in the north.
USER: Okay. Can you book that for me? It will be 5 of us staying there
SYSTEM: Okay. I just need a little bit of information to book that. What day do you want to check in and for how many nights will you stay there?
USER: I will be staying for 3 nights starting Wednesday.
SYSTEM: Sure, your booking was successful. Reference number is 1E4YWFGS . Can I help with anything else?
USER: That's all for now! Thank you, have a good day!

Answer: I found the following slots present in the conversation history you have provided:
hotel: bookday - wednesday, bookpeople - 5, bookstay - 3, internet - yes, name - avalon, pricerange - moderate, type - guesthouse, 
train: arrive - 11:45, bookpeople - 5, day - wednesday, departure - ely, destination - cambridge, 
</example>


<example>
Example 21
The following is the conversation history:
USER: Hi, I am looking for architectural churches in the Cambridge area. Can you assist?
SYSTEM: I have several churches listed, although none shown as architectural. May I offer a list for your consideration?
USER: Yes that would be great.
SYSTEM: It appears that there are not any located in Cambridge. Would you like me to find you one outside of Cambridge?
USER: Sorry, I needed to find a museum in town. Can you help me with that instead?
SYSTEM: I recommend Byard Art Gallery in the south. It's free to get in!
USER: Could I have the phone number please? I also need a train leaving from Cambridge and going to Birmingham New Street on Saturday, leaving by 13:15.
SYSTEM: 011223464646, is the phone. When will you travel?
USER: I will travel on Saturday.

Answer: I found the following slots present in the conversation history you have provided:
attraction: type - museum, 
train: day - saturday, departure - cambridge, destination - birmingham new street, leave - 13:15, 
</example>


<example>
Example 22
The following is the conversation history:
USER: There aren't any Polish restaurants in the centre, are there?
SYSTEM: Sorry there is not. How about another choice of food ?
USER: how about chinese?
SYSTEM: We have many Chinese restaurants! What's your price range?
USER: I'm not fussy about price, pick one for me and give me the address please, I'm starving!
SYSTEM: Rice house is located at 88 Mill Road City Centre. Would you like for me to book a reservation?
USER: Just the address is all I needed for now. But could you also help me find a train?
SYSTEM: Definitely! Can you give me some more specifics so I can help?
USER: I am going to London kings cross.
SYSTEM: And what is your arrival destination and time of travel?
USER: Leaving Cambridge to London kings cross and arrive by 19:45.
SYSTEM: Ok, on what day will that be?
USER: I need to leave on Tuesday.
SYSTEM: TR0315 arrives at 13:51. is that fine with you?
USER: what is its departure time?
SYSTEM: It leaves Cambridge at 13:00.
USER: Time I leave does not matter I just need it to arrive by 19:45.
SYSTEM: I have a train departing Cambridge at 17:00 and arriving at London Kings Cross at 17:51. I don't have a later arrival time on Tuesday, unfortunately.
USER: Alright. Could you please provide me with the train ID and the travel time?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - chinese, 
train: arrive - 19:45, day - tuesday, departure - cambridge, destination - london kings cross, 
</example>


<example>
Example 23
The following is the conversation history:
USER: I'd like to find a Turkish restaurant in the center of town.
SYSTEM: I have three Turkish restaurants in the centre of town. Are you looking for a specific price range?
USER: An expensive restaurant would be nice.
SYSTEM: Then the Meze Bar Restaurant is the one for you. Would you like a reservation?
USER: Yes please, can I reserve for 6 people at 12:15 on tuesday?
SYSTEM: Your table for 6 has been booked on Tuesday. Can I help you with something else?
USER: Could I have the reference number please

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - tuesday, bookpeople - 6, booktime - 12:15, food - turkish, name - meze bar restaurant, pricerange - expensive, 
</example>


<example>
Example 24
The following is the conversation history:
USER: I'm looking for a North African restaurant.
SYSTEM: I'm sorry but it looks like I don't happen to see any restaurants that specialize in that type of cuisine? Can I help you with a different type?
USER: How about something in the expensive price range instead?
SYSTEM: Sure, there are 57 expensive restaurants in town. Is there an area of town you'd prefer?
USER: I would prefer something near the centre please.
SYSTEM: There are over 33 restaurants that meet your criteria. May I interest you in African cuisine since you originally asked for North African restaurant?
USER: No, I think I'd like an expensive French restaurant instead.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - french, pricerange - expensive, 
</example>


<example>
Example 25
The following is the conversation history:
USER: I am looking for yippee noodle bar.
SYSTEM: Yippee Noodle Bar is at 40428 King Street City Centre. Would you like to make a reservation?
USER: Yes please. I need a reservation for 6 people at 16:15 on Thursday.
SYSTEM: Got it! your reservation is confirmed for Thursday at 16:15 for 6 people. your reference number is C73DB4I8 .
USER: I'm also looking for places to go in town.
SYSTEM: There are 79 different attractions in town. Do you have a specific area or type of attraction that you are looking for?
USER: Yes, I'm very interested in visiting a history museum. Is there a museum closer to the Yippee noodle bar or possibly within 5 to 8 miles is okay also
SYSTEM: Broughton house gallery is one in the centre of town, would that work?
USER: Yes. Can I please get a taxi to arrive at the restaurant by the booked time of 16:15?

Answer: I found the following slots present in the conversation history you have provided:
taxi: arrive - 16:15, destination - yippee noodle bar, 
restaurant: bookday - thursday, bookpeople - 6, booktime - 16:15, name - yippee noodle bar, 
attraction: area - centre, type - museum, 
</example>


<example>
Example 26
The following is the conversation history:
USER: Can you help me find a museum to visit?
SYSTEM: I can. Does location matter?
USER: No, it does not matter. You can make a suggestion and provide the address and postcode.
SYSTEM: cambridge and county folk museum located at 2-3 Castle street. 3.50 pounds to get in, but well worth it.Check out the gift shop too.
USER: Can I have the postcode, please?
SYSTEM: The postcode is at cb30aq
USER: Thanks much! Oh and I'd also like to find a place to dine in the centre. Can you help me with that too?
SYSTEM: Absolutely. What sort of cuisine would you like?
USER: I'd like modern American in the moderate price range, if possible?
SYSTEM: I have none that match your criteria. May I suggest a different area or food type?
USER: If you don't have any Modern American places, maybe Modern European?
SYSTEM: There are 2 modern European restaurants.
USER: Could you pick one and give me the postcode and phone number?
SYSTEM: Sure thing here you go 01223259988 and cb21rt.
USER: What is the address?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - modern european, pricerange - moderate, 
attraction: type - museum, 
</example>


<example>
Example 27
The following is the conversation history:
USER: I am looking for bistro food.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: food - bistro, 
</example>


<example>
Example 28
The following is the conversation history:
USER: I am coming to Cambridge soon to see the many local attractions.
SYSTEM: I have various attractions all over town. Is there a specific area you are wanting to find something to do?
USER: Well, first I need to find a place to stay. I need a hotel in the south part of town with free parking.

Answer: I found the following slots present in the conversation history you have provided:
hotel: area - south, parking - yes, 
</example>


<example>
Example 29
The following is the conversation history:
USER: I need to find a good vegetarian restaurant
SYSTEM: I'm sorry could you repeat your request? There seems to be an error.
USER: I meant train. I need a train ticket for monday.
SYSTEM: Where did you want to depart from, sir?
USER: I am departing from cambridge and going to bishops stortford.
SYSTEM: There are 5 trains from Cambridge to Bishops Stortford on Monday. Do you want to leave at any certain time?
USER: What is the first train after 11:30?
SYSTEM: TR4861 leaves at 13:29
USER: Could you give me the arrival time and price also please?

Answer: I found the following slots present in the conversation history you have provided:
train: day - monday, departure - cambridge, destination - bishops stortford, leave - 11:30, 
</example>


<example>
Example 30
The following is the conversation history:
USER: I'm looking for some romanian food around here.
SYSTEM: I'm sorry, there are no Romanian restaurants available.
USER: Ok, let's try to find an asian oriental restaurant.
SYSTEM: I have five. Is there an area you prefer?
USER: I need a cheap price range.
SYSTEM: I would rcommed the j restaurant, would you like me to book you?
USER: Yes I need a reservation for 6 people at 17:30 on a Saturday.
SYSTEM: Great, I will book that for you now.
USER: I need a confirmation number too thank you

Answer: I found the following slots present in the conversation history you have provided:
restaurant: bookday - saturday, bookpeople - 6, booktime - 17:30, food - asian oriental, pricerange - cheap, 
</example>


<example>
Example 31
The following is the conversation history:
USER: I'm looking for an expensive restaurant in the west.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - west, pricerange - expensive, 
</example>


<example>
Example 32
The following is the conversation history:
USER: Please help me arrange for a taxi
SYSTEM: Where is your departure site?
USER: I'd like to leave aylesbray lodge guest house by 12:15
SYSTEM: Ok, and what is your destination please?
USER: I'm going to ask.

Answer: I found the following slots present in the conversation history you have provided:
taxi: departure - aylesbray lodge guest house, leave - 12:15, 
</example>


<example>
Example 33
The following is the conversation history:
USER: I'm looking for a pleasant guesthouse to stay in. Would you be able to help me find one?
SYSTEM: Sure! What area would you like to stay?
USER: I would like to stay in the north. I would also like the guesthouse to have free parking and wifi.
SYSTEM: How about the acorn guesthouse?
USER: It has free parking and wifi? Sounds great.
SYSTEM: How many nights would you like to book it for?
USER: Just get me their phone number.
SYSTEM: The phone number is 01223353888.
USER: Thanks. I could also use some help finding out about a train going into Cambridge.
SYSTEM: I will need departure city, time of arrival or departure and day of travel please.
USER: Day of travel is Tuesday and departure city is Ely and to arrive by 12:45

Answer: I found the following slots present in the conversation history you have provided:
hotel: area - north, internet - yes, parking - yes, type - guesthouse, 
train: arrive - 12:45, day - tuesday, departure - ely, destination - cambridge, 
</example>


<example>
Example 34
The following is the conversation history:
USER: I am going to visit and would like to go to a nightclub. Any suggestions?

Answer: I found the following slots present in the conversation history you have provided:
attraction: type - nightclub, 
</example>


<example>
Example 35
The following is the conversation history:
USER: I'd like to find an attraction to visit. Something in the west.
SYSTEM: Okay, what type of attraction would you like to see?
USER: I would like to see a theater.
SYSTEM: I don't show any listings for theaters in the west would you like to search for another attraction?
USER: am also looking for a restaurant. The restaurant should serve south african food and should be in the moderate price range
SYSTEM: Unfortunately there are no restaurants that serve South African dishes on the West side, would you like me to try a different side of town?
USER: How about one that serves South African food?
SYSTEM: Unfortunately there are no restaurants that serve South African dishes on the West side, would you like me to try a different side of town?
USER: no but how about one that serves british food.
SYSTEM: The Saint Johns Chop House is moderately priced, serves British cuisine, as in the west part of town. Shall I book this for you?
USER: Yes, can you please book this for me?
SYSTEM: How many people and what day?
USER: I'm not ready to book yet. Can I get the phone number, postcode, and address, please?
SYSTEM: The address for Saint Johns Chop House is 21 - 24 Northampton Street, cb30ad. The phone number is 01223353110. Is there anything else that I can assist you with?
USER: Yes I need an attraction in the west. Anyone will do. Whatever you recommend.
SYSTEM: clare hall is a college with free admission. Their number is 01223332360.
USER: I also need a south african restaurant.
SYSTEM: I am sorry none are listed in that area, something else perhaps?
USER: Is there a restaurant in the west that serves British food?
SYSTEM: Yes, Saint Johns Chop House is available. Would you like to book a table?
USER: Not at this time. Can you give me the phone number, address and postcode, please?
SYSTEM: Saint Johns Chop House is located at 21-24 Northampton Street, postcode cb30ad. You can reach them by phone at 01223353110. Can I help you find anything else today?
USER: That is all, thanks.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - west, food - british, name - saint johns chop house, pricerange - moderate, 
attraction: area - west, 
</example>


<example>
Example 36
The following is the conversation history:
USER: I am traveling to Cambridge and would like to find a local restaurant. I want to arrive by train at noon.
SYSTEM: Hi there, let's start with the train arrival, where would you be travelling from?
USER: I am looking for a train that will depart from Norwich on Sunday
SYSTEM: There are trains every hour on the :16 that will get you there by noon, beginning at 5:16. Which would you prefer?
USER: How about 7:16? What is the price?
SYSTEM: TR4202 is the one that leaves at 7:16 and it costs 14.08 pounds per ticket. Would you like me to book it for you?
USER: Yes that would be great. I am also looking for a place to dine for the night. Do you have any suggestions?
SYSTEM: My recommendation would be the Ugly Duckling, a Chinese restaurant in the centre of town. It is located at 12 St. Johns Street City Centre.
USER: Is the restaurant moderately priced? If so, please book a table for 5 at 18:00 and send me the reference number.
SYSTEM: No, I'm sorry the ugly duckling is in the expensive price range. The copper kettle serves british food and is moderately priced. Would you like a reservation for it?
USER: The copper kettle will be fine. Yes please book a reservation.
SYSTEM: Sure thing! Your table is reserved. Your reference number is OY2LNXFW . Is there anything else I can assist you with today?
USER: No, that will be all. Thanks!

Answer: I found the following slots present in the conversation history you have provided:
restaurant: bookday - sunday, bookpeople - 5, booktime - 18:00, name - copper kettle, pricerange - moderate, 
train: arrive - 12:00, day - sunday, departure - norwich, destination - cambridge, 
</example>


<example>
Example 37
The following is the conversation history:
USER: Would you be so kind as to help me find a place to dine later?
SYSTEM: I sure can. What type of restaurant are you looking for?
USER: I'm looking for Cuban food.
SYSTEM: There are no Cuban restaurants unfortunately.
USER: That's okay. How about Indian?
SYSTEM: Yes what area are you looking to dine in?
USER: In the Centre as well please.
SYSTEM: I have 9 restaurants available. What price range would you prefer?
USER: The range does not matter. Just the Indian place you think best.
SYSTEM: I would recommend the The Golden Curry. Would you like to make a reservation?
USER: Yes, let's make it for 1 person at 19:45 on sunday.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - sunday, bookpeople - 1, booktime - 19:45, food - indian, name - golden curry, 
</example>


<example>
Example 38
The following is the conversation history:
USER: Hi. I'm trying to find a good restaurant in the south part of town.
SYSTEM: There are several good restaurants in the south part of town. Do you have a preference for the type of food or price range?
USER: Yes, I'd like a restaurant that serves portuguese food.
SYSTEM: nandos is the only restaurant i can find in the south that serves portuguese.
USER: Nandos sounds great. Thank you.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - south, food - portuguese, 
</example>


<example>
Example 39
The following is the conversation history:
USER: Hi! I am looking for a turkish food restaurant around the centre.
SYSTEM: There are 3 Turkish restaurants in the centre. Would you prefer expensive or moderate price range?
USER: Moderate price range would be fine. Could you pick the shortest name and tell me the address?
SYSTEM: Anatolia is located at 30 Bridge Street City Centre.
USER: Thank you! I am also looking for a 5 star hotel.
SYSTEM: There are no 5 star hotels, do you want to choose something else
USER: Yes, can you find a place for me with free wifi in the moderate price range?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - turkish, pricerange - moderate, 
hotel: internet - yes, stars - 5, type - hotel, 
</example>


<example>
Example 40
The following is the conversation history:
USER: I am looking for a train. The train should leave on tuesday and should depart from peterborough
SYSTEM: There are several trains that meet that criteria. What destination are you looking for?
USER: I need to leave from Peterborough.
SYSTEM: How about TR5042 that arrives at 05:19?
USER: I'd like to arrive by 10:45, do you have something close to that time?
SYSTEM: There are several trains that meet that criteria. what time would you like to depart?
USER: Departure time doesn't matter, just want to arrive by 10:45 so whatever is closest to that arrival time.
SYSTEM: Great, I have a train that meets your criteria. Would you like me to book it for you?
USER: Wait, does this train go to Cambridge? That's my destination.
SYSTEM: Yes I have a train that arrives at Cambridge on tuesday at 10:38 would you like me to book that for you?
USER: Yes please book it.

Answer: I found the following slots present in the conversation history you have provided:
train: arrive - 10:45, day - tuesday, departure - peterborough, destination - cambridge, 
</example>


<example>
Example 41
The following is the conversation history:
USER: Hi, I'm interested in finding something to do on the north end of town. Are there any boats there that I might be able to visit?
SYSTEM: Yes, the riverboat georgina operates out of that area. Would you like me to provide any additional information?
USER: Yes please. I would like to get the address and postcode for the riverboat.
SYSTEM: Certainly, their address is cambridge passenger cruisers, jubilee house and their postcode is cb43ax.
USER: Ok, I need a restaurant in the north side that serves chinese as well.
SYSTEM: There are 3 options for Chinese food on the North side. Would you prefer one that is moderately priced or an expensive one?
USER: Whichever one would be able to be booked for 4 people at 13:00 on thursday.
SYSTEM: Hakka has been booked, reference number is P1MMD3MO
USER: Thank you. I'll need a taxi to get me to the restaurant.

Answer: I found the following slots present in the conversation history you have provided:
taxi: arrive - 13:00, destination - hakka, 
restaurant: area - north, bookday - thursday, bookpeople - 4, booktime - 13:00, food - chinese, name - hakka, 
attraction: area - north, name - riverboat georgina, type - boat, 
</example>


<example>
Example 42
The following is the conversation history:
USER: I need to book a train departing from Cambridge.
SYSTEM: Sure, I can help you with that. Where were you wanting to travel to and when were you looking to depart?
USER: I need to leave Cambridge and go to Broxbourne on Wednesday after 15:45.

Answer: I found the following slots present in the conversation history you have provided:
train: day - wednesday, departure - cambridge, destination - broxbourne, leave - 15:45, 
</example>


<example>
Example 43
The following is the conversation history:
USER: I am looking for a restaurant that serves indian food.
SYSTEM: In what area of town would you like to eat?
USER: In the centre of town please. I am looking to stay in the expensive price range.
SYSTEM: Great, there are 6 restaurants that meet your criteria. I would suggest Curry Garden. Can I book it for you?
USER: Yes, could you please book it for 6 people at 14:30 on tuesday?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, bookday - tuesday, bookpeople - 6, booktime - 14:30, food - indian, name - curry garden, pricerange - expensive, 
</example>


<example>
Example 44
The following is the conversation history:
USER: I'm looking for a train for my trip to Cambridge. I need it to leave on Monday and to depart from Peterborough. Can you give me some times?
SYSTEM: Sure, there are plenty of available time starting at 05:19 and going all day. Was there a particular time of day you wanted to depart?
USER: I want to arrive at or a little before 12:15, please.
SYSTEM: TR0919 leaves Peterborough at 11:19 and arrives at 12:09. Would you like to book seats on that one?
USER: How long is the travel time. My math is not the best.
SYSTEM: My math isn't the best either but the travel duration is 50 minutes. I can help you book a seat on the TR0919 if you'd like.
USER: I am also looking for a hotel called Archway House.

Answer: I found the following slots present in the conversation history you have provided:
hotel: name - archway house, 
train: arrive - 12:15, day - monday, departure - peterborough, destination - cambridge, 
</example>


<example>
Example 45
The following is the conversation history:
USER: Hello. I'm leaving the city on Wednesday and need to find a train, but it must be after 13:00. Can you help me book a ticket?
SYSTEM: There are over 100 different trains available, what destination do you have in mind?
USER: I would like to go to cambridge from london liverpool street.

Answer: I found the following slots present in the conversation history you have provided:
train: day - wednesday, departure - cambridge, destination - london liverpool street, leave - 13:00, 
</example>


<example>
Example 46
The following is the conversation history:
USER: I'd like to find a cheap Indonesian restaurant. Can you help?
SYSTEM: Unfortunately, we do not have any Indonesian restaurants. Would you like Thai food?
USER: What kind of restaurants are in the west that's cheap?

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - west, pricerange - cheap, 
</example>


<example>
Example 47
The following is the conversation history:
USER: Can I please get a train ticket from Norwich to Cambridge?

Answer: I found the following slots present in the conversation history you have provided:
train: departure - norwich, destination - cambridge, 
</example>


<example>
Example 48
The following is the conversation history:
USER: I'm traveling to cambridge and I need a train that leaves on friday.
SYSTEM: Where will you be coming from, and what time would you like to depart from there?
USER: I'd like to get on the train at London Kings Cross and arrive in Cambridge by 15:15.
SYSTEM: TR4748 leaves Kings Cross at 13:17 and arrives at 14:08. Will that work?
USER: That sounds perfect! Can I purchase 3 tickets on that train, please?

Answer: I found the following slots present in the conversation history you have provided:
train: arrive - 15:15, bookpeople - 3, day - friday, departure - london kings cross, destination - cambridge, 
</example>


<example>
Example 49
The following is the conversation history:
USER: I am looking for a moderately priced restaurant that serves indian food.
SYSTEM: There are 4 restaurants to choose from. Do you have a part of town you prefer?
USER: Yes, I'd like the restaurant to be in the centre.

Answer: I found the following slots present in the conversation history you have provided:
restaurant: area - centre, food - indian, pricerange - moderate, 
</example>


<example>
Example 50
The following is the conversation history:
USER: i am looking for places to go in town. The attraction should be in the centre and should be in the type of theatre.

Answer: I found the following slots present in the conversation history you have provided:
attraction: area - centre, type - theatre, 
</example>
</examples>
"""