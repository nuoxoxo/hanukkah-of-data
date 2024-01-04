import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # .shape returns a tuple (H, W)

    # Way 2
    h, w = players.shape
    return [h, w]
    # Way 1
    # return list(players.shape)
