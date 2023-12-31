import numpy as np

class MLP:
    def __init__(self, entradas, saidas_desejadas, pesos_camada_entrada, pesos_camada_saida, taxa_aprendizado, num_epocas):
        self.entradas = entradas
        self.saidas_desejadas = saidas_desejadas 
        self.pesos_camada_entrada = pesos_camada_entrada
        self.pesos_camada_saida = pesos_camada_saida
        self.taxa_aprendizado = taxa_aprendizado
        self.num_epocas = num_epocas

    # Função de ativação (usaremos a sigmoid)
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Derivada da função de ativação sigmoid
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    # Função para treinar a MLP
    def treinar_mlp(self):
        for _ in range(self.num_epocas):
            # Feedforward
            camada_entrada = self.entradas
            soma_sinapse_entrada = np.dot(camada_entrada, self.pesos_camada_entrada)
            camada_oculta = self.sigmoid(soma_sinapse_entrada)
            soma_sinapse_saida = np.dot(camada_oculta, self.pesos_camada_saida)
            camada_saida = self.sigmoid(soma_sinapse_saida)

            # Cálculo do erro
            erro = self.saidas_desejadas - camada_saida

            # Backpropagation
            delta_saida = erro * self.sigmoid_derivative(camada_saida)
            delta_oculta = delta_saida.dot(self.pesos_camada_saida.T) * self.sigmoid_derivative(camada_oculta)

            # Atualização dos pesos
            self.pesos_camada_saida += camada_oculta.T.dot(delta_saida) * self.taxa_aprendizado
            self.pesos_camada_entrada += camada_entrada.T.dot(delta_oculta) * self.taxa_aprendizado

        return self.pesos_camada_entrada, self.pesos_camada_saida
    