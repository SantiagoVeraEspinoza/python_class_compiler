class Config:
    def __init__(self, datos):
        for clave, valor in datos.items():
            setattr(self, clave, valor)

cfg = Config({"modo": "debug", "nivel": 3})
print(cfg.modo, cfg.nivel)