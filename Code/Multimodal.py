from gmplot import gmplot
import webbrowser
import os

locations = [{'id': '585069b8ee19ad271e9ba949', 'google_id': 1026201, 'google_parent_id': 21176, 'name': 'Austin', 'canonical_name': 'Austin,Texas,United States', 'country_code': 'US', 'target_type': 'City', 'reach': 6440000, 'gps': [-97.7430608, 30.267153], 'keys': ['austin', 'texas', 'united', 'states']},
    {'id': '584f1826914a8159dc8f4189', 'google_id': 9060225, 'google_parent_id': 21176, 'name': 'Downtown Austin', 'canonical_name': 'Downtown Austin,Texas,United States', 'country_code': 'US', 'target_type': 'Neighborhood', 'gps': [-97.74438630000002, 30.2729209], 'reach': 1180000, 'keys': ['downtown', 'austin', 'texas', 'united', 'states']}, 
    {'id': '66826b75914a81594d5e00ea', 'google_id': 9198961, 'google_parent_id': 21176, 'name': 'East Austin', 'canonical_name': 'East Austin,Texas,United States', 'country_code': 'US', 'target_type': 'Neighborhood', 'reach': 451000, 'gps': [-97.7090635, 30.2654547], 'keys': ['east', 'austin', 'texas', 'united', 'states']}
]

latitudes = [locations['gps'][1] for location in locations]
longitudes = [location['gps'][0] for location in locations]

#this creates google map centered to the specified location with a zoom value at last
gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 13)

#this plots the line between the paths
gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width = 3)

#this stores the plot and draws it
output_file = "map.html"
gmap.draw(output_file)

webbrowser.open(output_file)


