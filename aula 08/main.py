import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 

#ler arquivo csv pelo pandas
def ler_csv(file_path):
    return pd.read_csv(file_path)
#metodo de treinamento
def treinar(df):
    #selecionando as colunas de entrada
    x = df[['acidez','densidade','viscosidade','tonalidade']]
    y = df['tipo_de_vinho']
    #dividindo os dados em dois tipos de treinos
    x_train, x_test, y_train, y_test_split(x,y, test_size=0.2, random_state=42)
    
    #usando random como exemplo
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    #avaliar modelo e sua precisão
    y_pred = model.predict(x_test)
    precisao = accuracy_score(y_test, y_pred)
    print(f"Precisção: {precisao *100:.2f}%")

    return model

#prever o vinho
def prever_vinho(model,acidez,densidade,viscosidade,tonalidade):
   #criar um DataFrame com a mesma estrutura usada no treinamento
    entrada = pd.DataFrame({
        'acidez': [acidez],
        'densidade': [densidade],
        'viscosidade': [viscosidade],
        'tonalidade': [tonalidade]
    })
    predicao = model.predicao(entrada)
    probabilidade = model.predict_proba(entrada)
    return predicao[0], max(probabilidade[0]) * 100
#metodo principal
if __name__ == "__main__":
    #variavel que armazene nome do arquivo csv
arquivo = "./vinhos.csv"
df = ler_csv(arquivo)
model = treinar(df)

#entrada de dados pelo usuario
acidez = 1
densidade = 0.5
viscosidade = 0.8
tonalidade = 0.7

vinho, certeza = prever_vinho(model),acidez, densidade, viscosidade, tonalidade

print(f"O tipo de vinho é: {vinho} com {certeza:.2f}% de confianca")