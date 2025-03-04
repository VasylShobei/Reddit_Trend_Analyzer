import praw
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

reddit = praw.Reddit(
    client_id="ekfFXTwzHVGM2DL5qHzfpg",
    client_secret="wdbs0o2pFK8WqQg7uOIM12EIf3ShVw",
    user_agent="my_trend_analyzer"
)

subreddit_name = "technology"

posts = reddit.subreddit(subreddit_name).top(time_filter="week", limit=50)

titles = [post.title for post in posts]

words = " ".join(titles).lower()

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(words)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title(f"Trending Words in r/{subreddit_name} (Last 24h)")
plt.show()

df = pd.DataFrame({"Title": titles})
df.to_csv(f"{subreddit_name}_trending.csv", index=False)

print(f"Trending data saved to {subreddit_name}_trending.csv")
