## House Price Prediction App

A simple Flask app for predicting house prices. It loads a trained model and serves a small web UI.

### Requirements
- Python 3.8+
- pip

Install dependencies:

```bash
pip install -r req.txt
```

### Run locally

```bash
python app.py
```

Then open the printed URL in your browser.

### Project structure
- `app.py`: Flask app entrypoint
- `model.py`: Model loading/inference helpers
- `regressor_model.pkl`: Pretrained model
- `templates/`: HTML templates
- `static/`: Static assets
- `req.txt`: Python dependencies

### Pushing to GitHub (quick steps)
1. Create an empty repository on GitHub (no README/license/gitignore).
2. From this project directory, connect and push:

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```


