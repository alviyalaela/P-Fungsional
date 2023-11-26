def group_heights(heights, interval_size):
    grouped_heights = {}
    
    for height in heights:
        group_key = (height // interval_size) * interval_size
        if group_key not in grouped_heights:
            grouped_heights[group_key] = {'interval': f"{group_key}-{group_key + interval_size - 1}", 'frequencies': 0}
        grouped_heights[group_key]['frequencies'] += 1
    
    return grouped_heights

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

grouped_heights = group_heights(tinggi_badan, interval_size)

for group_key, data in grouped_heights.items():
    print(f"Interval {data['interval']} : {data['frequencies']} orang")
