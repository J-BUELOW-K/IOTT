import math

import time






ROOT_RANK = 0
MAX_RANK = 0xFFFF






def dag_rank_macro(rank: float, MinHopRankIncrease: float) -> int: # Returns Interger part of rank. see sec 3.5.1 in RPL standard for more info
    return math.floor(rank/MinHopRankIncrease)
    






class Dodag:

    def __init__(self, dodag_id, dodag_version_num, is_root = False, MinHopRankIncrease = 256.0):
        self.dodag_id = dodag_id
        self.dodag_version_num = dodag_version_num
        self.MinHopRankIncrease = MinHopRankIncrease
        self.last_dio = time.time()

        if is_root:
            self.rank = ROOT_RANK
        else:
            self.rank = MAX_RANK
        self.rank 

    def set_rank(self, rank):
        self.rank = rank
        
    def DAGRank(self, rank):
        return math.floor(float(rank)/ self.MinHopRankIncrease)

    # er ikker sikker på om vi skal bruge float rank eller DAGRank() (interger part) her







class Rpl_Instance:

    def __init__(self, rpl_instance_id):
        self.rpl_instance_id = rpl_instance_id
        self.dodag_list = []

    def add_dodag(self, dodag: Dodag):
        self.dodag_list.append(dodag)