"""
 MapReduce Whole process
 1. (Start)User program start master and worker.
2. (Assign Task)Master assign task to the map worker and reduce worker.
(Assign Map and Reduce code)
3. (Split)Master Split the input data.
4. (Map Read)Each map worker read the split input data.
5. (Map)Each map worker do the “Map” job on their machine.
6. (Map output)Each map worker output the file in the local disk of its worker.
7. (Reduce Fetch)Each reduce worker fetch the data from the map worker.
8. (Reduce)Each Reducer worker do the “Reduce” job on their machine.
9. (Reduce output) Reduce worker output the final output data.

1. Mapper 和 Reducer是同时工作还是Mapper 先工作Reducer再工作? Mapper要结束了后Reducer才能运行
2. 运行过程中一个Mapper或者Reducer挂了怎么办? 重新分配一台机器做
3. Reducer一个机器Key数目特别多怎么办? 加一个random后缀，类似Shard Key
4. Input 和 Output 存放在哪? 存放在GFS里面
5. Local Disk 上面的Mapper output data有没有必要保存在GFS上面?要是丢了怎么办? 不需要，丢了重做就好
6. Mapper 和 Reducer 可以放在同一台机器么?
这样设计并不是特别好，Mapper 和Reducer之前都有很多需要预处理的工作。两台机器可以并行的预处理。

"""