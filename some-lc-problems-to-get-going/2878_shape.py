import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    # note - .shape returns a tuple (H, W)

    # way 3
    return list(players.shape)

    # way 2
    h, w = players.shape
    return list(h, w)

    # way 1
    return list(players.shape)

    # way 0
    return [ len(players), len(players.columns) ]
