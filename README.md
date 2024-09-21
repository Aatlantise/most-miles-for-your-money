# most-miles-for-your-money (M3)

Not for the faintest of hearts...and backs. This tool for those who prefer multi-stop flight itineraries ensures you'll get you the most miles for your money.

### The flexible low-income traveler

I am a PhD student.
That means I am fortunately flexible with my schedule, and unfortunately low-income.
I also consider myself gifted in sleeping in economy seats.

These features mix well in air travel, since flexible schedules allow room to choose from a wider selection of more inexpensive fares.
Fares often ridden with layovers, airport changes, and nights at the terminal.

Between an expensive direct long-haul and a much cheaper itinerary that goes the other way around the earth, sign me up for the latter!

This is a tool for exactly that--getting the most miles for your money.
Instead, you pay with your time, stress, and energy.

###  Case study

Let's consider a round trip from {WAS, PHL, NYC} to {SEL, PUS}.
Departure anytime after Dec 11 (day after the last day of fall) and return anytime before Jan 7 (day before first day of spring).
Holiday travel is not exactly cheap--a quick Google Flights search returns a nonstop round-trip on Korean Air, IAD-ICN,  for around $3,000. No way.

Another search offers a more reasonable alternative, a round trip on Finnair, JFK-ICN via HEL, for around $1,700.
More reasonable yes, but not reasonable enough.

Let's see if I can find two one-ways for cheaper.
A Dec 11 one-way fare from PHL to FUK is out for $580.
United PHL-IAH and, get this, ANA IAH-HND-FUK!
ANA economy is as premium economy economy seats can get, with a whopping 34 inches of pitch.
That's 6 more than what Iberia offers on their domestic short-haul.
From FUK, PUS is a short 20 minute, $50-80 flight, or a $30 ferry ride away.
I should note I will have to spend a night in FUK, however.

One the return leg, we can do something crazier.
Jan 6 ICN-CDG is $404 on Qatar, another 5-star airline.
There is an overnight stopover in DOH.
From CDG, JFK is a $230 Norse Atlantic flight away the same day, bags included.
From JFK, it'll be around $30 to get to home in Arlington, VA.
Round trip for a total of around $1,300, and a lot of miles too!

### The missing link in Google Flights

Google Flights is great, but doesn't really offer many of these "self-transfer" itineraries reliably, unless it's offered by one of the OTAs like kiwi.
Skyscanner is a bit better, but doesn't seem to have access to all fare types.
When I do something like this, I end up always searching over endless combinations of departure, arrival, layover airports.
It's fun, and you learn about interesting fifth freedom flights like Singapore FRA-JFK, Ethiopian ICN-NRT, but takes a lot of time and mental real estate.
I want to see if this can be automated.

### How MMM works

For now, it takes one argument--date of travel.
Departure and arrival airports are fixed at either Korea (ICN, GMP, PUS, CJJ, CJU) and the eastern United States (JFK, LGA, EWR, PHL, BWI, DCA, IAD).
It performs a nested search through a predetermined list of airports, and returns a most-miles-for-your-money itinerary.
