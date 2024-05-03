#def solution(game_board, table):
#    return 0
## 240306
import numpy as np
from collections import deque, Counter
def print_table(table):
    for row in table:
        print(row)
    print()
    
def pad(table, val):
    VAL = val
    OP = 1 - VAL
    padded_H_W = len(table) + 2
    padded_table = np.zeros((padded_H_W, padded_H_W))
    padded_table.fill(OP)
    padded_table[1:-1, 1:-1] = np.array(table)
    return padded_table
    

def BFS(table, val):
    d0 = [0,0,1,-1]
    d1 = [1,-1,0,0]
    VAL = val
    OP = 1 - VAL
    H_W = len(table)
    visited = np.zeros((H_W, H_W))
    
    blocks = []
    for i in range(H_W):
        for j in range(H_W):
            #print(i, j, table[i,j], visited[i,j])
            if table[i, j] == VAL and visited[i, j] == 0:
                queue = deque([(i, j)])
                block = [(i, j)]
                while queue:
                    curi, curj = queue.popleft() # NOTE 틀린 부분. i, j 로 덮어 씌우면 for문에 문제가 생김.
                    visited[curi,curj] = 1
                    for k in range(4):
                        ni, nj = curi + d0[k], curj + d1[k]
                        if visited[ni, nj] == 0 and table[ni, nj] == VAL:
                            queue.append((ni, nj))
                            block.append((ni, nj))
                blocks.append(block)
    return blocks

def rotate_invariant(blocks):
    new_blocks = []
    for block in blocks:
        block = np.array(block)
        mn = (block.max(0) - block.min(0)) + 1
        H, W = mn[0], mn[1]
        block = block - block.min(0) # 상대위치로 변경
    
        new_block = np.zeros((H, W)) # NOTE 틀린 부분. 전에 여기를 정사각형으로 만들고 0인 행 열을 지웠는데, 정사각형으로 만들지 않으면, 0인 행 열을 지우는 수고를 하지 않아도 됨.
        for i, j in block:
            new_block[i, j] = 1
        
        rot_new_block = []
        
        for _ in range(4):
            new_block = np.rot90(new_block)
            tuple_new_block = []
            for row in new_block:
                tuple_new_block.append(tuple(row))
            rot_new_block.append(tuple_new_block)
        new_blocks.append(tuple(min(rot_new_block)))
        #print(tuple(min(rot_new_block)))
        
    return new_blocks
    
    

            
def solution(game_board, table):
    game_board, table = pad(game_board, 0), pad(table, 1)
    gb_blocks = BFS(game_board, 0)
    tb_blocks = BFS(table, 1)
    gb_inv_blocks = rotate_invariant(gb_blocks)
    tb_inv_blocks = rotate_invariant(tb_blocks)
    
    answer = 0
    for k, v in (Counter(tb_inv_blocks) & Counter(gb_inv_blocks)).items():
        answer += np.array(k).sum() * v
    
    
    return answer












