import os
from datetime import datetime, timezone
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
APP_MODE = os.getenv("APP_MODE", "DEMO")
BOT_ENABLED = False

@app.route("/")
def index():
    return render_template("index.html", mode=APP_MODE, now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))

@app.route("/api/status")
def status():
    # Safe starter: dashboard only. No credentials or orders are handled here.
    return jsonify({
        "mode": APP_MODE,
        "bot_enabled": BOT_ENABLED,
        "connection": "Not connected",
        "market": "BTC/USD",
        "last_update": datetime.now(timezone.utc).isoformat(),
        "message": "Demo scaffold only. Connect and test the MT5 bridge locally before enabling any live trading."
    })

@app.route("/api/toggle", methods=["POST"])
def toggle():
    global BOT_ENABLED
    # This toggle is deliberately simulated; it does not place trades.
    data = request.get_json(silent=True) or {}
    desired = bool(data.get("enabled", False))
    if desired:
        return jsonify({"ok": False, "enabled": False,
                        "message": "Trading is not wired up. Configure and validate the demo bridge first."}), 400
    BOT_ENABLED = False
    return jsonify({"ok": True, "enabled": False, "message": "Bot paused (simulation)."})

@app.route("/api/health")
def health():
    return jsonify({"ok": True, "service": "SmartTrade AI dashboard", "trading": "disabled"})

if __name__ == "__main__":
    # Local development only. Do not expose this Flask development server to the public internet.
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
