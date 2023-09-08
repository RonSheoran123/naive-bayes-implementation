def predict(dictionary,X_test):
    y_pred=[]
    for x in X_test:
        x_class=predictSinglePoint(dictionary,x)
        y_pred.append(x_class)
    return y_pred
