# THIS WAS A PROJECT FOR AN ALGORITHM'S CLASS WHERE THE OBJECTIVE WAS TO FIND THE CLOSEST AND SECOND CLOSEST PAIR
# OF POINTS
import math


class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1

    def compute(self, file_data):

        for i in range(len(file_data)):  # make data list of list of floats
            file_data[i] = file_data[i].split()
            file_data[i][0] = float(file_data[i][0])
            file_data[i][1] = float(file_data[i][1])
        file_data.sort()  # sort the data
        closest_pairs, y_coords = self.find_pair(file_data)  # put data in find_pair function
        closest = closest_pairs[0]
        secondClosest = closest_pairs[1]
        return [closest, secondClosest]

    def find_pair(self, file_data):
        length = len(file_data)  # find length of data

        if length <= 4:  # if the length is less than 3...
            list_of_dist = self.brute_force(file_data)  # find the closest/second_closest distances
            closest = list_of_dist[0]
            second_closest = list_of_dist[1]
            list_y_coord = self.sort_by_y(file_data)  # make a list of coordinates sorted by y-values
            return [closest, second_closest], list_y_coord  # return a list of second/closest and list of y's
        else:
            mid_index = length // 2  # find the middle index
            left_data = file_data[:mid_index]  # split the lists to left and right
            right_data = file_data[mid_index:]
            left_pairs_list, left_y_coord = self.find_pair(left_data)  # find the second/closest and y's on left
            right_pairs_list, right_y_coord = self.find_pair(right_data)  # find the second/closest and y's on right
            left_pairs_list.extend(right_pairs_list)  # put the two lists together
            all_pairs_list = left_pairs_list  # make a list that has the left + right values
            all_pairs_list.sort()  # sort that list with both left + right values
            if all_pairs_list[0] != 0:  # since closest cannot be 0, we handle that here
                closest = all_pairs_list[0]
                second_closest = all_pairs_list[1]
            elif all_pairs_list[1] != 0:
                closest = all_pairs_list[1]
                second_closest = all_pairs_list[2]
            else:
                closest = all_pairs_list[2]
                second_closest = all_pairs_list[3]

            # RUNWAY
            left_y_coord.extend(right_y_coord)  # put the list of y's together
            all_y_coord = self.sort_by_y(left_y_coord)  # sort by the y values
            delta = second_closest  # make delta the second closest
            left_data = file_data[:mid_index]
            center_most_left = left_data[-1]  # get the center most point on the left
            center_most_right = right_data[0]  # get the center most point on the right
            center_point = (center_most_left[0] + center_most_right[0]) / 2  # average the two
            runway = []  # initialize the runway list
            for coord in all_y_coord:  # if x values are within runway, put it in list
                if center_point + delta >= coord[0] >= center_point - delta:
                    runway.append(coord)
            for i in range(len(runway) - 1):  # find distances across runway
                for j in range(i + 1, min(i + 7, len(runway))):
                    coord1 = runway[i]
                    coord2 = runway[j]
                    distance = self.dist(coord1, coord2)
                    if distance < closest and distance != 0:
                        second_closest = closest
                        closest = distance
                    if closest < distance < second_closest:
                        second_closest = distance

            return [closest, second_closest], all_y_coord

    def brute_force(self, file_data):
        length = len(file_data)
        if length == 2:
            coordinate_1 = file_data[0]
            coordinate_2 = file_data[1]
            closest = self.dist(coordinate_1, coordinate_2)
            return [closest, 0]
        elif length == 3:
            coordinate_1 = file_data[0]
            coordinate_2 = file_data[1]
            coordinate_3 = file_data[2]
            dist1_2 = self.dist(coordinate_1, coordinate_2)
            dist1_3 = self.dist(coordinate_1, coordinate_3)
            dist2_3 = self.dist(coordinate_2, coordinate_3)
            closest, second_closest = self.find_closest_and_second(dist1_2, dist1_3, dist2_3)
            return [closest, second_closest]
        else:
            coordinate_1 = file_data[0]
            coordinate_2 = file_data[1]
            coordinate_3 = file_data[2]
            coordinate_4 = file_data[3]
            dist1_2 = self.dist(coordinate_1, coordinate_2)
            dist1_3 = self.dist(coordinate_1, coordinate_3)
            dist1_4 = self.dist(coordinate_1, coordinate_4)
            dist2_3 = self.dist(coordinate_2, coordinate_3)
            dist2_4 = self.dist(coordinate_2, coordinate_4)
            dist3_4 = self.dist(coordinate_3, coordinate_4)
            closest, second_closest = self.find_closest_and_second(dist1_2, dist1_3, dist1_4, dist2_3, dist2_4, dist3_4)
            return [closest, second_closest]

    def dist(self, co1, co2):
        x1 = co1[0]
        y1 = co1[1]
        x2 = co2[0]
        y2 = co2[1]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    def find_closest_and_second(self, a, b, c, d=0, e=0, f=0):
        if d == 0:
            sorting_list = [a, b, c]
            sorting_list.sort()
            closest = sorting_list[0]
            second_closest = sorting_list[1]
            return closest, second_closest
        else:
            sorting_list = [a, b, c, d, e, f]
            sorting_list.sort()
            closest = sorting_list[0]
            second_closest = sorting_list[1]
            return closest, second_closest

    def same_side(self, center, co1, co2):
        if co1[0] < center and co2[0] < center:
            return True
        elif co1[0] > center and co2[0] > center:
            return True
        elif co1[0] == center and co2[0] == center:
            return True
        else:
            return False

    def sort_by_y(self, file_data):
        file_data.sort(key=self.take_y)
        list_y_coord = file_data
        return list_y_coord

    def take_y(self, element):
        return element[1]
