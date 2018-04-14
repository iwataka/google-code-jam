import math

def solve(desired_area):
    spec_area = 1.414213
    if desired_area <= spec_area:
        rad = math.acos((2 * desired_area + math.sqrt(8 - 4 * desired_area ** 2)) / 4)
        return calc_face_centers(rad)
    else:
        rad = math.pi / 4
        rad2 = math.acos(desired_area / 2)
        return calc_face_centers(rad, rad2)

def calc_face_centers(rad, additional_rad = None):
    original_point = [
            [0.5, 0.0, 0.0],
            [0.0, 0.5, 0.0],
            [0.0, 0.0, 0.5]
            ]
    rotated_point = [rotate_z(x, rad) for x in original_point]
    if additional_rad == None:
        return rotated_point
    else:
        return [rotate_x(x, rad) for x in rotated_point]

def rotate_z(point, rad):
    p = point[:]
    p[0] = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    p[1] = point[0] * math.sin(rad) + point[1] * math.cos(rad)
    p[2] = point[2]
    return p

def rotate_x(point, rad):
    p = point[:]
    p[1] = point[1] * math.cos(rad) - point[2] * math.sin(rad)
    p[2] = point[1] * math.sin(rad) + point[2] * math.cos(rad)
    p[0] = point[0]
    return p

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        desired_area = float(input())
        ans = solve(desired_area)
        print("Case #%d:" % (i + 1))
        for point in ans:
            print(" ".join([str(x) for x in point]))
