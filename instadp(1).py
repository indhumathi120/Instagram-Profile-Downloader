
"""Python provides powerful tools for web scraping of instagram"""

#importing the module instaloader(tool that automatically download picture of given profile from instagram)

import instaloader

#Accessing Instaloader
mod=instaloader.Instaloader()

#getting the input from the user
a=input("enter a profile name")

#downloading the profile using download_profile(only profile pic)
mod.download_profile(a,profile_pic_only=True)
