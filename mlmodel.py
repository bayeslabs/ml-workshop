#import all the packages
from pycaret.datasets import get_data
from pycaret.regression import *
from pycaret.utils import check_metric

class MlMain:
    def __init__(self, modeltype):
        self.modeltype = modeltype

    def predictions(self, test_data, model):
        if self.modeltype == "regression":
            return predict_model(model, data=test_data)

    def getmetrics(self,metrics_stor, predictions, test_metrics):
        for i in test_metrics:
            metrics_stor[i] = check_metric(predictions['Price'], predictions.Label, i)
        return metrics_stor

    def savemodelFn(self, model, modelfilename):
        save_model(model, modelfilename)

    def mlmain(self):
        dataset = get_data('diamond')
        data = dataset.sample(frac=0.9, random_state=786)
        data_unseen = dataset.drop(data.index)
        data.reset_index(drop=True, inplace=True)
        data_unseen.reset_index(drop=True, inplace=True)
        modeltype= self.modeltype


        exp_reg102 = setup(data = data, target = 'Price', session_id=123,
                  normalize = True, transformation = True, transform_target = True, 
                  combine_rare_levels = True, rare_level_threshold = 0.05,
                  remove_multicollinearity = True, multicollinearity_threshold = 0.95, 
                  bin_numeric_features = ['Carat Weight'],
                  log_experiment = True, experiment_name = 'diamond1', silent=True)

        finalmodel = compare_models(exclude = ['ransac','lr'])
        topmodelnames = list(pull()[:1]['Model'])

        if modeltype == "classification":
            test_metrics = ['Accuracy', 'AUC', 'F1', 'Precision', 'Recall',
                            'Kappa']

        elif modeltype == "regression":
            test_metrics = ['MAE', 'MSE', 'RMSE', 'R2', 'RMSLE', 'MAPE']


        unseen_predictions = self.predictions(data_unseen,finalmodel)

        metrics_stor={"modeltrained":topmodelnames[0]}
        self.savemodelFn(model=finalmodel, modelfilename = 'diamond_mlmodelv1')

        for i in test_metrics:
            metrics_stor[i] = check_metric(unseen_predictions['Price'], unseen_predictions.Label, i)
            
        return metrics_stor

if __name__ == '__main__':
    m=MlMain("regression")
    print(m.mlmain())

