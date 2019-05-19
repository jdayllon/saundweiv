# SaundWeiv

SaundWeiv is a ecosystem for Social Media Monitoring, it is composed of several items:
* ElasticSearch. Acts as data repository and indexer of social network info.
* Kibana. Gives non-expert users the ability to explore data captured from social networks autonomously
* Kafka. Constitutes the Interoperability substrate between producers and consumers of ecosystem data
* Agents. Obtain and enrich the data obtained from the web (web scrapping) and the APIs
 * Leiserbik. Extracts information from twitter web (https://github.com/jdayllon/leiserbik).

## Why Saundweiv ?

Saundweiv is a phonetical expression of english "SoundWave" a.k.a. Transformers Decepticon which acts as Decepticon Communications Officer (https://en.wikipedia.org/wiki/Soundwave_(Transformers)). It has several "collegues" like Laserbeak or Ramble that follow his orders and make intelligency missions.

## History 

* Current. This the first development version. Several weeks before i was developing a precuel project (https://github.com/jdayllon/TwitterScrapper) with similar focus.

# Launch

You can clone this repository and run the ecosystem using docker and docker-compose launching  `docker-compose up -d`