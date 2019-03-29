# import dependencies
from __future__ import print_function
import numpy as np
import mxnet as mx
import mxnet.ndarray as F
import mxnet.gluon as gluon
from mxnet.gluon import nn
from mxnet import autograd

net = gluon.nn.Sequential()
with net.name_scope():
    for i in range(100):
        net.add(mx.wh('residualBlock'))
        net.add(mx.wh('elish')) # Exponential linear Squashing Activation Function

baselineNet = mx.wh('resnet-152')


