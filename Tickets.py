# import Kyobo
from Kyobo import kyobo
from Yes24 import yes24
from Aladin import aladin
from DriverManager import driverManager



class ticketManager:
    def __init__(self):
        self.ticketList = []
        self.initTickets()
    def initTickets(self):
        #Todo 나중에 여기도 .yml로 뽑을 예정
        self.ticketList.append([[aladin, '', 0, 0, '왜곡하는 뇌', 2],
                     ])
        # self.ticketList.append([[aladin, '', 0, 0, '삶은 문제해결의 연속이다', 1],])
        self.ticketList.append([[yes24, '', 0, 0, '천하제일 치킨쇼', 5],       # 21p       # no device
            ])
        self.ticketList.append([[yes24, '', 0, 0, '천하제일 치킨쇼', 5],])
        self.ticketList.append([[yes24, '', 0, 0, '천하제일 치킨쇼', 5],])
        # self.ticketList.append([[yes24, '', 0, 0, '마틸다', 1],
        #             ])

        self.ticketList.append([[aladin, '', 0,'왜곡하는 뇌', 2],  # 11p
                                ])
        # self.ticketList.append( [[yes24, '', 0, 0, '당신의 뇌는 최적화를 원한다', 4],         # no device
        #            ])

        self.ticketList.append([[aladin, '', 0, 0, '기분은 노크하지 않는다', 2], # 11p
                                ])
        self.ticketList.append([[yes24, '', 0, 0, '시간이 있었으면 좋겠다', 6],
                   ])


    def getTicket(self):
        return self.ticketList
