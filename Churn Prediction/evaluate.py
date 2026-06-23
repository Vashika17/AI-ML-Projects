from sklearn.metrics import classification_report, roc_auc_score

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
    
    try:
        probs = model.predict_proba(X_test)[:,1]
        print("ROC-AUC:", roc_auc_score(y_test, probs))
    except:
        pass
