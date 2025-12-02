#Still in progress...
#here we define basic tasks of a branch and its attribute
#the branch publish a request for getting respective coordinates and the map will givve the idea about those coord

import rclpy
from rclpy.node import Node

map={}
from bot import bot
import random
i=1
dict_branches={}
class branch(Node):
    min_size=2
    i=i+1
    def __init__(self,members,leader,id=i,split=True):
        super().__init__("branch_node")
        self.leader=leader
        self.id=id
        self.members=members   #list of object form bot class
        self.lidar_pub=self.create_publisher()
        self.leader.leader()
        for i in self.members:
            i.follower()
            i.follow_leader=self.leader
        path=[]
        dict_branches[self.id]=self
        # self.pub()
        self.split=split   #this shows if the branch is able to split further or not
    def check_surr(self):

        pass
    def split(self,surrounding ):   #will be called when the exploration calls info and info calls this function
        #the surrounding will be a dict having eight surrounding coord and their code as -1,0,1
        if 1+len(self.members)<= 2:
            print(f"branch with id {self.id} is at its min")
            new=branch(self.id,self.members,self.leader,split=False)
            for i in surrounding:
                if surrounding[i]==1:
                    x=i
                    break
            new.pub(x)
        else:
            frontier=[]
            new_branch_leader=self.members.check_leader()
            n=len(self.members)//2   #number of members in the original
            self.members.remove(new_branch_leader)
            new1=branch(members=self.members[:n],leader=self.leader)
            new2=branch(members=self.members[n:],leader=new_branch_leader)
            for i in surrounding:
                if surrounding[i]==1:
                    frontier.append(i)   #frontier
                if len(frontier)==3:
                    
                    x=random.choice(frontier)   #take a frontier
                    surrounding[x]=0  #means its not a frontier anymore
                    new1.pub(x)
                    new2.split(surrounding)
                else:
                    x=random.choice(frontier) 
                    new1.pub(x)
                    frontier.remove(x)
                    new2.pub(frontier[0])

    def update_path(self):
        pass
    def update_branch(self,members_lost):
        pass
    def change_leader(self):
        pass
    def pub(self,init_coord):    #takes the start coord for the branch and publish data to exploration package
        pass
    




def main(args=None):
    rclpy.init(args=args)

    node=branch()
    rclpy.spin(node)   
    rclpy.shutdown()