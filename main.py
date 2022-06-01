import twint
import nest_asyncio
nest_asyncio.apply()

c = twint.Config()
c.Search = "eurocopa"
c.Lang = "es"
c.Filter_retweets = True
c.Limit = 10000
c.Since = '2021-01-01'
c.Output = "./tweets.json"
c.Min_likes = 5
c.Min_replies = 5
c.Min_retweets = 5
twint.run.Search(c)