from flask import Flask, jsonify, render_template, request, redirect, url_for
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "EH4X{1D0R_l34k5_m0r3_th4n_y0u_th1nk}")

# Intentionally vulnerable challenge data.
USERS = {
    1: {"id": 1, "username": "alex", "role": "employee", "bio": "Backend developer at Employee Exposure."},
    2: {"id": 2, "username": "maya", "role": "employee", "bio": "Frontend developer at Employee Exposure."},
    3: {"id": 3, "username": "sam", "role": "employee", "bio": "Security intern at Employee Exposure."},
    7: {
        "id": 7,
        "username": "ghost",
        "role": "administrator",
        "bio": "Internal administrator account.",
        # Deliberately exposed through the vulnerable API.
        "reset_token": "employee-exposure-reset-7f3a91",
    },
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/profile/<int:user_id>")
def profile(user_id):
    # Intentional IDOR: no authorization check and the whole record is returned.
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "profile not found"}), 404
    return jsonify(user)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        token = request.form.get("token", "")
        if token == USERS[7]["reset_token"]:
            return redirect(url_for("admin"))
        error = "Invalid reset token."
    return render_template("login.html", error=error)

@app.route("/admin")
def admin():
    return render_template("admin.html", flag=FLAG)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
