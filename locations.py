from urllib2 import urlopen
import re

def get_pcs_locations_js():
    pcs_loc_file = urlopen('http://www.phillycarshare.com/wordpress/locations/our-locations')
    pcs_loc_file_data = pcs_loc_file.read()

    begin = pcs_loc_file_data.find("var pods = [];")
    end = pcs_loc_file_data.find("var icon = new GIcon();")

    loc_js = pcs_loc_file_data[begin:end]

    return loc_js

def get_pcs_locations():
    pattern = 'pods.push\((\[.*\])\);\n'
    matches = re.findall(pattern, get_pcs_locations_js())

    # Take advantage of the fact that JS lists have the same format as Pythong
    # lists.
    locations = [eval(s) for s in matches]

    return locations

if __name__ == '__main__':
    print get_pcs_locations()
