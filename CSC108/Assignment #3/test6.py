def process_data(twitter_data):
    """(file open for reading) -> Twitterverse dictionary
    
    Read the file and return the data in the Twitterverse dictionary format. 
    
    """
    twitter_line = twitter_data.readlines()
    Twitterverse_dictonary = {}
    username_list = get_username(twitter_line)
    list_of_profile = get_profile_dictionary(twitter_line)
    for i in range(len(username_list)):
        for k in range(len(list_of_profile)):
            Twitterverse_dictionary[i] = list_of_profile[k]
    return Twitterverse_dictionary
        
def get_next(index):
    """
    """
    index = twitter_line.index('END\n', index + 1,)
    return index

def get_end(twitter_line):
    """(list of str) -> list of int
    
    Returns the index value of all the 'END\n' within the twitter data
    """
    inverse_end = twitter_line[::-1]
    inverse_last_end = twitter_line[::-1].index('END\n')
    last_end = len(twitter_line) - 1 - inverse_end.index('END\n')
    last_two_end = len(twitter_line) - 1 - inverse_end.index('END\n', inverse_last_end + 1)    
    end_list = []
    i = twitter_line.index('END\n')
    while i < last_end:
        end_list.append(i)
        i = get_next(i)
    end_list.append(last_end)
    return end_list

def get_username(twitter_line):
    """(list of str) -> list of str
    """
    username_list = []
    end = twitter_line.index('END\n')
    last_two_end = len(twitter_line) - twitter_line[::-1].index('END\n', end) - 1
    i = 0
    for i in range(last_two_end + 2):
        u = twitter_line.index('END\n', i) + 1
        username_list.append(u)
        i = u
    return username_list

def get_user_profile(twitter_line):
    """(list of str) -> list of list of str
    """
    user_profile = []
    end_list = get_end(twitter_line)
    for c in range(len(end_list) - 3):
        user_profile.append(twitter_line[end_list[c] + 2 : end_list[c + 1]])
        c = c + 1
    return user_profile