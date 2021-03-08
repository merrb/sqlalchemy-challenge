
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api/v1.0/precipitation')
def precipitation():
    return jsonify(prcp)

@app.route('/api/v1.0/stations')
def stations():
    return jsonify(prcp)

@app.route('/api/v1.0/tobs')
def tobs():
    return jsonify(prcp)

@app.route('/api/v1.0/<start>')
def apistart(start):
    return jsonify(prcp)


@app.route('/api/v1.0/<start>/<end>')
def apiend(start, end):
    return jsonify(prcp)


@app.route("/")
def welcome():
    """List all available api routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )







if __name__ == '__main__':
    app.run(debug=True)