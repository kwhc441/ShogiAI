from typing_extensions import Self
import torch
import torch.nn as nn
import torch.nn.functional as F

from dlshogi.common import *

class Bias(nn.Module):
    def __init__(self, shape):
        super(Bias, self).__init__()
        self.bias=nn.Parameter(torch.zeros(shape))

    def forward(self, input):
        return input + self.bias
# An ordinary implementation of Swish function
class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)

k = 192
fcl = 256 # fully connected layers
class PolicyValueNetwork(nn.Module):
    def __init__(self):
        super(PolicyValueNetwork, self).__init__()
        self.l1_1_1 = nn.Conv2d(in_channels=FEATURES1_NUM, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l1_1_2 = nn.Conv2d(in_channels=FEATURES1_NUM, out_channels=k, kernel_size=1, padding=0, bias=False)
        self.l1_2 = nn.Conv2d(in_channels=FEATURES2_NUM, out_channels=k, kernel_size=1, bias=False) # pieces_in_hand
        self.l2  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l3  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l4  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l5  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l6  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l7  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l8  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l9  = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l10 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l11 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l12 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l13 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l14 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l15 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l16 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l17 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l18 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l19 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l20 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l21 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        # 追加
        self.l22 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l23 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l24 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l25 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l26 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l27 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l28 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l29 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l30 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l31 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)

        self.l32 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l33 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l34 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l35 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l36 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l37 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l38 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l39 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l40 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l41 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)

        self.l42 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l43 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l44 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l45 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l46 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l47 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l48 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l49 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l50 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l51 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        # ここまで追加
        #追追加（25→50)
        self.l52 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l53 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l54 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l55 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l56 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l57 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l58 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l59 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l60 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l61 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)

        self.l62 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l63 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l64 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l65 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l66 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l67 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l68 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l69 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l70 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l71 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)

        self.l72 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l73 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l74 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l75 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l76 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l77 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l78 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l79 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l80 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l81 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l82 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l83 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l84 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l85 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l86 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l87 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l88 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l89 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l90 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l91 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)

        self.l92 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l93 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l94 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l95 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l96 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l97 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l98 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l99 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l100 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)
        self.l101 = nn.Conv2d(in_channels=k, out_channels=k, kernel_size=3, padding=1, bias=False)


        # policy network
        #self.l22 = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1, bias=False)
        #self.l22_2 = Bias(9*9*MAX_MOVE_LABEL_NUM)
        #self.l52 = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1, bias=False)
        #self.l52_2 = Bias(9*9*MAX_MOVE_LABEL_NUM)
        self.l102 = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1, bias=False)
        self.l102_2 = Bias(9*9*MAX_MOVE_LABEL_NUM)


        # value network
        #self.l22_v = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1)
        #self.l23_v = nn.Linear(9*9*MAX_MOVE_LABEL_NUM, fcl)
        #self.l24_v = nn.Linear(fcl, 1)
        #self.l52_v = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1)
        #self.l53_v = nn.Linear(9*9*MAX_MOVE_LABEL_NUM, fcl)
        #self.l54_v = nn.Linear(fcl, 1)
        self.l102_v = nn.Conv2d(in_channels=k, out_channels=MAX_MOVE_LABEL_NUM, kernel_size=1)
        self.l103_v = nn.Linear(9*9*MAX_MOVE_LABEL_NUM, fcl)
        self.l104_v = nn.Linear(fcl, 1)

        self.norm1  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm2  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm3  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm4  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm5  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm6  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm7  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm8  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm9  = nn.BatchNorm2d(k, eps=2e-05)
        self.norm10 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm11 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm12 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm13 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm14 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm15 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm16 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm17 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm18 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm19 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm20 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm21 = nn.BatchNorm2d(k, eps=2e-05)
        #追加
        self.norm22 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm23 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm24 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm25 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm26 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm27 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm28 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm29 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm30 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm31 = nn.BatchNorm2d(k, eps=2e-05)

        self.norm32 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm33 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm34 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm35 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm36 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm37 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm38 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm39 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm40 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm41 = nn.BatchNorm2d(k, eps=2e-05)

        self.norm42 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm43 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm44 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm45 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm46 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm47 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm48 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm49 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm50 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm51 = nn.BatchNorm2d(k, eps=2e-05)
        #ここまで追加
        #追追加
        self.norm52 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm53 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm54 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm55 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm56 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm57 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm58 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm59 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm60 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm61 = nn.BatchNorm2d(k, eps=2e-05)

        self.norm62 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm63 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm64 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm65 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm66 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm67 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm68 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm69 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm70 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm71 = nn.BatchNorm2d(k, eps=2e-05)

        self.norm72 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm73 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm74 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm75 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm76 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm77 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm78 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm79 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm80 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm81 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm82 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm83 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm84 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm85 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm86 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm87 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm88 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm89 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm90 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm91 = nn.BatchNorm2d(k, eps=2e-05)

        self.norm92 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm93 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm94 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm95 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm96 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm97 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm98 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm99 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm100 = nn.BatchNorm2d(k, eps=2e-05)
        self.norm101 = nn.BatchNorm2d(k, eps=2e-05)
        #self.norm22_v = nn.BatchNorm2d(MAX_MOVE_LABEL_NUM, eps=2e-05)
        #self.norm52_v = nn.BatchNorm2d(MAX_MOVE_LABEL_NUM, eps=2e-05)
        self.norm102_v = nn.BatchNorm2d(MAX_MOVE_LABEL_NUM, eps=2e-05)
        self.swish = nn.SiLU()

    def forward(self, x1, x2):
        u1_1_1 = self.l1_1_1(x1)
        u1_1_2 = self.l1_1_2(x1)
        u1_2 = self.l1_2(x2)
        u1 = u1_1_1 + u1_1_2 + u1_2
        # Residual block 01
        h1 = self.swish(self.norm1(u1))
        h2 = self.swish(self.norm2(self.l2(h1)))
        u3 = self.l3(h2) + u1
        # Residual block 02
        h3 = self.swish(self.norm3(u3))
        h4 = self.swish(self.norm4(self.l4(h3)))
        u5 = self.l5(h4) + u3
        # Residual block 03
        h5 = self.swish(self.norm5(u5))
        h6 = self.swish(self.norm6(self.l6(h5)))
        u7 = self.l7(h6) + u5
        # Residual block 04
        h7 = self.swish(self.norm7(u7))
        h8 = self.swish(self.norm8(self.l8(h7)))
        u9 = self.l9(h8) + u7
        # Residual block 05
        h9 = self.swish(self.norm9(u9))
        h10 = self.swish(self.norm10(self.l10(h9)))
        u11 = self.l11(h10) + u9
        # Residual block 06
        h11 = self.swish(self.norm11(u11))
        h12 = self.swish(self.norm12(self.l12(h11)))
        u13 = self.l13(h12) + u11
        # Residual block 07
        h13 = self.swish(self.norm13(u13))
        h14 = self.swish(self.norm14(self.l14(h13)))
        u15 = self.l15(h14) + u13
        # Residual block 08
        h15 = self.swish(self.norm15(u15))
        h16 = self.swish(self.norm16(self.l16(h15)))
        u17 = self.l17(h16) + u15
        # Residual block 09
        h17 = self.swish(self.norm17(u17))
        h18 = self.swish(self.norm18(self.l18(h17)))
        u19 = self.l19(h18) + u17
        # Residual block 10
        h19 = self.swish(self.norm19(u19))
        h20 = self.swish(self.norm20(self.l20(h19)))
        u21 = self.l21(h20) + u19
        #h21 = self.swish(self.norm21(u21))

        #追加
        # Residual block 11
        h21 = self.swish(self.norm21(u21))
        h22 = self.swish(self.norm22(self.l22(h21)))
        u23 = self.l23(h22) + u21
        # Residual block 12
        h23 = self.swish(self.norm23(u23))
        h24 = self.swish(self.norm24(self.l24(h23)))
        u25 = self.l25(h24) + u23
        # Residual block 13
        h25 = self.swish(self.norm25(u25))
        h26 = self.swish(self.norm26(self.l26(h25)))
        u27 = self.l27(h26) + u25
        # Residual block 14
        h27 = self.swish(self.norm27(u27))
        h28 = self.swish(self.norm28(self.l28(h27)))
        u29 = self.l29(h28) + u27
        # Residual block 15
        h29 = self.swish(self.norm29(u29))
        h30 = self.swish(self.norm30(self.l30(h29)))
        u31 = self.l31(h30) + u29
        # Residual block 16
        h31 = self.swish(self.norm31(u31))
        h32 = self.swish(self.norm32(self.l32(h31)))
        u33 = self.l33(h32) + u31
        # Residual block 17
        h33 = self.swish(self.norm33(u33))
        h34 = self.swish(self.norm34(self.l34(h33)))
        u35 = self.l35(h34) + u33
        # Residual block 18
        h35 = self.swish(self.norm35(u35))
        h36 = self.swish(self.norm36(self.l36(h35)))
        u37 = self.l37(h36) + u35
        # Residual block 19
        h37 = self.swish(self.norm37(u37))
        h38 = self.swish(self.norm38(self.l38(h37)))
        u39 = self.l39(h38) + u37
        # Residual block 20
        h39 = self.swish(self.norm39(u39))
        h40 = self.swish(self.norm40(self.l40(h39)))
        u41 = self.l41(h40) + u39

        # Residual block 21
        h41 = self.swish(self.norm41(u41))
        h42 = self.swish(self.norm42(self.l42(h41)))
        u43 = self.l43(h42) + u41
        # Residual block 22
        h43 = self.swish(self.norm43(u43))
        h44 = self.swish(self.norm44(self.l44(h43)))
        u45 = self.l45(h44) + u43
        # Residual block 23
        h45 = self.swish(self.norm45(u45))
        h46 = self.swish(self.norm46(self.l46(h45)))
        u47 = self.l47(h46) + u45
        # Residual block 24
        h47 = self.swish(self.norm47(u47))
        h48 = self.swish(self.norm48(self.l48(h47)))
        u49 = self.l49(h48) + u47
        # Residual block 25
        h49 = self.swish(self.norm49(u49))
        h50 = self.swish(self.norm50(self.l50(h49)))
        u51 = self.l51(h50) + u49
        #h51 = self.swish(self.norm51(u51))
        #ここまで追加
        #追追加
        # Residual block 26
        h51 = self.swish(self.norm51(u51))
        h52 = self.swish(self.norm52(self.l52(h51)))
        u53 = self.l53(h52) + u51
        # Residual block 27
        h53 = self.swish(self.norm53(u53))
        h54 = self.swish(self.norm54(self.l54(h53)))
        u55 = self.l55(h54) + u53
        # Residual block 28
        h55 = self.swish(self.norm55(u55))
        h56 = self.swish(self.norm56(self.l56(h55)))
        u57 = self.l57(h56) + u55
        # Residual block 29
        h57 = self.swish(self.norm57(u57))
        h58 = self.swish(self.norm58(self.l58(h57)))
        u59 = self.l59(h58) + u57
        # Residual block 30
        h59 = self.swish(self.norm59(u59))
        h60 = self.swish(self.norm60(self.l60(h59)))
        u61 = self.l61(h60) + u59
        # Residual block 31
        h61 = self.swish(self.norm61(u61))
        h62 = self.swish(self.norm62(self.l62(h61)))
        u63 = self.l63(h62) + u61
        # Residual block 32
        h63 = self.swish(self.norm63(u63))
        h64 = self.swish(self.norm64(self.l64(h63)))
        u65 = self.l65(h64) + u63
        # Residual block 33
        h65 = self.swish(self.norm65(u65))
        h66 = self.swish(self.norm66(self.l66(h65)))
        u67 = self.l67(h66) + u65
        # Residual block 34
        h67 = self.swish(self.norm67(u67))
        h68 = self.swish(self.norm68(self.l68(h67)))
        u69 = self.l69(h68) + u67
        # Residual block 35
        h69 = self.swish(self.norm69(u69))
        h70 = self.swish(self.norm70(self.l70(h69)))
        u71 = self.l71(h70) + u69

        # Residual block 36
        h71 = self.swish(self.norm71(u71))
        h72 = self.swish(self.norm72(self.l72(h71)))
        u73 = self.l73(h72) + u71
        # Residual block 37
        h73 = self.swish(self.norm73(u73))
        h74 = self.swish(self.norm74(self.l74(h73)))
        u75 = self.l75(h74) + u73
        # Residual block 38
        h75 = self.swish(self.norm75(u75))
        h76 = self.swish(self.norm76(self.l76(h75)))
        u77 = self.l77(h76) + u75
        # Residual block 39
        h77 = self.swish(self.norm77(u77))
        h78 = self.swish(self.norm78(self.l78(h77)))
        u79 = self.l79(h78) + u77
        # Residual block 40
        h79 = self.swish(self.norm79(u79))
        h80 = self.swish(self.norm80(self.l80(h79)))
        u81 = self.l81(h80) + u79
        # Residual block 41
        h81 = self.swish(self.norm81(u81))
        h82 = self.swish(self.norm82(self.l82(h81)))
        u83 = self.l83(h82) + u81
        # Residual block 42
        h83 = self.swish(self.norm83(u83))
        h84 = self.swish(self.norm84(self.l84(h83)))
        u85 = self.l85(h84) + u83
        # Residual block 43
        h85 = self.swish(self.norm85(u85))
        h86 = self.swish(self.norm86(self.l86(h85)))
        u87 = self.l87(h86) + u85
        # Residual block 44
        h87 = self.swish(self.norm87(u87))
        h88 = self.swish(self.norm88(self.l88(h87)))
        u89 = self.l89(h88) + u87
        # Residual block 45
        h89 = self.swish(self.norm89(u89))
        h90 = self.swish(self.norm90(self.l90(h89)))
        u91 = self.l91(h90) + u89
        # Residual block 46
        h91 = self.swish(self.norm91(u91))
        h92 = self.swish(self.norm92(self.l92(h91)))
        u93 = self.l93(h92) + u91
        # Residual block 47
        h93 = self.swish(self.norm93(u93))
        h94 = self.swish(self.norm94(self.l94(h93)))
        u95 = self.l95(h94) + u93
        # Residual block 48
        h95 = self.swish(self.norm95(u95))
        h96 = self.swish(self.norm96(self.l96(h95)))
        u97 = self.l97(h96) + u95
        # Residual block 49
        h97 = self.swish(self.norm97(u97))
        h98 = self.swish(self.norm98(self.l98(h97)))
        u99 = self.l99(h98) + u97
        # Residual block 50
        h99 = self.swish(self.norm99(u99))
        h100 = self.swish(self.norm100(self.l100(h99)))
        u101 = self.l101(h100) + u99
        h101 = self.swish(self.norm101(u101))


        # policy network
        #h22 = self.l22(h21)
        #h22_1 = self.l22_2(torch.flatten(h22, 1))
        #h52 = self.l52(h51)
        #h52_1 = self.l52_2(torch.flatten(h52, 1))
        h102 = self.l102(h101)
        h102_1 = self.l102_2(torch.flatten(h102, 1))
        # value network
        #h22_v = self.swish(self.norm22_v(self.l22_v(h21)))
        #h23_v = self.swish(self.l23_v(torch.flatten(h22_v, 1)))
        #return h22_1, self.l24_v(h23_v)
        #h52_v = self.swish(self.norm52_v(self.l52_v(h51)))
        #h53_v = self.swish(self.l53_v(torch.flatten(h52_v, 1)))
        #return h52_1, self.l54_v(h53_v)
        h102_v = self.swish(self.norm102_v(self.l102_v(h101)))
        h103_v = self.swish(self.l103_v(torch.flatten(h102_v, 1)))
        
        return h102_1, self.l104_v(h103_v)
    
    def set_swish(self, memory_efficient=True):
        """Sets swish function as memory efficient (for training) or standard (for export).
        Args:
            memory_efficient (bool): Whether to use memory-efficient version of swish.
        """
        self.swish = nn.SiLU() if memory_efficient else Swish()
