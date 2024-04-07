def find_min_cost_and_coupons(n, costs):
    sorted_costs = sorted(enumerate(costs), key=lambda x: -x[1])
    
    total_cost = sum(costs)  
    coupons = 0             
    unused_coupons = 0      
    used_coupons_days = []   
    for day, cost in sorted_costs:
        if cost > 100:          
            coupons += 1
        if coupons > 0:       
            total_cost -= cost
            coupons -= 1       
            used_coupons_days.append(day + 1) 
    
    unused_coupons = coupons
    
    return total_cost, unused_coupons, len(used_coupons_days), sorted(used_coupons_days)

n = int(input().strip()) 
costs = [int(input().strip()) for _ in range(n)]  

min_cost, unused_coupons, used_coupons_count, used_coupons_days = find_min_cost_and_coupons(n, costs)

print(min_cost)
print(unused_coupons, used_coupons_count)
print("\n".join(map(str, used_coupons_days)))