#from collections import Counter
#from dataclasses import dataclass
#from itertools import product
#
#
#@dataclass(frozen=True)
#class Pos:
#    x: int
#    y: int
#
#    def neighbors(self): # 현재 점의 이웃 점을 모두 리턴
#        return [
#            Pos(self.x, self.y - 1),
#            Pos(self.x + 1, self.y),
#            Pos(self.x, self.y + 1),
#            Pos(self.x - 1, self.y),
#        ]
#
#
#def make_tile_from_positions(positions):
#    """Smallest possible representation with rotation"""
#
#    def rotate90(tile):
#        return tuple(
#            tuple(tile[i][j] for i in range(len(tile)))
#            for j in reversed(range(len(tile[0])))
#        )
#
#    positions = set(positions)
#
#    # 해당 블럭이 차지하는 x축, y축 최대 최소를 구함. 즉, 왼쪽 노란색 블럭을 배치하기 위해 3x3 의 크기가 필요하다는 것을 구하는 것.
#    xs = [pos.x for pos in positions]
#    min_x = min(xs) 
#    max_x = max(xs)
#
#    ys = [pos.y for pos in positions]
#    min_y = min(ys)
#    max_y = max(ys)
#
#    tile_representations = [
#        tuple(
#            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1))
#            for i in range(min_x, max_x + 1)
#        )
#    ]
#
#    for __ in range(3):
#        tile_representations.append(rotate90(tile_representations[-1]))
#
#    return min(tile_representations)
#
#
#def get_tile_size(tile):
#    return sum(sum(row) for row in tile)
#
#
#def parse_tiles(board, tile_value=1):
#    n = len(board)
#
#    # Add sentinel boundaries
#    sentinel = 1 - tile_value
#
#    board = [
#        [sentinel] * (n + 2),
#        *([sentinel] + row + [sentinel] for row in board),
#        [sentinel] * (n + 2),
#    ] # tile_value 가 아닌 값으로 board 를 둘러싸서 새로운 board 를 만듬
#
#    # Detect tiles
#    tile_positions = []
#    for i, j in product(range(1, n + 1), range(1, n + 1)): # 모든 점에 대해
#        if board[i][j] == tile_value: # DFS
#            stack = [Pos(i, j)] # Pos 객체 생성
#            squares = []
#            while stack:
#                curr = stack.pop()
#                board[curr.x][curr.y] = sentinel # 여기서 board 값을 역으로 바꿔버리고 이것이 visitied 를 대신하기에 중복된 타일은 들어가지 않음
#                squares.append(curr) # 하나의 block 에 대응하는 모든 점을 담은 것이 squares
#                for neighbor in curr.neighbors(): # 모든 이웃에 대해
#                    if board[neighbor.x][neighbor.y] == tile_value: # 타일값이면 stack 에 추가
#                        stack.append(neighbor)
#            tile_positions.append(squares)
#
#    # Make tiles
#    """
#    tile_positions 는 모든 블럭의 각 position
#    예) table 의 tile_positions
#    [
#    [Pos(x=1, y=1), Pos(x=2, y=1)], 
#    [Pos(x=1, y=4), Pos(x=1, y=5), Pos(x=2, y=5), Pos(x=3, y=5), Pos(x=3, y=6)], 
#    [Pos(x=2, y=3), Pos(x=3, y=3), Pos(x=4, y=3), Pos(x=3, y=2)], 
#    [Pos(x=5, y=1), Pos(x=5, y=2), Pos(x=6, y=2)], 
#    [Pos(x=5, y=4), Pos(x=5, y=5)]
#    ]
#    
#    game_board 의 tiles
#    [
#    [Pos(x=1, y=3), Pos(x=1, y=4), Pos(x=2, y=4), Pos(x=3, y=4), Pos(x=3, y=5)], 
#    [Pos(x=1, y=6), Pos(x=2, y=6)], 
#    [Pos(x=2, y=1), Pos(x=2, y=2), Pos(x=3, y=1)], 
#    [Pos(x=4, y=3), Pos(x=5, y=3), Pos(x=5, y=4), Pos(x=5, y=2)], 
#    [Pos(x=5, y=6), Pos(x=6, y=6), Pos(x=6, y=5)], 
#    [Pos(x=6, y=1)]
#    ]
#    """
#    tiles = [make_tile_from_positions(p) for p in tile_positions]
#    #print(len(tiles[0][0]))
#    """
#    예) table 의 tiles. 어차피 블럭을 배치한 이후 인접한 칸이 비면 안되기 때문에, game_board 나 table 이나 모든 블럭을 회전 포함해서 하나의 표현으로 바꾼 것. 그러면 & 연산 만으로도 블럭 배치가 가능한지 확인이 됨. 회전에 대해 모두 연산 후 min 을 취하는 이유는 game_board 와 table 의 블럭이 어떤 각도인지 알 수 없기 때문. 이를 하나의 각도로 동기화 하는 것.
#    [
#    ((True,), (True,)), # 2x1 반경에서 둘 다 True 이어야 배치 가능
#    ((False, False, True), (True, True, True), (True, False, False)), 3x3 반경에서 min 을 뽑으면 한가지 각도에서의 블럭의 True 상태로 표현됨
#    ((False, True), (True, True), (False, True)), 
#    ((False, True), (True, True)), 
#    ((True,), (True,))
#    ]
#    
#    game_board 의 tiles
#    [
#    ((False, False, True), (True, True, True), (True, False, False)), 
#    ((True,), (True,)), 
#    ((False, True), (True, True)), 
#    ((False, True), (True, True), (False, True)), 
#    ((False, True), (True, True)), 
#    ((True,),)
#    ]
#    """
#
#    return tiles
#
#
#def solution(game_board, table):
#    tiles = parse_tiles(table, 1)
#    empty_spaces = parse_tiles(game_board, 0)
#
#    tile_counter = Counter(tiles)
#    empty_space_counter = Counter(empty_spaces)
#
#    used_tiles = tile_counter & empty_space_counter
#
#    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())



