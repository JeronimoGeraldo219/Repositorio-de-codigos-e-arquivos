def print_board(board):
    """
    Função auxiliar que imprime o tabuleiro atual.
    """
    for i in range(3):
        print(' | '.join(board[i]))
        if i != 2:
            print('---------')

def check_win(board):
    """
    Função auxiliar que verifica se alguém ganhou o jogo.
    Retorna 'X' se o jogador X ganhou, 'O' se o jogador O ganhou,
    'empate' se houve um empate ou None se o jogo ainda não acabou.
    """
    # Verifica linhas
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Verifica colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Verifica se há empate
    if all([cell != ' ' for row in board for cell in row]):
        return 'empate'
    # Se ainda não acabou, retorna None
    return None

def get_move(player):
    """
    Função auxiliar que pede ao jogador atual para escolher sua jogada.
    Retorna um par (row, col) com as coordenadas escolhidas.
    """
    print(f'É a vez do jogador {player}.')
    while True:
        move = input('Digite a linha e coluna desejadas (ex: 1 2): ')
        try:
            row, col = [int(num) - 1 for num in move.split()]
            if row not in range(3) or col not in range(3):
                raise ValueError
            break
        except ValueError:
            print('Coordenadas inválidas. Tente novamente.')
    return row, col

def play_game():
    """
    Função principal que controla o jogo completo.
    """
    board = [[' ', ' ', ' '] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        row, col = get_move(current_player)
        if board[row][col] != ' ':
            print('Esta célula já está ocupada. Tente novamente.')
            continue
        board[row][col] = current_player
        winner = check_win(board)
        if winner:
            print_board(board)
            if winner == 'empate':
                print('O jogo empatou!')
            else:
                print(f'O jogador {winner} ganhou!')
            break
        # Alterna o jogador atual
        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == '__main__':
    play_game()
