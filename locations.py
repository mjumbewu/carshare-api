from urllib2 import urlopen

def get_locations_js():
    pcs_loc_file = urlopen('http://www.phillycarshare.com/wordpress/locations/our-locations')
    pcs_loc_file_data = pcs_loc_file.read()

    begin = pcs_loc_file_data.find("var pods = [];")
    end = pcs_loc_file_data.find("var icon = new GIcon();")

    loc_js = pcs_loc_file_data[begin:end]

    return loc_js

if __name__ == '__main__':
    print get_locations_js()
