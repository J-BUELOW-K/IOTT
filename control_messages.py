
import defines

"""

lave en class der hedder ICMP_dio
    Anvend en class der hedder ICMP header
    dio_object = icmp_dio()
    DAG Metric Container hvor input er en string og den laver det selv
        None
        Hop count object
        EXT reliability object

Lave det samme til de to andre (dao og dao ack)

https://datatracker.ietf.org/doc/html/rfc6551#section-3.3

fx for dio message --> ICMP header + DIO + Options (hop/EXT)

"""

# Container
# lave class til hop count object
# TODO lave class til EXT reliability object

# Lave dio message class
# Lave dao message class
# Lave dao ack message class

# TODO Lave ICMP_dio class
# TODO Lave ICMP_dao class
# TODO Lave ICMP_dao_ack class 
# TODO Packet

# Lave ICMP header class



class ICMP_header:

    """ICMP "header" only"""

    def __init__(self, type, code):
        
    #     0                   1                   2                   3
    #     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |     Type      |     Code      |          Checksum             |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |                                                               |
    #    .                             Base                              .
    #    .                                                               .
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |                                                               |
    #    .                           Option(s)                           .
    #    .                                                               .
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Source: rfc6550

        self.type = type
        self.code = code

        # Checksum and options not included. Base field is implemented at a higher level.
        # Refer https://datatracker.ietf.org/doc/html/rfc6550#section-6

        # TODO Check for ICMP type = 155 in message handler
        # TODO Check ICMP code. If unknown, the discard. 



class DIO:

    """DODAG Information Object (DIO)""" 

    #     0                   1                   2                   3
    #     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    | RPLInstanceID |Version Number |             Rank              |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |G|0| MOP | Prf |     DTSN      |     Flags     |   Reserved    |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |                                                               |
    #    +                                                               +
    #    |                                                               |
    #    +                            DODAGID                            +
    #    |                                                               |
    #    +                                                               +
    #    |                                                               |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |   Option(s)...
    #    +-+-+-+-+-+-+-+-+

    def __init__(self, rpl_instance_id, vers, rank, g_flag, mop,\
                 prf, dtsn, flags, reserved, dodag_id, opt):

        self.rpl_instance_id = rpl_instance_id      # Set by the DODAG root and indicate which RPL Instance the DODAG is a part of.
        self.vers = vers                            # TODO Unsigned integer set by the DODAG root to the DODAGVersionNumber           
        self.rank = rank                            # TODO Unsigned integer indicating the DODAG Rank of the node sending the DIO message
        self.g_flag = g_flag                        # The Grounded 'G' flag indicates whether the DODAG advertised can satisfy the 
                                                    # application-defined goal. If the flag is set, the DODAG is grounded. If the 
                                                    # flag is cleared, the DODAG is floating.
        self.mop = mop                              # The Mode of Operation (MOP) field identifies the mode of operation of the RPL 
                                                    # Instance as administratively provisioned at and distributed by the DODAG root.  
                                                    # All nodes who join the DODAG must be able to honor the MOP in order to fully 
                                                    # participate as a router, or else they must only join as a leaf.
        self.prf = prf                              # TODO DODAGPreference (Prf): A 3-bit unsigned integer that defines how preferable the
                                                    # root of this DODAG is compared to other DODAG roots within the instance
        self.dtsn = dtsn                            # TODO Unsigned integer set by the node issuing the DIO message
        self.flags = flags                          # TODO MUST be set to 0 by sender and ignored by receiver. 
        self.reserved = reserved                    # TODO MUST be set to 0 by sender and ignored by receiver.
        self.dodag_id = dodag_id                    # IPv6 address set by a DODAG root that uniquely identifies a DODAG. The DODAGID 
                                                    # MUST be a routable IPv6 address belonging to the DODAG root.
        self.opt = opt                              # The DIO message MAY carry valid options. Refer RFC6550 section 6.3.3 for valid options.

        # All fields included, however not all are necessarily used.
        # Reference: https://datatracker.ietf.org/doc/html/rfc6550#section-6.3



