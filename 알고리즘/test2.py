
# def section_length(coord):
#     temp = copy.deepcopy(coord)
#     temp.append(temp[0])

#     section = []
#     circum = 0
#     for i in range(len(temp)-1):
#         if temp[i][0] == temp[i+1][0]:
#             section.append(abs(temp[i][1]-temp[i+1][1]))
#             circum += section[i]
#         elif temp[i][1] == temp[i+1][1]:
#             section.append(abs(temp[i][0]-temp[i+1][0]))
#             circum += section[i]
    
#     return section, circum

# def move(temp, i, time):
#     coord = copy.deepcopy(temp)
#     coord.append(coord[0])
#     new_coord = []
#     if coord[i][0] == coord[i+1][0]:
#         if (coord[i+1][1] - coord[i][1]) > 0:
#             new_coord = [coord[i][0], coord[i][1]+time]
#         else:
#             new_coord = [coord[i][0], coord[i][1]-time]

#     elif coord[i][1] == coord[i+1][1]:
#         if (coord[i+1][0] - coord[i][0]) > 0:
#             new_coord = [coord[i][0]+time, coord[i][1]]
#         else:
#             new_coord = [coord[i][0]-time, coord[i][1]]
#     new_coord = map(str, new_coord)
#     print(" ".join(new_coord))


# def robot_coord(coord, circum, time, section):

#     left_time = 0
#     for time in times:
#         t = time
#         if t >= circum:
#             left_time = t % circum
#             for i, s in enumerate(section):
#                 if left_time >= s:
#                     left_time -= s
#                 else:
#                     move(coord, i, left_time)
#                     break
#         else:
#             for i, s in enumerate(section):
#                 if t >= s:
#                     t -= s
#                 else:
#                     move(coord, i, t)
#                     break
#
# class Robot:
#     def __init__(self, x, y, direct, coord):
#         self.direct = direct
#         self.coord = coord
#         self.now_coord = [x, y]
#         for i, c in enumerate(coord):
#             if c == self.now_coord:
#                 self.now_index = i
    
#     def move(self, t):
#         for i, c in enumerate(coord):
#             if c == self.now_coord:
#                 self.now_index = i

#         if self.direct == '+':
#             try:
#                 self.now_coord = self.coord[self.now_index+t]
#             except:
#                 self.now_coord = self.coord[self.now_index + t - len(coord)]

#         elif self.direct == '-':
#             try:
#                 self.now_coord = self.coord[self.now_index-t]
#             except:
#                 self.now_coord = self.coord[self.now_index - t]
    
#     def change_direction(self):
#         if self.direct == '+':
#             self.direct == '-'
#         else:
#             self.direct == '+'
    
#     def __repr__(self):
#         return " ".join(map(str, self.now_coord))