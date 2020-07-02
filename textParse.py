import spacy

nlp = spacy.load("en_core_web_sm")

text = ("""
TL;DR: eBuddy is a messaging platform, which supports mobile apps and web interface for sending messages through the Internet as an SMS replacement, and features media messaging, location discovery of other contacts, and several other features.  

 

Cassandra is eBuddy’s primary database for several different services.  Including for their user data and discovery service for finding new contacts, as well as their persistent sessions storage.  In addition, eBuddy uses Cassandra for message history and for a Geo Hashing database for location discovery so that you can find people nearby that are using the messaging application.

 

eBuddy considered HBase as a possibility and finally decided on Cassandra for a number of reasons — it’s written in Java, it’s open source, it’s easy to add and remove nodes, and the initial setup was easy. 

 

Today we have Eric Zoerner Senior Software Developer at eBuddy.  Eric, thank you so much for joining us.  I’m really looking forward to learning about how you’re using Cassandra.  To start things off could you tell us a little bit about what eBuddy does?

Yes, eBuddy has a messaging platform, which supports apps on smart phones and a web interface for sending messages through the Internet as an SMS replacement, and features media messaging, location discovery of other contacts, and several other features.  We are now focusing on supporting group conversations with control over sharing your media and locations. It’s a hybrid social app with a messaging app.

 

Excellent.  Is that cross-platform as well? 

Yes, we currently support iPhone, Android and the Web.

 

So how is Cassandra incorporated into the mix there at eBuddy?

We use Cassandra as our primary database for several different services.  We also use MySQL, and Hadoop for data warehousing.  For Cassandra we use it for our user data and our discovery service for finding new contacts is built on top of that, and we also use Cassandra for our persistent sessions storage.  In addition we use it for message history and for a Geo Hashing database for location discovery so that you can find people who are nearby that are using XMS, which is the name of our messaging application.

 

Very interesting.  So it stores the actual location then in Cassandra?

Yes, using Geo Hashing we store the hash of grids based on latitude and longitude.

 

Very cool.  Was there another technology that you had evaluated or compared Cassandra against before going with Cassandra?

Yeah we also took a close look at HBase as a possibility and finally decided on Cassandra for a number of reasons—it’s written in Java, it’s open source and it’s very easy to add and remove nodes. Easy setup was one of the big things for me in that it is so easy to just get up and running compared to some other solutions.  We also use Hadoop in our company but we use that for our data warehouse,  a very different purpose.

 

Could you share with us a little bit about what your deployment looks like?

We basically have three different classes of machines that we use in three different clusters.  One is our user data service where we use four hosts and have a replication factor of three.  That’s with an eight core with hyperthreading RAID 10 discs and 48 gigs of RAM.  That is part of the same cluster with our data warehouse machines, which is actually only one machine, but in a separate data center.  We use that for calculating second-degree suggestions.  We also use Neo4J there in conjunction with that for graph calculations.  That machine is SSD drives 2.1 terabyte, and 48 gigs of RAM.  Then we have our persistent session store cluster, which is four machines, 64 gigs, 12 cores with hyperthreading and also SSDs two 256 gig SSDs.

 

Are you currently utilizing a multi data center replication then?

Only for our data warehouse.  We have our user data cluster, which is also used for message history and that is connected to our data warehouse machine in the same cluster in a separate data center where we just send one replica over to the data warehouse machine so that it can use that information for calculating the second degree suggestions.  Then we use the data with the three replicas as our primary productions database.

 

For someone who’s just getting started with Cassandra what advice do you have for them that is going to be beneficial for their entry into using it?

My advice is just to install it locally and play around with and write some test cases because it’s so easy just to get up and running that it’s very little effort to do so, and to just use it is my best advice.  Start your development with it play around with it.

 

I think that’s all the questions that I have for you today but before we sign off here is there anything else that you would like to add about Cassandra or eBuddy?  

I think it’s been a positive experience to host the meet-ups at eBuddy and meet other people that are using Cassandra, and the Netherlands, and Amsterdam.  We’ve had people come from other cities in the Netherlands to give presentations on what they’re doing and it’s just been very satisfying to see other people coming and being able to network in that way, and to get questions answered.  The support from Datstax has also been very good. Hayato Shimizu and John Glendenning came from London to our meet-up. That was a very positive thing and I think it attracted more people to come to our meet-up.  Yeah it’s very good.

 

Definitely.  If there’s anything else you’d like to add, share with the readers today?

I guess I am just looking forward to seeing the new features that are coming, especially nested collections and user data types. I think those are really cool features so I’m looking forward to working with them.

 

Very cool.  We’re looking forward to all the other upcoming updates as well.  Thank you so much for joining us today.

You’re welcome.  
""")

doc = nlp(text)

for entity in doc.ents:
    print(entity.text, entity.label_)