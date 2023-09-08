def probability(dictionary,x,current_class):
    output=np.log(dictionary[current_class]["total_count"])-np.log(dictionary["total_data"])
    num_features=len(dictionary[current_class].keys())-1
    for j in range(1,num_features+1):
        xj=x[j-1]
        count_current_class_with_value_xj=dictionary[current_class][j][xj]+1
        count_current_class=dictionary[current_class]["total_count"]+len(dictionary[current_class][j].keys())
        current_xj_probability=np.log(count_current_class_with_value_xj)-np.log(count_current_class)
        output=output+current_xj_probability
    return output
