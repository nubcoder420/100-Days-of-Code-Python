from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    cafe_data = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
    return jsonify({"random_cafe": cafe_data})

@app.route('/all', methods=["GET"])
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search", methods=["GET"])
def search_cafes():
    location = request.args.get('loc')

    if not location:
        return jsonify({"message": "Location parameter is missing."}), 400

    cafes = Cafe.query.filter_by(location=location).all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify({"message": f"No cafes found in {location}."}), 404


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    api_key = request.args.get("api_key")

    if api_key == "TopSecretAPIKey":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify({"error": "Not authorized. Please provide a valid API key."}), 403

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."}), 200
    else:
        return jsonify({"error": {"Not found": f"Sorry, a cafe with id {cafe_id} was not found in the database."}}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")

    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"success": f"Cafe with id {cafe_id} has been deleted successfully."}), 200
        else:
            return jsonify({"error": f"Cafe with id {cafe_id} not found in the database."}), 404
    else:
        return jsonify({"error": "Not authorized. Please provide a valid API key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
