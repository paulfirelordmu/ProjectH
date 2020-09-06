import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
title = ['name','bathrooms','bedrooms','beds','person_capacity','preview_amenities',"room_and_property_type","room_type","reviews_count","avg_rating","preview_tags",'price_string','url']
ws.append(title)
url_list = ["https://www.airbnb.cn/api/v2/explore_tabs?_format=for_explore_search_web&adults=8&amenities[]=8&auto_ib=true&checkin=2020-09-26&checkout=2020-09-27&client_session_id=0c24936d-6d5a-4cd8-9bd6-fdada98570ac&currency=CNY&current_tab_id=home_tab&display_currency=CNY&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=20&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=zh&metadata_only=false&parent_city_place_id=ChIJMzz1sUBwsjURoWTDI5QSlQI&place_id=ChIJL1y5sLn1sjURUYX9ezX0ntY&poi_group=0&poi_tab=shortHaul&price_max=2000&query=上海&query_understanding_enabled=true&refinement_paths[]=/homes&satori_config_token=EhIiQhIiIjISEjISISIiAA&satori_version=1.1.13&screen_height=438&screen_size=large&screen_width=1680&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&version=1.7.8"]
for url in url_list:
    response = requests.request('GET', url)
    result = response.json()['explore_tabs'][0]['sections']
    for i in result:
        listings = i.get("listings", '')
        if listings:
            for l in listings:
                listing = l['listing']
                price = l['pricing_quote']
                apartment = []
                try:
                    name = listing['name']
                    bathrooms= listing['bathrooms']
                    bedrooms = listing['bedrooms']
                    beds = listing['beds']
                    person_capacity = listing['person_capacity']
                    preview_amenities = listing['preview_amenities']
                    room_and_property_type = listing['room_and_property_type']
                    room_type = listing['room_type']
                    tags = [ p['name'] for p in listing["preview_tags"]]
                    price_string = price['price_string']
                    avg_rating = listing['avg_rating']
                    reviews_count = listing['reviews_count']
                    item_id = listing['id']
                    if avg_rating>=4.5 and reviews_count>=10 :
                        apartment.append(name)
                        apartment.append(bathrooms)
                        apartment.append(bedrooms)
                        apartment.append(beds)
                        apartment.append(person_capacity)
                        apartment.append(preview_amenities)
                        apartment.append(room_and_property_type)
                        apartment.append(room_type)
                        apartment.append(avg_rating)
                        apartment.append(reviews_count)
                        apartment.append(' '.join(tags))
                        apartment.append(price_string)
                        apartment.append("https://www.airbnb.cn/rooms/"+str(item_id))
                        ws.append(apartment)
                except Exception as e:
                    print(e)
wb.save('Project-H.xlsx')