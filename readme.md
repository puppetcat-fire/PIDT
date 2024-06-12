使用jidt计算随机生成的4*4的元胞自动机的第6列和第8列的转移熵和互信息。
test.py 参考https://blog.csdn.net/qq_40680263/article/details/98773037 会生成4*4的元胞自动机的最长100行的列表，因为列表会覆盖掉out.txt所以可以等到循环出现时再计算该元胞自动机的信息。
main.py是主程序入口，计算了第6列和第8列数据的转移熵和互信息。
- initJVM中初始化了jar的环境相关。
- mi是调用了infodynamics.measures.continuous.kraskov MutualInfoCalculatorMultiVariateKraskov1来计算互信息，参考python示例6
- te是调用了infodynamics.measures.discrete TransferEntropyCalculatorDiscrete来计算转移熵，参考python示例2
demo.py是参考https://blog.csdn.net/fangsfdavid/article/details/118353170 中对jidt的转移熵的计算的调用，将其用于生成的数据上使用。