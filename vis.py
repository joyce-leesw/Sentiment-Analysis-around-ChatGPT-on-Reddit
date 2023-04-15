import matplotlib.pyplot as plt
from wordcloud import WordCloud

# count the number of submissions in each year-month combination
def plot_sub_per_month(sub_df):
    monthly_count = sub_df.groupby(sub_df['created_year_month']).size()
    fig, ax = plt.subplots()
    ax.bar(monthly_count.index, monthly_count.values)
    ax.set_xlabel('Year-Month')
    ax.set_ylabel('Number of Posts')
    ax.set_title('Number of Posts per Month')
    plt.show()

# plot a wordcloud to see the trending words throughout the months
def plot_trending(sub_df):
    post_title_text = ' '.join([title for title in sub_df['post_title'].str.lower()])

    word_cloud = WordCloud(collocation_threshold=2, width=1000, height=500, background_color="white").generate(post_title_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

# plot a wordcloud to see the trending words of the selected year and month
def plot_trending_selected_year(selected_year_month, sub_df):
    posts_in_month = sub_df[sub_df['created_year_month'] == selected_year_month]
    post_title_text_year = ' '.join(item for item in posts_in_month[~posts_in_month['post_title'].isna()]['post_title'])

    word_cloud = WordCloud(collocation_threshold=2, width=1000, height=500, background_color="white").generate(post_title_text_year)

    plt.figure(figsize=(10,5))
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

def plot_sentiment(comments_posts_df):
    sentiment_count = comments_posts_df['sentiment'].value_counts()
    wedgeprops = {'width': 0.9,'linewidth': 1, 'edgecolor': 'white'}
    sentiment_count.plot.pie(autopct='%1.1f%%', wedgeprops=wedgeprops)
    plt.title('Sentiment around ChatGPT')
    plt.show()

def plot_emotion(comments_posts_df):
    emotion_counts = comments_posts_df['emotion'].value_counts()
    ax = emotion_counts.plot.bar()
    ax.set_title('Emotions around ChatGPT')
    ax.set_xlabel('Emotion')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation= 360)
    plt.show()