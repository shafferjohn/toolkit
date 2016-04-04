**Readme:**
launch with params, like:
`python mts.py -d ./file -s shaffer -t 2`
> the filename of this script is mts.py
> `-d` means which folder (all files in it) do you search
> `-s` means what do you search for
> `-t` thread count
and then it will output the line no. and the content of the line.

About thread count
Recommend for SSD: thread counts of all your cpu(s),
e.g 4 cores and 8 thread counts, use the number 8.
Recommend for HDD: 2 or 4
Too many I/O running will slow down your machine.

**You can do what you want about this script.
By [Shaffer John][1]
[www.shaffer.cn][1]**

------
**使用方法：**
带参数执行，例如
`python mts.py -d ./file -s shaffer -t 2`
> 脚本文件是mts.py
> `-d` 查询文件夹（下的所有文件）
> `-s` 查询字符串
> `-t` 线程数
输出行数和所在行的内容

线程数
固态硬盘建议填CPU线程数
机械硬盘不要填太大，并发IO数太多反而更慢

**你可以任意修改此脚本
By [Shaffer John][1]
[www.shaffer.cn][1]**
[1]: http://www.shaffer.cn