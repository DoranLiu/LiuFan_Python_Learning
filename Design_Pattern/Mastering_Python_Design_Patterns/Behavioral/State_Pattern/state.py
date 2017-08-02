'''
状态设计模式(State design pattern)

状态机可用于解决多种不同的问题，包括非计算机的问题。非计算机的例子包括自动售货机、电梯、交通灯、暗码锁、停车计时器、自动加油泵及自然语言文法描述。
计算机方面的例子包括 游戏编程和计算机编程的其他领域、硬件设计、协议设计，以及编程语言解析(请参考网页[t.cn/RUFNdYt]和网页[t.cn/zY5jPeH])。

例子：
这里再一次提到零食自动售货机(在之前的第10章中见过)，它也是日常生活中状态模式的一个例子。
自动售货机有不同的状态，并根据我们放入的钱币数量作出不同反应。根据我们的选 择和放入的钱币，机器会执行以下操作。
 拒绝我们的选择，因为请求的货物已售罄。
 拒绝我们的选择，因为放入的钱币不足。
 递送货物，且不找零，因为放入的钱币恰好足够。
 递送货物，并找零。
'''
from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


@acts_as_state_machine
class Process:
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    wait = Event(from_states=(created, running, blocked,
                              swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked),
                  to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print('Error: transition of {} from {} to {} failed'.format(process.name,
                                                                    process.current_state, event_name))


def state_info(process):
    print('state of {}: {}'.format(process.name, process.current_state))


def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

if __name__ == '__main__':
    main()
