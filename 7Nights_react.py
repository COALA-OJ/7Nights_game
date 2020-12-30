class UserState:
    def __init__(self):
        """
        usermap initial itself and start point
        """
        self.usermap = []
        self.st_x
        self.st_y

    def isEvnet(self):
        """
        event 발생 여부
        1. 몬스터 만났을 때
        2. 아이템을 얻었을 때
        """
    def legalMoves(self):
        """
        이동키를 입력 받았을 때 이동 가능한 곳 인지 확인
        'up' 'down' 'left' 'right'
        벽이라면 이동 불가능, 이벤트 발생 여부 체크?

        :return: True/False
        """

    def result(self):
        """
        이동 전, 후 맵 출력
        ex) 전체 맵 중에 현재 위치 기준으로 주변 10x10 출력
        만약 가장 위쪽이여서 더이상 출력할 결과가 없다면? 유저가 이동?
        :return:
        """
