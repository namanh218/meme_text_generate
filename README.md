# meme_text_generate
My main purpose:
---
For this demo day, I want something more funny, chill and suitable with my ability. But for real, my project is now working in real life, same idea however with more data and more function and highly accuracy.
Thanks to Ai, now we can do everything, but I really don't know how can they make a joke, predicting next letters or can give people a hint. 

My idea:
---
Nowaday, Internet is so popular. So it's easy to find out a topic for project. I came  to medium.com and found this idea.
With giving me a data with a text from meme database, and the key id for name pictures. We can seperated all the sentence and build a model deep learning.
Unfortunately, they public only 500 sentences with 50 key id it's mean i got 10 sentence for each pic. 
So step by step I did this project followed by this pipeline: get data, clean data, prepare, build model, predict result.

How was i do that:
---
With get data: I downloaded data json from medium, but i need to crawl data from imgflip.com thank to beautifulsoup.
Clean data: For this thing, I had to delete some no meaningful sentences, delete some  noise symbol. I already crawled new data, but they not clean and I had to fix it manually.
Prepare: I seperated labels with all the letters and symbols in my sentences and beside transformed all text to number. Using pad_senquence all text. Labels now became a np.array. Below is my results after seperating text. From 700 samples now I got 30000 samples to train, I split train data to test and validation.
Build model:
---
For text, I think LSTM is good for text and also optimizer by RMSProp, with loss by RMsprop. My model has 256 layer size over 900000 parameters and output using softmax activation.

It's return full text length but you can see some sentences you will found "|" between. The | is mean you have breakdown in that meme. You have to breakdown and make the meme more meaningful.
Now it's Flask app. I am highly recommend using this 4 popular memes: "Is This pigeon", "Surprised pikachu", "Batman slaps Robin", "Expanding brain".
