'''
This code generates *language_info.json*. The content can be extended over time.
    1. Specify 18 districts of Hong Kong (for now)
    2. Specify a coordinate for each district
    3. Specify location groups in each district
'''

import pandas as pd

district = ['Wong Tai Sin',
            'Kowloon City',
            'Kwun Tong',
            'Sai Kung',
            'North',
            'Central-Western',
            'Wan Chai',
            'Eastern',
            'Tuen Mun',
            'Yuen Long',
            'Southern',
            'Islands',
            'Sham Shui Po',
            'Yau Tsim Mong',
            'Kwai Tsing',
            'Tsuen Wan',
            'Tai Po',
            'Sha Tin']
coordinate = [(22.3416, 114.1938),  # Wong Tai Sin Station
              (22.3172, 114.1876),  # To Kwa Wan Station
              (22.3121, 114.2263),  # Kwun Tong Station
              (22.3074, 114.2600),  # Tseung Kwan O Station
              (22.5012, 114.1279),  # Sheung Shui Station
              (22.2819, 114.1582),  # Central Station
              (22.2775, 114.1731),  # Wan Chai Station
              (22.2912, 114.2005),  # North Point Station
              (22.3948, 113.9731),  # Tuen Mun Station
              (22.4460, 114.0347),  # Yuen Long Station
              (22.2419, 114.1561),  # Lei Tung Station
              (22.2892, 113.9414),  # Tung Chung Station
              (22.3307, 114.1622),  # Sham Shui Po Station
              (22.3128, 114.1706),  # Yau Ma Tei Station
              (22.3630, 114.1312),  # Kwai Hing Station
              (22.3736, 114.1177),  # Tsuen Wan Station
              (22.4445, 114.1704),  # Tai Po Market Station
              (22.3818, 114.1869)]  # Sha Tin Station
locations = [['Wong Tai Sin Area'],
             ['Hung Hom', 'Kowloon City', 'Kowloon City Area', 'To Kwa Wan'],
             ['Kowloon Bay', 'Kwun Tong', 'Kwun Tong Area', 'Ngau Tau Kok'],
             ['Sai Kung', 'Sai Kung Area', 'Tseung Kwan O'],
             ['Fanling', 'Northern NT Area', 'Sheung Shui'],
             ['Admiralty', 'Central', 'Central & Western Area', 'Sai Wan', 'Sai Ying Pun', 'Sheung Wan'],
             ['Causeway Bay', 'Wan Chai', 'Wan Chai Area'],
             ['Chai Wan', 'Eastern Area', 'North Point', 'Quarry Bay', 'Sai Wan Ho', 'Shau Kei Wan', 'Tin Shui Wai', 'Tai Koo', 'Tin Hau'],
             ['Tuen Mun Area'],
             ['Tin Shui Wai', 'Yuen Long', 'Yuen Long Area'],
             ['Aberdeen', 'Pok Fu Lam', 'Southern Area'],
             ['Airport Area', 'Cheung Chau Area', 'Lantau Island', 'Tung Chung'],
             ['Cheung Sha Wan', 'Lai Chi Kok', 'Sham Shui Po', 'Sham Shui Po Area'],
             ['Mong Kok', 'Tsim Sha Tsui', 'Yau Ma Tei', 'Yau Tsim Mong Area'],
             ['Kwai Fong', 'Kwai Hing', 'Kwai Tsing Area', 'Tsing Yi'],
             ['Tsuen Wan Area'],
             ['Tai Po Area'],
             ['Shatin Area']]
pd.DataFrame({'district': district,
              'coordinate': coordinate,
              'locations': locations}).to_json("location_info.json", orient='records')
