def num_rushes(slope_height, rush_height_gain, back_sliding):
    """calculates the number of rushes needed for herbert to climb a slope"""
    slope_height-=rush_height_gain
    if slope_height <= 0:
        return 1
    slope_height+=back_sliding
    return 1 + num_rushes(slope_height, rush_height_gain, back_sliding)

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """calculates the number of rushes needed for herbert to climb a slope"""
    slope_height-=rush_height_gain
    if slope_height <= 0:
        return 1
    slope_height+=back_sliding
    rush_height_gain*=0.95
    back_sliding*=0.95
    return 1 + num_rushes(slope_height, rush_height_gain, back_sliding)