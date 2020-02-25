import sys

class Bank:
    def __init__(self,queue_num,queue_length,all_queue):
        self.time = 0
        self.queue_num = queue_num
        self.index = 0
        self.queue_length = queue_length
        self.total_num = len(all_queue)
        self.index2time = dict(zip(range(len(all_queue)),all_queue))
        self.queue = self.init_queue()
        self.now_server = dict(zip(range(self.queue_num),[[i,self.index2time[i]] for i in range(self.queue_num)])) #key:id value:queue
        self.wait_list = list(range(self.queue_num*self.queue_length,len(all_queue)))

    def init_queue(self):
        ret_list = [[-1 for i in range(self.queue_length)] for j in range(self.queue_num)]
        for i in range(self.total_num):
            if i // self.queue_num == self.queue_length:
                break
            # print(i,i%self.queue_num,i//self.queue_num)
            ret_list[i%self.queue_num][i//self.queue_num] = i
        return ret_list

    def next(self):
        # print(self.wait_list)
        min_time = sys.maxsize
        min_index = None
        for people in self.now_server.keys():
            if self.now_server[people][1] < min_time:
                min_index = people
                min_queue_num = self.now_server[people][0]
                min_time = self.now_server[people][1]
        if not self.now_server.keys():
            return None,None
        self.queue[min_queue_num].pop(0)
        if len(self.wait_list) == 0:
            pass
        else:
            next_people = self.wait_list.pop(0)
            self.queue[min_queue_num].append(next_people)
        # print(self.now_server)
        del self.now_server[min_index]
        for server_people in self.now_server.keys():
            self.now_server[server_people][1] -= min_time
        # print(self.queue,min_queue_num)
        if len(self.queue[min_queue_num]):
            # print(self.time,print(self.queue[min_queue_num][0]))
            self.now_server[self.queue[min_queue_num][0]] = [min_queue_num,self.index2time[self.queue[min_queue_num][0]]]

        self.time += min_time
        # print(self.time - self.index2time[min_index])
        if self.time - self.index2time[min_index] >= 60 * 9:
            # print(self.time)
            return None, None
        return self.time, min_index
if __name__ == '__main__':
    queue_num, queue_length, _,_ = list(map(lambda x: int(x), input().split(' ')))
    all_queue = list(map(lambda x: int(x), input().split(' ')))
    output_list = list(map(lambda x: int(x), input().split(' ')))
    bank = Bank(queue_num=queue_num,queue_length=queue_length,all_queue=all_queue)
    saver = {}
    for i in range(len(all_queue)):
        time, index = bank.next()
        if time == None:
            continue
        saver[index] = time
    for output in output_list:
        output = output -1
        if output not in saver.keys():
            print('sorry')
        else:
            time = saver[output]
            if output+1 == output_list[-1]:
                print('{}:{}'.format(8 + time // 60 if 8 + time // 60 >= 10 else '0' + str(8 + time // 60),
                                     time % 60 if time % 60 >= 10 else '0' + str(time % 60)),end='')
            else:
                print('{}:{}'.format( 8+time//60 if 8+time//60>=10 else '0'+str(8+time//60),
                                  time%60 if time%60>=10 else '0'+str(time%60)))
