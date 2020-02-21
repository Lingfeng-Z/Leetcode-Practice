import datetime

def main(input):
    line = input.split(' ')
    R = line[0]
    S = line[1]
    DIR = line[2]
    HH = line[3]



class timeTable():
    def __init__(self):
        self.starttime = {tuple([A1,A7]):datetime.datetime.strptime('5:55', '%H:%M'),
        tuple([A1,A13]):datetime.datetime.strptime('6:00', '%H:%M'),
        tuple([A7,A1]):datetime.datetime.strptime('6:06', '%H:%M'),
        tuple([A7,A13]):datetime.datetime.strptime('6:10', '%H:%M'),
        tuple([A13,A1]):datetime.datetime.strptime('5:52', '%H:%M'),
        tuple([B1,A7]):datetime.datetime.strptime('6:00', '%H:%M'),
        tuple([A7,B1]):datetime.datetime.strptime('6:11', '%H:%M'),}

        self.sep = {tuple([A1,A7]): datetime.timedelta(minutes=10),
        tuple([A1,A13]): datetime.timedelta(minutes=10),
        tuple([A7,A1]): datetime.timedelta(minutes=10),
        tuple([A13,A1]): datetime.timedelta(minutes=10),
        tuple([B1,A7]): datetime.timedelta(minutes=6),
        tuple([A7,B1]): datetime.timedelta(minutes=6)}

        self.interaltimecost = {'A':[3,5,2,3,4,3,4,2,2,3,6,2],
        'B':[4,3,3,2,3]}
        self.timecost = {}
        for i in self.interaltimecost.keys():
            self.timecost[i] = {'U':[0], 'D':[0]}
            for j in range(1, len(self.interaltimecost[i])+1):
                self.timecost[i]['U'].append(self.interaltimecost[i][:j])
                self.timecost[i]['D'].append(self.interaltimecost[i][len(self.interaltimecost[i])-j:])
        self.pointlist = []
        self.endpoint = ['A1', 'A13', 'A7', 'B1']
        self.timetable = {}
  
  def makeTimetable(self):
        for i in self.starttime.keys():
            tempstarttime = self.starttime[i]
            if i in self.sep.keys():
                while True:
                    hour = tempstarttime.hour
                    if hour >= 11:
                        break
                    else:
                        starttime.append(tempstarttime)
                        tempstarttime += self.sep[i]
                if list[i][0][0] == list[i][1][0]:
                    if int(list[i][0][1:]) < int(list[i][1][1:]):
                        self.int(list[i][0][1:]
                for j in starttime:

            else:








if __name__ == "__main__":
    input = "A A5 U 13"
    main(input)