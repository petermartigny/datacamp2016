from sklearn.svm import SVR
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator
import numpy as np


class Regressor(BaseEstimator):                                                  
    def __init__(self):                                                          
        self.n_components = 50
        self.C = 100000
        self.epsilon = 0.2
        self.gamma = 50
        self.kernel = 'rbf'
                                    
        self.list_molecule = ['A', 'B', 'Q', 'R']                                
        self.dict_reg = {}        

        for mol in self.list_molecule:                                           
            self.dict_reg[mol] = Pipeline([                                      
                ('pca', PCA(n_components=self.n_components)),                    
                ('reg', SVR(C = self.C, 
                            epsilon = self.epsilon, 
                            gamma = self.gamma,
                           kernel = self.kernel))                                            
            ])                                                                
                                                                                 
    def fit(self, X, y):                                                         
        for i, mol in enumerate(self.list_molecule):                             
            ind_mol = np.where(np.argmax(X[:, -4:], axis=1) == i)[0]             
            XX_mol = X[ind_mol]                                                  
            y_mol = y[ind_mol].astype(float)                                     
            self.dict_reg[mol].fit(XX_mol, y_mol)                        
                                                                                 
    def predict(self, X):                                                        
        y_pred = np.zeros(X.shape[0])                                            
        for i, mol in enumerate(self.list_molecule):                             
            ind_mol = np.where(np.argmax(X[:, -4:], axis=1) == i)[0]             
            XX_mol = X[ind_mol].astype(float)                                    
            y_pred[ind_mol] = self.dict_reg[mol].predict(XX_mol)        
        return y_pred 
