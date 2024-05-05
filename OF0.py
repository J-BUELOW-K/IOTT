import network
import math
from control_messages import HP_OBJ, ETX_OBJ
from dodag import Dodag
import defines
from defines import METRIC_OBJECT_TYPE, METRIC_OBJECT_NONE, METRIC_OBJECT_HOPCOUNT, METRIC_OBJECT_ETX
#from network import Node


# # Objective Code Point
# OCP = 0


def map_value_to_step_of_rank(value:float, method:str='linear', min_value:int=0, max_value:float=60000, min_step:int=1, max_step:int=9):
    if method == 'linear': # linear mapping between value and step_of_rank (value is a float between min_value and max_value)
        return int((value - min_value) / (max_value - min_value) * (max_step - min_step) + min_step)
    
    elif method == 'log': # logarithmic mapping between value and step_of_rank (value is a float between min_value and max_value)
        return int(math.log(value) / math.log(max_value) * (max_step - min_step) + min_step)
    
    elif method == 'sigmoid': # sigmoid mapping between value and step_of_rank (value is a float between min_value and max_value)
        return int(1 / (1 + math.exp(-value)) * (max_step - min_step) + min_step)



def DAGRank(rank):
    return math.floor(float(rank) / defines.DEFAULT_MIN_HOP_RANK_INCREASE) # Returns Interger part of rank. see sec 3.5.1 in RPL standard for more info


def of0_compute_rank(parent_rank, metric_object = None):  
    # note, metric_object is the full metric_object all the way from the node to the root
    # The step_of_rank Sp that is computed for that link is multiplied by
    # the rank_factor Rf and then possibly stretched by a term Sr that is
    # less than or equal to the configured stretch_of_rank.  The resulting
    # rank_increase is added to the Rank of preferred parent R(P) to obtain
    # that of this node R(N):
    
        # R(N) = R(P) + rank_increase where:

        # rank_increase = (Rf*Sp + Sr) * MinHopRankIncrease
        
    # UDREGNE STEP OF RANK. ENTEN VED BRUG AF DEFAULT step_of_rank (hvis der ingen metric object gives), eller "HP" eller "ETX"
        # måske er https://mailarchive.ietf.org/arch/msg/6tisch/ijlk2XYM6Xz7xQtTB88DMSNjRdw/ brugbar
        # aka måske Sp = a*ETX + b .
        # hvor man lige skal tænke over hvad a skal være (ivhertfald noget scalere ETX ned, fordi vores ETX er stor.)
        # (husk også at step_of_rank skal være et heltal) 
        
    

    if metric_object is None:
        step_of_rank = defines.DEFAULT_STEP_OF_RANK
    elif isinstance(metric_object, HP_OBJ):
        step_of_rank=map_value_to_step_of_rank(metric_object.cumulative_hop_count, method='log', max_value=(defines.NUMBER_OF_NODES//2)) # or 'log' or 'sigmoid'
        pass # TODO map hop count til STEP_OF_RANK mellem 1 og 9 
    elif isinstance(metric_object, ETX_OBJ):
        step_of_rank=map_value_to_step_of_rank(metric_object.cumulative_etx, method='linear') # or 'log' or 'sigmoid'
        #print("debug hejsa3")
    else:
        raise ValueError("Invalid metric object type")
    
    
    rank_increase = (defines.DEFAULT_RANK_FACTOR*step_of_rank + defines.DEFAULT_RANK_STRETCH) * defines.DEFAULT_MIN_HOP_RANK_INCREASE  
    new_rank =  parent_rank + rank_increase
    
    if new_rank > defines.INFINITE_RANK:
        return defines.INFINITE_RANK
    else:
        return new_rank    

        

            
    
    
    

    
#def of0_compare_parent(current_parent: Node, challenger_parent: Node, ICMP_DIO, metric_object_to_challenger = None, metric_object_type = None):
def of0_compare_parent(current_parent_rank, challenger_parent_rank,
                       metric_object_through_current_parrent = None, metric_object_through_challenger = None):
    # note, "parent" in parameter names means "prefered parent"


    rank_through_current_parent = of0_compute_rank(current_parent_rank, metric_object_through_current_parrent)
    rank_through_challenger_parent = of0_compute_rank(challenger_parent_rank, metric_object_through_challenger)

    if DAGRank(rank_through_challenger_parent) < DAGRank(rank_through_current_parent):    # only choose challenger parent as new prefered parent IF it results in a better DAGRank (if equal, keep current parent)
        # note, DAGRank() is used when comparing ranks (see RPL standard)
        return "update parent", DAGRank(rank_through_challenger_parent) 
    
    elif DAGRank(rank_through_challenger_parent) >= DAGRank(rank_through_current_parent): # step 8 in RFC 6552
        return "keep parent", DAGRank(rank_through_current_parent)


    else:
        return "keep parent", DAGRank(rank_through_current_parent) 
    #TODO: return "keep parent" or "update parent" depending on which parent is better (based on rank)
    
    
    
