from interaction_control.robot import *
from Nao.nao_move import *


class RobotNao(Component):
    talk_node = None
    act_node = None
    robot = None

    def introduction(self):
        self.current_state = 'introduction'
        # say introduction

    def act(self):
        self.current_state = "act"
        # say saimon says
        print "Simon says"
        # say raise you hands
        print "raise you hands"
        # raise robot hands
        print "raising hands"

    def finished_action(self):
        self.current_state = "finished_action"



