# loading all necessary libraries
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

year: str = "2015"
# Load in the dataframe
df = pd.read_csv("C:\\Users\\beniv\\OneDrive\\שולחן העבודה\\big data final\\" + year + "_graph.csv", index_col=0)
# Looking at first 5 rows of the dataset
# print(df.head())

print(df[["words", "num_appearance"]])
# Group by by country
country = df.groupby("words")

# Summary statistic of all countries
plt.figure(figsize=(15, 10))
country.mean().sort_values(by="num_appearance", ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.tick_params(axis='x', which='major', labelsize=6)
plt.xlabel("words")
plt.ylabel("frequency")
plt.title(year)
plt.savefig("C:\\Users\\beniv\\OneDrive\\שולחן העבודה\\big data final\\plot" + year + ".png")
plt.show()

text = " "
for i in range(0, len(df)):
    text = text + ((df["words"].values[i] + " ") * df["num_appearance"].values[i])

stopwords = set(STOPWORDS)
stopwords.update(["may", "used"])
# Create and generate a word cloud image:
wordcloud = WordCloud(stopwords=stopwords, collocations=False).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
# Save the image in the img folder:
wordcloud.to_file("C:\\Users\\beniv\\OneDrive\\שולחן העבודה\\big data final\\black_worldcloud" + year + ".png")

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(stopwords=stopwords, max_font_size=80, max_words=180, background_color="white",
                      collocations=False).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("C:\\Users\\beniv\\OneDrive\\שולחן העבודה\\big data final\\white_worldcloud" + year + ".png")
