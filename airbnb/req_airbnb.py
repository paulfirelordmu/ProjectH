import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
title = ['name','bathrooms','bedrooms','beds','person_capacity','preview_amenities',"room_and_property_type","room_type","preview_tags",'price_string','url']
ws.append(title)
response = requests.request('GET', "https://www.airbnb.cn/api/v2/explore_tabs?_format=for_explore_search_web&adults=8&amenities[]=8&auto_ib=true&checkin=2020-09-26&checkout=2020-09-27&currency=CNY&current_tab_id=home_tab&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=20&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=zh&metadata_only=false&min_bathrooms=0&parent_city_place_id=ChIJMzz1sUBwsjURoWTDI5QSlQI&place_id=ChIJL1y5sLn1sjURUYX9ezX0ntY&poi_group=0&poi_tab=shortHaul&query=%E4%B8%8A%E6%B5%B7&query_understanding_enabled=true&refinement_paths[]=%2Fhomes&satori_config_token=EhIiQhIiIjISEjISISIiAA&satori_version=1.1.13&screen_height=787&screen_size=large&screen_width=2560&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&version=1.7.8")
result = response.json()['explore_tabs'][0]['sections']
for i in result:
    listings = i.get("listings", '')
    if listings:
        for l in listings:
            listing = l['listing']
            price = l['pricing_quote']
            apartment = []
            apartment.append(listing['name'])
            apartment.append(listing['bathrooms'])
            apartment.append(listing['bedrooms'])
            apartment.append(listing['beds'])
            apartment.append(listing['person_capacity'])
            apartment.append(listing['preview_amenities'])
            apartment.append(listing["room_and_property_type"])
            apartment.append(listing["room_type"])
            tags = [ p['name'] for p in listing["preview_tags"]]
            apartment.append(' '.join(tags))
            apartment.append(price['price_string'])
            apartment.append("https://www.airbnb.cn/rooms/"+str(listing['id']))
            ws.append(apartment)
wb.save('Project-H.xlsx')