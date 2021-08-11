from tweetAPI import tweetAPI
from imageAPI import ImageAPI

imageAPI = ImageAPI()
imageAPI.gradient(2)
imageAPI.saveImg('teste.png')
ta = tweetAPI()

ta.postTweet('olha essa imagem que eu gerei \n by the bot', 'teste.png')