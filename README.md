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
python3 cli_tool.py --password "P@ssw0rd123"
```

## 📊 Sample Output
```
Rating: Strong (Score: 60/100)
Entropy: 3.28 bits
Feedback:
- Password is shorter than 12 characters.
- Low entropy.
```

## ✅ Requirements
```bash
pip install -r requirements.txt
```

## 🧪 Run Tests
```bash
python3 -m unittest tests/test_analyzer.py
```

## 📂 Project Structure
- `analyzer.py` – Core logic
- `cli_tool.py` – CLI for users
- `dictionary.txt` – List of common passwords
- `tests/` – Unit tests
- `examples/` – Optional examples

---

✅ Built for learning, demos, and security awareness tools.
