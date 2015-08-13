import praw
import time
from pprint import pprint

def main():
    user_agent = "NowKith 1.0 by /u/redleader6432"
    r = praw.Reddit(user_agent=user_agent)              #get reddit

    user_name = "NowKithBot"
    r.login(user_name, "M1keTys0nwtcys")
    user = r.get_redditor(user_name)                    #get user

    i = 1
    subreddits = ["funny","pics","AdviceAnimals","todayilearned","aww","me_irl","gifs","videos","gaming","WTF","BlackPeopleTwitter","leagueoflegends","askreddit","DotA2","ShowerThoughts"]
    subreddit = r.get_subreddit('todayilearned')             #get subreddit
    for submission in subreddit.get_hot(limit=50):      #for each hot submission
        print(i,'. ',submission.id)
        checkComments(r, submission.id)                 #check comments
        i += 1

    print("Finished")
    #TODO - time elapsed, total checked/found


def checkComments(reddit, submissionid):
    submission = reddit.get_submission(submission_id = submissionid)    #get submission from id
    #submission.replace_more_comments(limit=15, threshold=20)            #grabs more comments, takes longer

    forest_comments = submission.comments                               #gets comment tree
    flat_comments = praw.helpers.flatten_tree(forest_comments)          #flatten tree for easy searching

    #TODO - method to traverse comment forest more efficiently

    processedComments = 0
    matches = ["Now kiss", "now kiss", "Now kith", "just kiss", "Just kiss"]
    done = []
    for comment in flat_comments:
        if hasattr(comment, 'body'):             #check that this isnt a MoreComments object
            processedComments +=1
            hasMatch = any(string in comment.body for string in matches)
            if submission.id not in done and hasMatch:         #TODO - better string matching
                comment.reply("http://imgur.com/hUNAo")
                done.append(submission.id)
                print("Found kiss instance at:")
                print(comment.permalink)
    
    print("Processed:",processedComments)       #Number of comments checked

    #TODO - add timing for efficiency stats



def test():             #grabs comment/submitted karma breakdown by subreddit
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