# 240129 버전
#from collections import deque
#import numpy as np
#def blocks_to_bool(blocks):
#    bool_list = []
#    for block in blocks:
#        #block = set(block)
#        xs = np.array([point[0] for point in block])
#        ys = np.array([point[1] for point in block])
#        len_x = xs.max() - xs.min() + 1
#        len_y = ys.max() - ys.min() + 1
#        block_range = np.zeros((max(len_x, len_y), max(len_x, len_y)), dtype=bool)
#        
#        xs = xs - xs.min() # NOTE 상대적인 위치 틀림. xs[0] ys[0] 을 빼야한다고 생각했는데, 그건 xs[0] ys[0] 이 최좌상단이라는 가정일때만 가능. 근데 왼쪽 table (1) 은 최좌상단이 아님
#        ys = ys - ys.min()
#        
#        #indices = np.concatenate([xs.reshape(-1,1), ys.reshape(-1,1)], axis=1) # 각 index 에 빠르게 값 넣는 방법 필요
#        for x, y in zip(xs.tolist(), ys.tolist()):
#            block_range[x, y] = True
#            
#        #print(block_range)
#        
#        # block_range : 각 block 의 최대 범위를 표현하는 map 에서 block 표현
#        """ 예
#        [[1 0 0]
#         [1 1 1]
#         [0 0 0]]
#        """
#        
#        # 모든 회전을 포함해서 하나의 표현으로 변환 NOTE 틀린 부분 np.rot90
#        rotations = []
#        for i in range(4):
#            # NOTE 틀린 부분. 모두 0인 행과 열을 지워야 테케 6~9, 10 통과. 정사각형에서 회전하고 비교하는 경우, 빈공간 때문에 다른 부분이 생기나 봄.
#            rot = np.rot90(block_range, i)
#            # 모두 0인 행 찾기
#            nonzero_rows = np.any(rot != False, axis=1)
#            # 모두 0인 열 찾기
#            nonzero_columns = np.any(rot != False, axis=0)
#            # 0이 아닌 행과 열 선택
#            rot = rot[nonzero_rows][:, nonzero_columns]
#            # NOTE 틀린 부분. Counter 는 list(tuple) 만 가능한데, 2차원 list 는 바로 tuple 로 바꿀 수가 없어서 1차원 list 마다 tuple 로 바꿔야 함.
#            rotations.append(
#                tuple(tuple(row) for row in rot)
#            )
#            
#        
#        # NOTE 틀린 부분. list 에 대한 min.
#        # list 에 대한 min 이면 4가지 중 위치정보로 앞에서부터 봤을 때 가장 작은 것만 남길 수 있음
#        #print("rotations", rotations)
#        min_rotations = min(rotations)
#        bool_list.append(min_rotations)
#        
#        
#            
#    return bool_list
#    
#def DFS(graph:np.array, val:int):
#    d1 = [0, 0, -1, 1]
#    d2 = [1, -1, 0, 0]
#    VAL = val
#    OP = 1 - VAL
#    # boundary 생성
#    graph_new = np.zeros((graph.shape[0]+2, graph.shape[1]+2), dtype=int)
#    graph_new.fill(OP)
#    graph_new[1:-1, 1:-1] = graph
#    graph = graph_new
#    blocks = []
#    for i in range(1, graph.shape[0]):
#        for j in range(1, graph.shape[1]):
#            block = []
#            if graph[i][j] == VAL:
#                stack = deque([[i, j]])
#                while stack:
#                    x, y = stack.pop()
#                    block.append((x, y))
#                    graph[x][y] = OP
#                    for k in range(4):
#                        nx, ny = x+d1[k], y+d2[k]
#                        if graph[nx][ny] == VAL:
#                            stack.append((nx, ny))
#                blocks.append(block)
#    return blocks
#    
#from collections import Counter
#def solution(game_board, table):
#    answer = -1
#    #DFS for blocks
#    #blocks to matching information
#    gb_blocks = DFS(np.array(game_board), 0)
#    tb_blocks = DFS(np.array(table), 1)
#    gb_bool_list = blocks_to_bool(gb_blocks)
#    tb_bool_list = blocks_to_bool(tb_blocks)
#    #print(gb_blocks, "\n", tb_blocks)
#    gb = Counter(gb_bool_list)
#    tb = Counter(tb_bool_list)
#    #print(gb, "\n", tb)
#    ret = gb & tb
#    #print([(block, num) for block, num in ret.items()])
#    #return 0
#    """
#    NOTE 틀린 부분. & 연산 결과. 즉, 교집합과 그 숫자를 세어 반환함
#    Counter(
#    {
#        ((False, False, True), (True, True, True), (True, False, False)): 1, 
#        ((False, False), (True, True)): 1, 
#        ((False, True), (True, True)): 1
#    }
#    )
#    """
#    def num_tiles(block):
#        # NOTE 에러 TypeError: Object of type int64 is not JSON serializable
#        # 해결: int 로 감싸서 type 을 맞춰줌
#        return int(sum([sum(row) for row in block]))
#    return sum([num_tiles(block) * num for block, num in ret.items()]) # NOTE 틀린 부분. 같은 모양이 여러 개 일 수 있으므로 num 을 곱해야 함

