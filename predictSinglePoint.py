def predictSinglePoint(dictionary,x):
    classes=dictionar.keys()
    best_p=-1000
    best_class=-1
    first_run=True
    
    for current_class in classes:
        if(current_class=="total_data"):
            continue
        p_current_class=probability(dictionary,x,current_class)
        if(first_run or p_current_class>best_p):
            best_p=p_current_class
            best_class=current_class
            first_run=False
    return best_class
