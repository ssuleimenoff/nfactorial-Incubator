def trapping_rain_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    trapped_water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] < left_max:
                trapped_water += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                trapped_water += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return trapped_water


s = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapping_rain_water(s))
