#Still in progress....
#To be used to get intimation from the exploration package about the dead end or split requirement


import rclpy
from rclpy.node import Node

from branch import branch,dict_branches
surrounding={}
class info_node(Node):
    def __init__(self):
        super().__init__("info_node")
        self.info_sub=self.create_subscription()   #this will get info form the exploration package and callback the function to call the split
        #msg has branch object and dictionary surrounding


    def callback(self,msg):
        branch=dict_branches[msg.id]   #this is so that object of rbanch class can be called using the id as class objects can not be sent over msg
        branch.split(surrounding)   
