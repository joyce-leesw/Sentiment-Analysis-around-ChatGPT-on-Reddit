import pandas as pd

def get_top_posts(reddit, subreddit_list, limit = 1000, time_filter='all'):
  submissions = reddit.subreddit(subreddit_list).top(time_filter= time_filter, limit= limit)

    # initialise a dataframe to store all the scraped data
  sub_details = []
  for submission in submissions:
    sub_details.append({'post_id': submission.id,
                        'subreddit': submission.subreddit,
                        'created_utc': submission.created_utc,
                        'post_title': submission.title, 
                        'num_comments': submission.num_comments,
                        'score': submission.score,
                        'upvote_ratio': submission.upvote_ratio
                        })
  return pd.DataFrame(sub_details)

# get comments from every post
def get_comments(reddit, sub_df):
  comments_list = [] 
  for post_id in sub_df['post_id']:
    submission = reddit.submission(post_id)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
      comments_list.append({'post_id': post_id,
                          'comment': comment.body})
  return pd.DataFrame(comments_list)

def get_sentiment(text, sentiment_classifier):
    try:
        sentiment = sentiment_classifier(text)[0]['label']
    except:
        sentiment = 'Not classified'
    return sentiment

def get_emotion(text, emotion_classifier):
    pred_score = emotion_classifier(text)
    emotion = max(pred_score[0], key=lambda x:x['score'])['label']
    return emotion