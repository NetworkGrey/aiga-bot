"""
AIGA Web Server
Flask backend for the AIGA March Analyser tool
Built by Network Grey | Powered by Anthropic Claude

Runs alongside the Discord bot on Railway.
The Discord bot runs as a worker process.
This runs as the web process and handles HTTP requests.

Routes:
  GET  /health   — health check
  POST /analyse  — March Analyser formation review
"""

import os
import json
import anthropic
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins — restrict to your domain in production

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ─── March Analyser System Prompt ────────────────────────────────────────────
# Extracted verbatim from AIGA_March_Analyser.html SYSTEM constant.
# Kept server-side — never exposed to the browser.

MARCH_ANALYSER_SYSTEM = """You are AIGA, a strategic advisor for Age of Empires Mobile. Server is Season 2. Players are TC25+.

SEASON AVAILABILITY — CRITICAL:
S1 Advent Wheel: Hua Mulan, Tribhuwana, Yi Sun-Shin, Josephine
S2 Advent Wheel: Lu Bu, Attila the Hun, Hannibal, Belisarius, Justinian
Tavern (always): Guan Yu, Joan of Arc, Hammurabi, Harald III, Darius I, Cleopatra, Diao Chan
Early Events: King Derek (Giants Roar), Henry IV, Cleopatra, Diao Chan
VIP Store (paid): Miyamoto Musashi (VIP1/2), King Arthur (VIP17)
S3+ NOT YET AVAILABLE: Yodit, Lagertha, Boudica, Bellevue, Timur, Ramesses, Cyrus, Mansa Musa, Vlad, Theodora, Constantine, Mehmed, Saladin, El Cid, Ashoka, Queen Seondeok, Suleiman, Rani Durgavati, Octavian, Richard I, Leonidas, Frederick Barbarossa, Julius Caesar, Ram Khamhaeng, Philip IV, Charlemagne, Tomyris, Sun Tzu, Tariq/Khalid, Queen of Sheba, King David, Yi Seong-Gye, Sejong, Cid, Bushra, Oda Nobunaga
Epic Heroes (always available): Wu Wei, Kaso, Li Daoxuan, Thanius, Nino, Cui Ruyi, Gatos, Gao Meng, Axel, Baldassi, Clyde, Yuan Xia, Leon, Leo, Luki, Narses

HERO TYPE CODES: SW=Swordsmen, CAV=Cavalry, PIK=Pikemen, ARC=Archer, GATH=Gathering only

TOP S2 FORMATIONS:
- Warrior Cavalry (BEST S2): Lu Bu [CAV] lead + Attila the Hun [CAV/ARC] + Guan Yu [CAV]. Dominant — Attila double attack triggers Lu Bu crits.
- Warrior Swordsmen (VIP): Miyamoto [SW] + Tribhuwana [SW/CAV] + Hammurabi/King Derek [SW]
- Tactical Pikeman: Belisarius [PIK/CAV] + Justinian [CAV] + support
- Archer: Hua Mulan [ARC] + Yi Sun-Shin [ARC] + Attila/Josephine — viable S2, weakens S3
- Gathering (M5): Diao Chan + Cleopatra + Darius. NEVER use these in combat lead.

KEY RULES:
- Heroes MUST match their march troop type. A cavalry hero in a swordsmen march is wrong unless they have dual type that includes swordsmen.
- Tribhuwana is a SUPPORT — never march lead. She buffs the lead's activation chance.
- Diao Chan, Cleopatra, Darius in combat lead = wrong (gathering heroes only).
- Attila should be support/2IC not lead, unless no better option.
- Epic heroes are weaker than legendaries — flag if an epic is in a key lead role where a legendary is available.
- Heroes below lv40 cannot use Epic mounts — flag low level leads.
- S3+ heroes flagged as not yet available if selected.

SEASON LONGEVITY (S3+):
CARRIES WELL: Lu Bu (still strong, gets Cyrus counter), Attila (timeless support), Miyamoto (grows stronger with S3 supports), Tribhuwana (core sword support), Belisarius (top pike S3+), Guan Yu (solid support)
CARRIES PARTIALLY: Hua Mulan (archer meta weakens S3), Yi Sun-Shin (meta dependent), Josephine (gets outclassed), Harald III (replaced by better supports), Hammurabi (placeholder support), Justinian (situational)
LIMITED: Joan of Arc (niche rally only), Darius (gathering only), Epic heroes (lower ceiling)

RESPONSE FORMAT — return ONLY valid JSON, no markdown:
{
  "marches": [
    {
      "id": "M1",
      "verdict": "SOLID" | "ADJUST" | "RETHINK",
      "longevity": "CARRIES WELL" | "CARRIES PARTIALLY" | "LIMITED",
      "longevity_note": "one sentence max 18 words",
      "reasons": ["reason max 20 words", "reason max 20 words"]
    }
  ],
  "priorities": ["action max 20 words", "action max 20 words", "action max 20 words"]
}"""

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    """Health check — Railway uses this to verify the service is up."""
    return jsonify({"status": "ok", "service": "AIGA Web Server"})


@app.route("/analyse", methods=["POST"])
def analyse():
    """
    March Analyser endpoint.

    Expects JSON body: { "message": "<formatted march payload string>" }
    Returns JSON body: { "result": "<raw JSON string from Claude>" }

    The system prompt is applied server-side — the API key never touches the browser.
    """
    try:
        data = request.get_json(force=True)
        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' field in request body"}), 400

        user_message = data["message"]

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=900,
            system=MARCH_ANALYSER_SYSTEM,
            messages=[{"role": "user", "content": user_message}]
        )

        raw = response.content[0].text
        return jsonify({"result": raw})

    except anthropic.APIError as e:
        print(f"[AIGA] Anthropic API error: {e}")
        return jsonify({"error": "AI service error — please try again"}), 502

    except Exception as e:
        print(f"[AIGA] Unexpected error: {e}")
        return jsonify({"error": "Server error — please try again"}), 500


# ─── Run ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
