class BombaDiesel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.valor_litro = valor_litro
        self.quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if litros <= self.quantidade_disponivel:
            self.quantidade_disponivel -= litros
            return litros
        return 0

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_disponivel:
            self.quantidade_disponivel -= litros
            return litros * self.valor_litro
        return 0
