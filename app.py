from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Anylist',
  'location': 'Bangalore, India',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 2,
  'title': 'Data Scientise',
  'location': 'Pune, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 3,
  'title': 'Front End Engineer',
  'location': 'Delhi, India',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 4,
  'title': 'Backend Scientise',
  'location': 'Pune, India',
  'salary': '$ 120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, title='Jovian Career')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  # print("i am inside the main")
  app.run(host='0.0.0.0', debug=True)
