# 単純パーセプトロンクラス
class SimplePerceptron:

    # 初期化
    def __init__(self):
        self.input_n = 2                   # 入力を受ける個数(バイアス項は含まない)
        self.list_w = []                   # 重み
        self.eta = 0.1                     # 学習係数
        self.bias = 1                      # バイアス
        weight = 1                         # 重み初期
        for i in range(self.input_n + 1):  # 入力個数+バイアス分繰り返す
            self.list_w.append(weight)
                    
    # ステップ関数
    # グラフが階段状になる関数、num>0なら1、num≦0なら0を返す
    def step(self, num):
        if num > 0:
            return 1
        else:
            return 0
            
    # 内積
    def dot(self, list_x):
        sum = 0
        list_x.append(self.bias)               # リストxにハイアス項を追加する
        for x, w in zip(list_x, self.list_w):
            sum += x * w
        return sum
        
    # 逐次学習
    def train(self, list_x, y):
        ### list_x.append(self.bias)               # リストxにハイアス項を追加する
        o = self.feedforward(list_x)
        for i in range(self.input_n + 1):
            self.list_w[i] = self.list_w[i] + (y - o) * list_x[i] * self.eta
            
        ### self.print_w()
            
    
    # 出力
    # 0または1の数字を1つ返す
    def feedforward(self, list_x):
        ### list_x.append(self.bias)               # リストxにハイアス項を追加する
        return self.step(self.dot(list_x))

    # not出力
    # 0または1の数字を1つ返す
    def notfeedforward(self, list_x):
        y = self.feedforward(list_x)
        ### print("y = {0:d}".format(y))
        if y == 0:
            return 1
        else:
            return 0
        
    def print_w(self):
        print(self.list_w)
        
        
# 先生
class Teacher:
    # 初期化
    def __init__(self):
        self.epoch = 100
        
    
    def teach(self, student, td):
        for i in range(self.epoch):
            for j in range(td.len()):
                student.train(td.getx(j), td.gety(j))
        return student

# 学習データクラス
class TrainData:

    # 初期化
    def __init__(self, list_x, list_y):
        self.train_x = list_x
        self.train_y = list_y
   
    def len(self):
        return len(self.train_y)
       
    def getx(self, i):
        return self.train_x[i]
       
    def gety(self, i):
        return self.train_y[i]
       
       
#main処理,andを学習させる。
if __name__ == "__main__":
    andCircuit = SimplePerceptron()
    orCircuit = SimplePerceptron()
    tc = Teacher()
    andTd = TrainData([[0,0],[0,1],[1,0],[1,1]], [0,0,0,1])
    orTd = TrainData([[0,0],[0,1],[1,0],[1,1]], [0,1,1,1])
    
    andCircuit = tc.teach(andCircuit, andTd)
    orCircuit = tc.teach(orCircuit, orTd)
    
    print("--or--")

    print(orCircuit.feedforward([0,0]))
    print(orCircuit.feedforward([0,1]))
    print(orCircuit.feedforward([1,0]))
    print(orCircuit.feedforward([1,1]))
    
    print("--and--")
    
    print(andCircuit.feedforward([0,0]))
    print(andCircuit.feedforward([0,1]))
    print(andCircuit.feedforward([1,0]))
    print(andCircuit.feedforward([1,1]))
    
    
    print("--nand--")
    
    print(andCircuit.notfeedforward([0,0]))
    print(andCircuit.notfeedforward([0,1]))
    print(andCircuit.notfeedforward([1,0]))
    print(andCircuit.notfeedforward([1,1]))
    
    print("----")
    list_x = [[0,0],[0,1],[1,0],[1,1]]
    for x in list_x:
        print("X1 = {0:d}, X2 = {1:d} => ".format(x[0], x[1]), end='')
        orAns = orCircuit.feedforward([x[0], x[1]])
        ### print("orAns = {0:d}".format(orAns))
        
        nandAns = andCircuit.notfeedforward([x[0], x[1]])
        ### print("nandAns = {0:d}".format(nandAns))
        
        andAns = andCircuit.feedforward([x[0], x[1]])
        ### print("andAns = {0:d}".format(andAns))
        
        xorAns = andCircuit.feedforward([orAns, nandAns])
        ### print("xorAns = {0:d}".format(xorAns))
        print( "OR : {0:d}, NAND : {1:d}, XOR : {2:d}".format(orAns, nandAns, xorAns) )
 