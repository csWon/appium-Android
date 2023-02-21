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

        # ticket1 = [[aladin, '', 0, 0, '저는 많이 보고 있어요', 1],
        #            ]
        # ticket2 = [[aladin, '', 0, 0, '저는 많이 보고 있어요', 1],
        #            ]
        # ticket3 = [[aladin, '', 0, 0, '저는 많이 보고 있어요', 1],
        #            ]
        # ticket4 = [[aladin, '', 0, 0, '사랑의 이해', 0],
        #            ]
        # ticket5 = [[aladin, '', 0, 0, '사랑의 이해', 0],
        #            ]
        # ticket6 = [[aladin, '', 0, 0, '사랑의 이해', 0],
        #            ]
        ticket1 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]
        ticket2 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]
        ticket3 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]
        ticket4 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]
        ticket5 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]
        ticket6 = [[kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
                   ]

        self.ticketList.append(ticket1)
        self.ticketList.append(ticket2)
        self.ticketList.append(ticket3)
        self.ticketList.append(ticket4)
        self.ticketList.append(ticket5)
        self.ticketList.append(ticket6)

    def getTicket(self):
        return self.ticketList

        # testList_12124 = [
        #     [kyobo, '', 0, 0, '물고기는 존재하지 않는다', 0],
        #     [aladin, '', 0, 0, '사랑의 이해', 0],
        #     # [kyobo, '', 0, 0, '데일리 필로소피'],
        #     # [kyobo, '', 0, 0, '구의 증명'],
        #     [yes24, '', 0, 0, '생에 감사해'],
        #     # [kyobo, '', 0, 0, '클루지'],
        #     # [kyobo, '', 0, 0, '나도 모르는 내 마음의 심리법칙'],
        #     # [aladin, '', 0, 0, '넌 대체 몇 년째 영어 공부를 하고 있는 거니?'],
        #     # [aladin, '', 0, 0, '세상의 마지막 기차역'],
        #     # [kyobo, '', 0, 0, '클루지'],
        #     # [yes24, '', 0, 0, '물고기는 존재하지 않는다'],
        #     # [yes24, '', 0, 0, '돈의 속성 200쇄 리커버'],
        #     # [aladin, '', 0, 0, '쿼런틴'],
        #     # [aladin, '', 0, 0, '쿼런틴'],
        #     # [yes24, '', 0, 0, '돈의 속성 200쇄 리커버'],
        #     # [aladin, '', 0, 0, '쿼런틴'],
        #
        #     [aladin, '', 0, 0, '쿼런틴'],
        #     [yes24, '', 0, 0, '물고기는 존재하지 않는다'],
        # ]
        # return testList_12124