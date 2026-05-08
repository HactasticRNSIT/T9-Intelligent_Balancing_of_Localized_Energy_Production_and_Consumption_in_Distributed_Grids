from train_model import model
prediction = model.predict([[solar, battery]])
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy.db'

db = SQLAlchemy(app)
class EnergyData(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    solar_power = db.Column(db.Integer)

    battery = db.Column(db.Integer)

    prediction = db.Column(db.Float)
    new_data = EnergyData(

    solar_power=solar,

    battery=battery,

    prediction=prediction[0]
)

db.session.add(new_data)

db.session.commit()
return jsonify({

    "prediction": prediction[0]

})