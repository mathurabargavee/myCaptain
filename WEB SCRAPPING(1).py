# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:30:40 2021

@author: Mathura
"""


import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


parser=argparse.ArgumentParser()
parser.add_argument("--page_num_MAX",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the name of db",type=str)
args=parser.parse_args()

oyo_url="https.//www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX=args.page_num_MAX
scraped_info_list=[]
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url=oyo_url + str(page_num)
    print("GET Request for: " + url)
    req=requests.get(url
    content=req.content
    
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        #try..except
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None
            
    amenities_list=[]
    parent_amenities_element=hotel.find("span",{"class":"amenityWrapper"})
    for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
        amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
    
    hotel_dict["amenities"]=','.join(amenities_list[:-1])
    
    scraped_info_list.append(hotel_dict)
    connect.insert_into_table(args.dbname,tuple(hotel_dict.values()))
        
        
        
        
    
