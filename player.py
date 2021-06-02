class Player():
    def __init__(self):
        self.heights = []
        self.chosen_position = None
        self.chosen_rotation = None

    def calculate_heights(self, board):
        # Necesitaremos: board.width, board.height, board.cells. Y "rellenar" self.heights.
        for i in board.width:
            height = 0
            for j in board.height:
                # (i,j) es un cuadrado del tablero
                if (i,j) in board.cells and j > height:    # Si True, significa que "está llena"
                    height = j
            self.heights.append(height)


    def sum_heights(self, board):   # HECHO
        # Rellenamos self.heights
        self.calculate_heights(board)

        return sum(self.heights)

        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]  
        # [0,0,0,0,0,0,0,0,0,0]   
            
    def calculate_squares(self, board): #Calcular si el cuadrante esta relleno         
          
        matriz_cuadrantes = []   
        for h in board.height:
            matriz_cuadrantes.append([])
            for w in board.width:
                if (h,w) in board.cells:
                    matriz_cuadrantes[h - 1].append(1)
                else:
                    matriz_cuadrantes[h - 1].append(0)
                    
    def holes_count(self, board):
        pass
    def calculate_bumpiness(self, board):
        self.calculate_heights(board)
        pass


    def count_cleared_lines(self,board,previous_score):
        # new_score - previous_score
        pass
    
    
    def find_best_move(self,board):
        # Llamará las de arriba
        
        # Iterar por todas las rotaciones y movimientos posibles
        # Crear para cada rotación y movimiento posible, un tablero sandbox (sandbox = board.clone())
        # En el sandox, harás los movimientos y rotaciones, calcularás current_score, y verás si supera un best_score
        # Para el best_score, guardarás self.chosen_position, self.chosen_rotation
        pass

    def choose_action(self):
        pass