# 240129 이 함수만 복습함
#def blocks_to_bool(blocks):
#    bool_list = []
#    for block in blocks:
#        Xs = list(map(lambda x:x[0], block))
#        Ys = list(map(lambda x:x[1], block))
#        max_len = max(max(Xs) - min(Xs) + 1, max(Ys) - min(Ys) + 1)
#        
#        block_table = np.zeros((max_len, max_len), dtype = bool)
#        xindices, yindices = np.array(Xs) - min(Xs), np.array(Ys) - min(Ys)
#        for x, y in zip(xindices, yindices):
#            block_table[x, y] = True
#            
#        block_list = []
#        for i in range(4):
#            rot_table = np.rot90(block_table, i)
#            nonzero_x_ids = rot_table.any(axis=1, where=True) # NOTE 틀린부분. 가로가 axis 0 이고, 세로가 axis 1
#            nonzero_y_ids = rot_table.any(axis=0, where=True)
#            #print("\n origin", block_table, "indices", nonzero_x_ids, nonzero_y_ids)
#            try:
#                #rot_table = rot_table[nonzero_x_ids, nonzero_y_ids] # NOTE 틀린 부분. 이렇게 하면 3,3 이 아니면 에러나고, 아래처럼 해야 3,3 처럼 정사각형에 대한 bool ids 가 아니어도 에러가 안 남
#                rot_table = rot_table[nonzero_x_ids][:, nonzero_y_ids]
#            except Exception as e: # NOTE 틀린 부분. Exception 을 print 하는 방법
#                print(e, "\n-->", rot_table)
#            #print(f"{i*90}-->", rot_table)
#            block_list.append(tuple(tuple(row.tolist()) for row in rot_table))
#            
#        block_min = min(block_list)
#        bool_list.append(block_min)
#        #print(block_min)
#    return bool_list

# 240130
#from collections import deque
#import numpy as np
#def blocks_to_bool(blocks):
#    bool_list = []
#    for block in blocks:
#        Xs = list(map(lambda x:x[0], block))
#        Ys = list(map(lambda x:x[1], block))
#        max_len = max( max(Xs) - min(Xs) + 1, max(Ys) - min(Ys) + 1)
#        block_table = np.zeros((max_len, max_len), dtype=bool)
#        for x, y in zip(Xs, Ys):
#            block_table[x - min(Xs), y - min(Ys)] = True
#        rot_list = []
#        for i in range(4):
#            rot = np.rot90(block_table, i)
#            xids = rot.any(axis=1, where=True)
#            yids = rot.any(axis=0, where=True)
#            rot = rot[xids][:, yids]
#            rot_list.append(tuple(tuple(row) for row in rot))
#        bool_list.append(min(rot_list))
#            
#    return bool_list
#    
#def DFS(graph:np.array, val:int):
#    d1 = [0, 0, -1, 1]
#    d2 = [-1, 1, 0, 0]
#    VAL = val
#    OP  = 1 - VAL
#    
#    ext_graph = np.zeros((graph.shape[0] + 2, graph.shape[1] + 2), dtype=int)
#    ext_graph.fill(OP)
#    ext_graph[1:-1, 1:-1] = graph
#    graph = ext_graph
#    
#    blocks = []
#    for i in range(1, graph.shape[0]):
#        for j in range(1, graph.shape[1]):
#            block = []
#            if graph[i, j] == VAL:
#                stack = deque([(i, j)])
#                while stack:
#                    x, y = stack.pop()
#                    block.append((x, y))
#                    graph[x, y] = OP
#                    for k in range(4):
#                        nx, ny = x + d1[k], y + d2[k]
#                        if graph[nx, ny] == VAL:
#                            stack.append((nx, ny))
#                blocks.append(block)
#    return blocks
#    
#from collections import Counter
#def solution(game_board, table):
#    ag = DFS(np.array(game_board), 0)
#    at = DFS(np.array(table), 1)
#    
#    bg = Counter(blocks_to_bool(ag))
#    bt = Counter(blocks_to_bool(at))
#    
#    intersection = bg & bt
#    
#    def num_tiles(block, num):
#        return sum([sum(row) for row in block]) * num
#    #return sum([num_tiles(block, num) for block, num in intersection.items()])
#    return int(sum([num_tiles(block, num) for block, num in intersection.items()]))

