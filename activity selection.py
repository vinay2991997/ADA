
class Activity:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __lt__(self,other):
        if self.end < other.end:
            return True
        else:
            return False
    def __str__(self):
        return '('+ str(self.start) + ',' + str(self.end) + ')'

#Activity Selection

n = int(input("Enter the number of Activities :"))

activities = list()

for i in range(n):
    start,end = tuple(map(int,input().strip().split()))
    activities.append(Activity(start,end))

#activities.sort(key=end,reverse = True)
activities.sort()
#print(sorted(activities))
newlist = list()
last = 0
for activity in activities:
    if activity.start >= last:
        newlist.append(activity)
        last = activity.end
    #print(activity.start,activity.end)

for activity in newlist:
    print(activity.start,activity.end)
