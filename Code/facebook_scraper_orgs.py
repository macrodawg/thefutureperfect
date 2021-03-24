# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:04:06 2021

@author: Danielle Handel
"""

## This code scrapes name, post id, shares, detailed reactions, comments, text 
## content, post times, photo, video, and post links from over 40 other successful
## nonprofits tackling child trafficking across the globe



# package to scrape public facebook pages 
from facebook_page_scraper import Facebook_scraper

# alert me when it is done 
import winsound

#list of many 


page_names = ['a21campaign', 'AnnieCannons', 'CASJustice', 'CASTLosAngeles', 'CATWIntl', 
'ChainsInterrupted', 'ChildrensRescueInitiative', 'childrescuecoalition', 
'covenantrescue', 'DeliverFund', 'destinyrescue', 'ecpat', 'fairgirls.org', 
'FreedomNetworkUSA', 'GenerateHope.org', 'globalcenturion', 'gpseattle', 
'HagarInternational', 'hopeforjustice', 'innocentsatrisk', 
'InternationalJusticeMission ', 'irc.alert', 'LocateRescueReturn', 
'love146.org', 'LoveJusticeIntl', 'OURrescue', 'OutofDarknessAtlanta', 
'polarisproject', 'projectrescue', 'ratanakinternational', 
'sharedhopeinternational', 'STOPTHETRAFFIK', 'theasservoproject', 
'TheExodusRoad', 'thelifeguardgroup', 'truckersagainsttrafficking', 
'UnitedAbolitionists', 'UnlikelyHeroes.LoveIsHeroic ', 
'voicesagainstchildtrafficking', 'WeAreUnseen', 'ZOEChildren']

posts_count = 2500
browser = "firefox"
directory = r"C:\Users\hande\Documents\Spring 2021\Future Perfect"

# loop over each page and scraoe as much as possible (fb will only allow up to 20 it seems)

for page_name in page_names:
    facebook_posts = Facebook_scraper(page_name,posts_count,browser)
    facebook_posts.scrap_to_csv(page_name + "_scrape", directory)


winsound.MessageBeep()