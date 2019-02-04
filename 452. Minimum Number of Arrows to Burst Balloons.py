class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        points.sort()
        shoot_num =1
        shoot_begin = points[0][0]
        shoot_end   = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= shoot_end:
                shoot_begin = points[i][0]
                if shoot_end > points[i][1]:
                    shoot_end = points[i][1]
            else:
                shoot_num+=1
                shoot_begin = points[i][0]
                shoot_end   = points[i][1]
        return shoot_num
