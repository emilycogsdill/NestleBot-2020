from nestlebot_functions import *

import time

def main():
    
    print("getting Twitter API")
    api = get_twitter_api()
    
    # set tweeting time interval
    INTERVAL = 60 * 15 * 1  # tweet every 15 minutes
    #INTERVAL = 30  # every 30 seconds, for testing
    
    while True:
        
        print("Time to tweet - LFG")
        
        #get the freshest list of brands
        brand_list = get_brands()
        
        try:
            #get the image we're gonna tweet
            tweet_image_path, item = get_image(brand_list)
            
            #create and post the tweet
            generate_tweet(tweet_image_path, item, api)
            
            print("Tweeted!!! Back to sleep...")
        
        except:
            print("Tweet failed, RIP. Back to sleep...")
            raise
            pass
        
        #back to sleep zzzzzz
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
    