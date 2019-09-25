import airbnb


from utils import str_utils

def run():
    api = airbnb.Api(randomize=True)


    # sh = api.get_homes("Shanghai")
    # print(str_utils.json_encode(sh))

    d = api.get_calendar(31375330)
    print(str_utils.json_encode(d))

    d = api.get_listing_calendar(31375330)
    print(str_utils.json_encode(d))



if __name__ == '__main__':
    run()