#here we will make the basic class of the bots from which their attributes will me controlled

import rclpy
from rclpy.node import Node
class bot(Node):
    def __init__(self,id,coord,priority,color="white",returning=False):
        super().__init__("bot_node")
        self.id=id
        self.coord=coord
        self.color=color
        self.priority=priority
        self.returning=returning
        self.path=[]
        self.follow_leader=None    #initially following none
        self.map_pub=self.create_publisher()   #to the map publish the coordinates,id and initial colour 
    def leader(self):
        self.color="blue"
        self.update_map()
    def follower(self):
        self.color="green"
        self.update_map()
    def explorer(self):
        self.color="yellow"
        self.update_map()
    def is_returning(self):
        self.returning=True
        self.color="red"
        self.update_map()
    def follow(self,leader):
        self.follow_leader=leader
    def is_leader(self):
        return self.color=="blue"
    def update_map(self): #called everytime a bot object is made or colour updated so that map can be updated
        #publish the id and colour of bot 
        pass


def main(args=None):
    rclpy.init(args=args)

    node=bot()
    rclpy.spin(node)   
    rclpy.shutdown()