#اسلام الامير عبدالله 
#سكشن 2
def sort_heights(heights):
    for i in range(1, len(heights)):  
        current_height = heights[i]
        j = i - 1
        while j >= 0 and current_height < heights[j]:  
            heights[j + 1] = heights[j]
            j -= 1
        heights[j + 1] = current_height 


heights = [150, 140, 160, 130, 155]  
print("قبل الترتيب:", heights)
sort_heights(heights)
print("بعد الترتيب:", heights)