import requests
from bs4 import BeautifulSoup
import pandas as pd
import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from encodings.aliases import aliases
import os

stop=wordcloud.STOPWORDS
wc=WordCloud(background_color='black',stopwords=stop,height=1000,width=800)
inp=input("Enter your url: ")
file_type=os.path.splitext(inp)[1]
print(file_type)
if file_type=='':
            print('Now at url session')
            req=requests.get(inp)
            soup=BeautifulSoup(req.content,"html.parser")

            r=soup.get_text() 
            try:
                    wc.generate(r)
                    wc.to_file('path/to/the/folder/wordcloud.png')
                    cloud=wc.generate(r)
                    plt.imshow(cloud,interpolation='bilinear')

                    plt.axis('off')
                    plt.show()

            except ValueError:
                        print("Error!!!...Got 0 words to plot..")
                    
elif file_type=='.txt':
        
            for i in set(aliases.values()):
                                  try:
                                    text=open(inp,mode='r',encoding=str(i)).read()
                                    break
                                  except:
                                         pass
                    
            cloud=wc.generate(text)
            cloud.to_file('path/to/the/folder/wordcloud.png')
            plt.imshow(cloud,interpolation='bilinear')
            plt.axis('off')
            plt.show()
          
