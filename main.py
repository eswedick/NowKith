import praw
import pprint

def main():
    user_agent = "NowKithMikeTyson 0.0 by /u/redleader6432"
    r = praw.Reddit(user_agent=user_agent)

    user_name = "redleader6432"
    user = r.get_redditor(user_name)

    thing_limit = 10
    subreddit = r.get_subreddit('bestof')
    for submission in subreddit.get_hot(limit=10):
        print(submission.url)



def test():
    user_agent = "NowKithMikeTyson 0.0 by /u/redleader6432"
    r = praw.Reddit(user_agent=user_agent)

    user_name = "redleader6432"
    user = r.get_redditor(user_name)

    thing_limit = 10

    gen = user.get_submitted(limit=thing_limit)
    com = user.get_comments(limit=thing_limit)

    karma_by_subreddit = {}
    comments = {}

    for thing in gen:
        subreddit = thing.subreddit.display_name
        karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

    for thing in com:
        subreddit = thing.subreddit.display_name
        comments[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

    print('Submitted:')
    pprint.pprint(karma_by_subreddit)

    print('Comments:')
    pprint.pprint(comments)




    #get top submissions
    #for each submission in submissions
        #processComments

    #processComments
    #select top x comments
        #search thru tree for "Now Kiss"
            #postJones(commentid)

    #postJones
    #post reply with .jpg


if __name__ == '__main__':
    main()