class DAO:

    """DODAG Information Object (DAO)"""

    #         0                   1                   2                   3
    #         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    #        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #        | RPLInstanceID |K|D|   Flags   |   Reserved    | DAOSequence   |
    #        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #        |                                                               |
    #        +                                                               +
    #        |                                                               |
    #        +                            DODAGID*                           +
    #        |                                                               |
    #        +                                                               +
    #        |                                                               |
    #        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #        |   Option(s)...
    #        +-+-+-+-+-+-+-+-+


    def __init__(self, rpl_instance_id, k_flag, d_flag, dao_sequence,\
                 dodag_id, opt, flags = 0, reserved = 0):
        
        self.rpl_instance_id = rpl_instance_id      # Topology instance associated with the DODAG, as learned from the DIO.
        self.k_flag = k_flag                        # The 'K' flag indicates that the recipient is expected to send a DAO-ACK back.
        self.d_flag = d_flag                        # The 'D' flag indicates that the DODAGID field is present. This
                                                    # flag MUST be set when a local RPLInstanceID is used.
        self.flags = flags                          # TODO MUST be set to 0 by sender and ignored by receiver.
        self.reserved = reserved                    # TODO MUST be set to 0 by the sender and ignored by the receiver.
        self.dao_sequence = dao_sequence            # Incremented at each unique DAO message from a node and echoed in the DAO-ACK message.
        self.dodag_id = dodag_id                    # TODO Unsigned integer set by a DODAG root that uniquely identifies a DODAG. This field is only
                                                    # present when the 'D' flag is set.
        self.opt = opt                              # The DIO message MAY carry valid options.
                                                    # This project supports Hop Count Objects, EXT reliability object, or none.
    
    # All fields included, however not all are necessarily used.
    # Reference: https://datatracker.ietf.org/doc/html/rfc6550#section-6.4

 

class DAO_ACK:

    """Destination Advertisement Object Acknowledgement"""

    #     0                   1                   2                   3
    #     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    | RPLInstanceID |D|  Reserved   |  DAOSequence  |    Status     |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |                                                               |
    #    +                                                               +
    #    |                                                               |
    #    +                            DODAGID*                           +
    #    |                                                               |
    #    +                                                               +
    #    |                                                               |
    #    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #    |   Option(s)...
    #    +-+-+-+-+-+-+-+-+


    def __init__(self, rpl_instance_id, d_flag, reserved,\
                 dao_sequence, status, dodag_id, opt):
        
        self.rpl_instance_id = rpl_instance_id      # Topology instance associated with the DODAG, as learned from the DIO.
        self.d_flag = d_flag                        # The 'D' flag indicates that the DODAGID field is present. This
                                                    # flag MUST be set when a local RPLInstanceID is used.
        self.reserved = reserved                    # Reserved for flags. 
        self.dao_sequence = dao_sequence            # Incremented at each DAO message from a node, and echoed in the DAO-ACK 
                                                    # by the recipient. The DAOSequence is used to correlate a DAO message and a DAO ACK message
        self.status = status                        # TODO Status 0: Unqualified acceptance (i.e., the node receiving the DAO-ACK is not rejected).
        self.dodag_id = dodag_id                    # TODO Unsigned integer set by a DODAG root that uniquely identifies a DODAG. This field is only
                                                    # present when the 'D' flag is set.
        self.opt = opt                              # The DIO message MAY carry valid options.

    # All fields included, however not all are necessarily used.
    # Reference: https://datatracker.ietf.org/doc/html/rfc6550#section-6.5




    # Routing Metrics applied in this project has been reduced a lot and will not
    # use the standart DAG Metric Container Format. Only the Hop Count (HP) and ETX Reliability
    # Object are implemented. 

class HP_OBJ():
    
    # The Hop Count (HP) object is used to report the number of traversed
    # nodes along the path.

    #   0                   1             
    #   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 
    #   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #   |  Res  | Flags |   Hop Count   |
    #   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # The HP object may also contain a set of TLVs used to convey various
    # node characteristics. No TLV is currently defined and has thus been opmitted.
    # Hop count may be used as a metric or as a constraint. Is only used as a metric
    # TODOThe first node on the path (not including the sender) must set this value to 1
    
    def __init__(self, HP, res = 0, flags = 0):
        
        self.res = res                              # Reserved field.  This field MUST be set to zero on 
                                                    # transmission and MUST be ignored on receipt.
        self.flags = flags                          # No Flag is currently defined.  Unassigned bits are considered reserved.
                                                    # They MUST be set to zero on transmission and MUST be ignored on receipt.
        self.HP = HP                                # Hop Count - Used as a metric

    # Referce: https://datatracker.ietf.org/doc/html/rfc6551#section-3.3


class ETX_OBJ():
    pass

    # Referce: https://datatracker.ietf.org/doc/html/rfc6551#section-4.3.2