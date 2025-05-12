# Coffee Barista Machine - Python Terminal App  

☕ A terminal-based coffee machine simulator with Poetry dependency management  

---

## 🚀 **Getting Started**  

### **Prerequisites**  
- Python 3.8+  
- [Poetry](https://python-poetry.org/) (recommended)  

### **Installation**  

1. **Clone & Enter Project**  
   ```bash
   git clone <repo-name>
   cd coffee-barista
   ```

2. **Install Dependencies with Poetry**  
   ```bash
   poetry install
   ```


## ▶ **Running the App**  

### **Start the Coffee Machine**  
```bash
poetry run python main.py
```

### **Run Tests**  
```bash
poetry run python -m pytest test/
```


### **Adding New Dependencies**  
```bash
poetry add package-name          # Production dependency
```

---

## ☕ **Features**  
- Interactive terminal interface  
- Multiple coffee recipes (Espresso, Latte, Cappuccino)  
- Resource management (water, milk, coffee beans)  
- Coin-operated payment system  

---

## 🤖 **Testing**  
Run all tests:  
```bash
poetry run pytest -v
```
