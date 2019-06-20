
from core.extract import Extract
from core.load import Load
from core.transform import Transform


list_of_coordinates = Extract('data_points_20180101.txt').get_list_of_coordinates()
transform = Transform(key_google_maps='AIzaSyBhFuJK5JqixSDEaKPGjUmAoARcpntgU-c')
load = Load()

for pair_of_coordinates in list_of_coordinates:
    adress = transform.get_adress(pair_of_coordinates)
    load.save(adress)

    print('-------------------------')
    print(adress)
    print('-------------------------')



