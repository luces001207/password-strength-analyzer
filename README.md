# 🔐 Password Strength Analyzer

A Python tool to evaluate the strength of a password using entropy, dictionary matching, and rule-based scoring.

## 🚀 Features
- Entropy calculation (Shannon entropy)
- Dictionary word detection
- Rule-based scoring (length, digits, symbols, etc.)
- CLI tool interface
- Example password tests

## 🛠 Usage
```bash
$ python3 cli_tool.py --password "P@ssw0rd123"
```

## 📊 Sample Output
```
Rating: Strong (Score: 70/100)
Entropy: 3.9 bits
Feedback:
- Contains common dictionary word.
```

## ✅ Requirements
```bash
pip install -r requirements.txt
```

## 🧪 Run Tests
```bash
python -m unittest tests/test_analyzer.py
```

## 📂 Project Structure
- `analyzer.py` – Core logic
- `cli_tool.py` – CLI for users
- `dictionary.txt` – List of common passwords
- `tests/` – Unit tests
- `examples/` – Optional examples

---

✅ Built for learning, demos, and security awareness tools.
