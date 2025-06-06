# AyCromo YOLOv8 API 🔬🧬

API local desenvolvida em Python com Flask utilizando o modelo `YOLOv8` para contagem de cromossomos em imagens microscópicas. Essa API pode ser integrada com aplicativos Flutter ou outras interfaces para análise automatizada de imagens citogenéticas.

## 📦 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Flask 2.3.3](https://flask.palletsprojects.com/)
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- [PyTorch](https://pytorch.org/)
- [Pillow](https://python-pillow.org/)

---

## 🧠 Modelo

O modelo `best.pt` foi treinado com YOLOv8 para detecção de cromossomos. Ele deve estar na raiz do projeto ou no caminho configurado no código:

```python
model = YOLO("best.pt")
```

### ✅ Métricas principais do modelo

| Métrica           | Valor  | Interpretação                                                                 |
|-------------------|--------|-------------------------------------------------------------------------------|
| **Precision**     | 1.00   | O modelo **não gerou falsos positivos** – tudo o que ele detectou era válido |
| **Recall**        | 0.624  | O modelo detectou cerca de **62% dos cromossomos reais** nas imagens         |
| **mAP@50**        | 0.887  | Alta qualidade de detecção com IoU ≥ 0.5                                     |
| **mAP@50-95**     | 0.683  | Excelente desempenho geral em múltiplos thresholds de IoU                    |
| **Fitness**       | 0.70   | Pontuação composta usada pelo YOLO – acima de 0.6 já é considerada ótima     |

### 🔍 O que isso significa?

- ✅ Seu modelo **acerta muito bem o que ele detecta** (precision = 1.0)
- ⚠️ **Pode estar perdendo alguns cromossomos reais** (recall = 62%)
- 📈 **Desempenho muito bom** para uso prático (mAP elevado e fitness > 0.6)
- 💡 Para melhorar recall: adicione mais imagens ou aumente o número de épocas de treinamento

---

## 📁 Estrutura do Projeto
aycromo_yolo_api/
├── best.pt                  # Modelo treinado YOLOv8
├── main.py                  # Código principal da API
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo

---

## 🛠️ Instalação

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/aycromo_yolo_api.git
cd aycromo_yolo_api

pip install -r requirements.txt

python main.py
```