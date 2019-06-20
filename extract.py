class Extract:

    def __init__(self, file_name):
        self.__text_file = open(f'resources/{file_name}', 'r')
        self.__text = self.__text_file.readlines()
        self.__text_file.close()
        self.__list_of_coordinates = []
        self.__temporary_list = [0, 0]

    def get_list_of_coordinates(self):
        for line in self.__text:
            self.__check_line(line)

            if self.__is_a_pair_of_coordinates(self.__temporary_list):
                self.__list_of_coordinates.append(self.__temporary_list.copy())
                self.__temporary_list = [0, 0]

        return self.__list_of_coordinates

    def __check_line(self, line):
        if 'Latitude:' in line:
            self.__temporary_list[0] = self.__get_coordinate_value(line)
        if 'Longitude:' in line:
            self.__temporary_list[1] = self.__get_coordinate_value(line)

    @staticmethod
    def __is_a_pair_of_coordinates(list):
        if list[0] != 0 and list[1] != 0:
            return True

        return False

    @staticmethod
    def __get_coordinate_value(line):
        return line.split(' ')[4].replace('\n', '')
