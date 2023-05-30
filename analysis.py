from gameState import ProcessGameState

def a(game, team, team_side):
    data = game.data
    filtered_data = data[(data.team == team) & (data.side == team_side)]
    valid_rows = game.check_boundary()
    ans = filtered_data.index.isin(valid_rows)
    return ans.mean()


def b(game, team, team_side, site):
    data = game.data
    filtered_data = data[(data.team == team) & (data.side == team_side)]

def c():
    pass

def main():
    file_path = 'game_state_frame_data.pickle'
    ZBOUNDS = [285, 421]
    BOUNDS = [[-1735, 250],[-2024, 398],[-2806, 742],[-2472, 1233], [-1565, 580]]
    
    game = ProcessGameState(file_path, ZBOUNDS, BOUNDS)


    print("Q: Is entering via the light blue boundary a common strategy used by Team2 on T (terrorist) side?")
    THRESHOLD = 0.5
    if a(game, 'Team2', 'T') > THRESHOLD:
        print("answer ===> yes, it is a common strat.")
    else:
        print("answer ===> no, it is not a common strat.")

if __name__ == "__main__":
    main()