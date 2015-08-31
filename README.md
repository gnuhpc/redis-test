# 测试说明

本测试基于的redis版本为3.0.3, 目标是对该版本的redis内存占用进行beachmark测试，摸清各类数据结构占用内存的基本增长趋势。

测试机器OS为：
>
SUSE Linux Enterprise Server 11 (x86_64)
VERSION = 11
PATCHLEVEL = 2
>

测试python版本为：
>
Python 2.6 (r26:66714, May  6 2011, 15:10:21)
[GCC 4.3.4 [gcc-4_3-branch revision 152973]] on linux2

#测试过程

采用redis-python客户端进行内存写入，在写入之前进行flushdb，写入完毕后获取info信息中的内存占用情况。

