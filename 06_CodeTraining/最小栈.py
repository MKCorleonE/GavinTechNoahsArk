"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int value) 将元素 value 推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""

# 最佳答案，辅助栈
class MinStack:
    def __init__(self):   # 初始化栈，包括主栈和辅助栈
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:   # 将元素 x 推入主栈 stack，并根据条件将其推入辅助栈 min_stack
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: 
            self.min_stack.append(x)
    def pop(self) -> None:   # 弹出主栈 stack 的栈顶元素，并根据条件弹出辅助栈 min_stack 的栈顶元素
        if self.stack.pop() == self.min_stack[-1]:  # 注意：pop() 方法会返回被弹出的元素值，所以可以直接与 min_stack 的栈顶元素比较
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]

# 复杂度分析：
# 时间复杂度：O(1)，每个操作都是常数时间。
# 空间复杂度：O(n)，最坏情况下，辅助栈的大小与主栈相同。

# 思路
# 借用一个辅助栈 min_stack，用于存获取 stack 中最小值。
# 
# 算法流程：
# push() 方法： 每当push()新值进来时，如果 小于等于 min_stack 栈顶值，则一起 push() 到 min_stack，即更新了栈顶最小值；
# pop() 方法： 判断将 pop() 出去的元素值是否是 min_stack 栈顶元素值（即最小值），如果是则将 min_stack 栈顶元素一起 pop()，这样可以保证 min_stack 栈顶元素始终是 stack 中的最小值。
# getMin()方法： 返回 min_stack 栈顶即可。
#
# min_stack 作用分析：
# min_stack 等价于遍历 stack所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈。
# 相当于给 stack 中的降序元素做了标记，每当 pop() 这些降序元素，min_stack 会将相应的栈顶元素 pop() 出去，保证其栈顶元素始终是 stack 中的最小元素。
